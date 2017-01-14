"""
Method defines pipeline classes to process items.
"""
from sqlalchemy.orm import sessionmaker
from sponsors.models import db_create, db_connect, create_tables, Sponsor

class PyConPipeline(object):
    """
    Pipeline that connects to the database, opens a session to the database,
    processes individual items, and adds them to the database
    """

    def __init__(self):

        engine = db_create()
        del engine

        engine = db_connect()
        if not engine.dialect.has_table(engine, table_name='sponsor', schema=None):
            create_tables(engine)
        self.session = sessionmaker(bind=engine)

    def process_item(self, item, spider):

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
