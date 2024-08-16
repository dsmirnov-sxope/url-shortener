"""
Container for cache.
"""
# pylint: disable=[c-extension-no-member, unsubscriptable-object, too-few-public-methods]
from dependency_injector import containers, providers
from redis import Redis

from shortener.cache.client import RedisClient
from shortener.repositories.url import URLRepository


class CacheContainer(containers.DeclarativeContainer):
    """
    Cache container.
    """
    config = providers.Dependency()

    redis = providers.Singleton(
        Redis,
        host=config.provided["host"],
        port=config.provided["port"],
        db=config.provided["db"],
        username=config.provided["username"],
        password=config.provided["password"],
        # decode_responses=True,
    )

    client = providers.Singleton(
        RedisClient,
    )

    client.add_attributes(
        client=redis,
    )

    url_repo = providers.Singleton(
        URLRepository,
    )

    url_repo.add_attributes(
        cache=client,
    )
