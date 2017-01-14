"""
Define database table structure.

Functions that connect to the database and create all necessary tables are included.
"""
from sqlalchemy import create_engine, Column, String, Text, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from . import settings

BASE = declarative_base()


def db_create():
    """Read connect info from settings file and connect to database."""
    connection_info = settings.DATABASE
    db_name = connection_info['database']
    del connection_info['database']

    engine = create_engine(URL(**connection_info))
    engine.execute('CREATE DATABASE IF NOT EXISTS {};'.format(db_name))
    connection_info['database'] = db_name


def db_connect():
    """Perform database connection using database settings from settings.py."""
    return create_engine(URL(**settings.DATABASE))


def create_tables(engine):
    """Create tables in database."""
    BASE.metadata.create_all(engine)


class Sponsor(BASE):
    """SQLAlchemy sponsor model."""

    __tablename__ = 'sponsor'
    year = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), primary_key=True, nullable=False)
    url = Column(String(255), nullable=False)
    sponsor_level = Column(String(20), nullable=False)
    description = Column(Text, nullable=False)
