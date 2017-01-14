"""Method defines pipeline classes to process items."""
from scrapy.exceptions import DropItem
from sqlalchemy.orm import sessionmaker
from sponsors.models import db_create, db_connect, create_tables, Sponsor


class PyConPipeline(object):
    """Connects to database, opens a session, and processes individual items."""

    def __init__(self):
        """Create database if necesary and get engine."""
        db_create()

        engine = db_connect()
        if not engine.dialect.has_table(engine, table_name='sponsor', schema=None):
            create_tables(engine)
        self.session = sessionmaker(bind=engine)

    def process_item(self, item, spider):  # pylint: disable=unused-argument
        """Process a single item by loading item into model and adding to database."""
        session = self.session()
        sponsor = Sponsor(**item)

        try:
            session.add(sponsor)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item


class DuplicatesPipeline(object):
    """Drop item from pipeline if it has already been processed."""

    def __init__(self):
        self.ids_seen = set()

        db_create()

        engine = db_connect()
        if not engine.dialect.has_table(engine, table_name='sponsor', schema=None):
            create_tables(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for value in session.query(Sponsor.name, Sponsor.year).distinct():
            self.ids_seen.add(value)

    def process_item(self, item, spider):

        if (item['name'], item['year']) in self.ids_seen:
            raise DropItem("Duplicate item found: {} {}".format(item['year'], item['name']))
        else:
            self.ids_seen.add((item['name'], item['year']))
            return item
