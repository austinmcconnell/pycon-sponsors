"""Method defines pipeline classes to process items."""
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
