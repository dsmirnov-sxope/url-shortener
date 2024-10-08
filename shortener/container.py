"""
Container module.
"""

# pylint: disable=[c-extension-no-member, unsubscriptable-object]
from dependency_injector import containers, providers

from shortener.cache.container import CacheContainer
from shortener.config import get_config_path
from shortener.services.url import URLShortenerService


class Container(
    containers.DeclarativeContainer
):  # pylint: disable=[too-few-public-methods]
    """
    Main container class.
    """

    config = providers.Configuration()

    cache_package: providers.Container[CacheContainer] = providers.Container(
        CacheContainer,
        config=config.cache,
    )

    url_shortener_service: providers.Factory[URLShortenerService] = providers.Factory(
        URLShortenerService,
        url_repository=cache_package.url_repo,
    )


def create_container() -> Container:
    """
    Creates container for application.
    Returns:
        Container: Container instance.
    """
    config_path = get_config_path()
    container = Container()
    container.config.from_yaml(config_path)
    container.wire(packages=["shortener"])
    return container
