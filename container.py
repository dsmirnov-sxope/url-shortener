from dependency_injector import containers, providers
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from models.base import get_engine, Base
from repositories.url import URLRepository
from services.url import URLShortenerService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.database_url.from_value(DATABASE_URL)

    engine = providers.ThreadSafeSingleton(
        create_engine,
        url=config.database_url,
    )

    session = providers.ThreadSafeSingleton(
        sessionmaker,
        bind=engine,
    )

    url_repository = providers.Factory(
        URLRepository,
        session=session,
    )

    url_shortener_service = providers.Factory(
        URLShortenerService,
        url_repository=url_repository,
    )


def init_db():
    engine = get_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
