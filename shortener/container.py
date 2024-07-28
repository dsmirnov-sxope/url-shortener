"""
Container module.
"""
from typing import Callable

# pylint: disable=[c-extension-no-member, unsubscriptable-object]
from dependency_injector import containers, providers
from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from shortener.config import DATABASE_URL
from shortener.models.base import Base, get_engine
from shortener.repositories.url import URLRepository
from shortener.services.url import URLShortenerService


class Container(containers.DeclarativeContainer):
    """
    Main container class.
    """
    config = providers.Configuration()
    config.database_url.from_value(DATABASE_URL)

    engine: providers.ThreadSafeSingleton[Engine] = providers.ThreadSafeSingleton(
        create_engine,
        url=config.database_url,
    )

    session: providers.ThreadSafeSingleton[Callable[..., Session]] = providers.ThreadSafeSingleton(
        sessionmaker,
        bind=engine,
    )

    url_repository: providers.Factory[URLRepository] = providers.Factory(
        URLRepository,
        session=session,
    )

    url_shortener_service: providers.Factory[URLShortenerService] = providers.Factory(
        URLShortenerService,
        url_repository=url_repository,
    )


def init_db() -> None:
    """
    Initialize the database.
    :return: None
    """
    engine = get_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
