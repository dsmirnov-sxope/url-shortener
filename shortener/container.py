"""
Container module.
"""

# pylint: disable=[c-extension-no-member, unsubscriptable-object]
from dependency_injector import containers, providers

from shortener.cache.container import CacheContainer
from shortener.config import get_config_path
from shortener.services.url import URLShortenerService
from shortener.services.user import UserService


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
    )

    user_service: providers.Factory[UserService] = providers.Factory(
        UserService,
    )

    url_shortener_service.add_attributes(
        repo=cache_package.url_repo,
    )
    user_service.add_attributes(
        repo=cache_package.user_repo,
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
