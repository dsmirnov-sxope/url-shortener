"""
Base model module.
"""

from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

Base = declarative_base()


def get_engine(database_url: str) -> Engine:
    """
    Creates a new SQLAlchemy engine for the specified database.

    :param database_url: String representing the database URL to connect to,
     formatted according to SQLAlchemy conventions.
    :return: Engine: SQLAlchemy engine for the specified database.
    """
    return create_engine(database_url)


def get_session(engine: Engine) -> Session:
    """
    Creates a new SQLAlchemy session for the specified engine
    for interacting with the database.

    :param engine: SQLAlchemy engine to bind the session to.
    :return: Session: SQLAlchemy session for the specified engine.
    """
    Session = sessionmaker(  # pylint: disable=[redefined-outer-name] # noqa
        bind=engine
    )
    return Session()
