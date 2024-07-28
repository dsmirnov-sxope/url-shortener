from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def get_engine(database_url):
    return create_engine(database_url)


def get_session(engine):
    Session = sessionmaker(bind=engine)  # noqa
    return Session()
