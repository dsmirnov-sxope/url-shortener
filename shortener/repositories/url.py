"""
URlRepository module.
"""

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from shortener.cache.client import RedisClient


class URLRepository:
    """
    Redis based URL repository.
    """

    cache: "RedisClient"

    def get_url_by_original_url(
        self,
        original_url: str,
    ) -> str | None:
        """
        Retrieves the short URL associated with the given original URL.

        Args:
            original_url (str): The original URL to search for.

        Returns:
            str | None: The short URL if found, otherwise None.
        """
        short_url = self.cache.get(f"original:{original_url}")
        return short_url

    def get_url_by_short_url(
        self,
        short_url: str,
    ) -> str | None:
        """
        Retrieves the original URL associated with the given short URL.

        Args:
            short_url (str): The short URL to search for.
        """
        original_url = self.cache.get(f"short:{short_url}")
        return original_url

    def add_url(self, original_url: str, short_url: str, ttl: int = None) -> None:
        """
        Adds a new URL mapping to the repository.

        Args:
            original_url (str): The original URL to add.
            short_url (str): The short URL to associate with the original URL.
            ttl (int, optional): The time-to-live (TTL) for the URL mapping, in seconds.
            If not provided, the mapping will not expire.
        """
        self.cache.set(
            key=f"original:{original_url}",
            value=short_url,
            ttl=ttl,
        )
        self.cache.set(
            key=f"short:{short_url}",
            value=original_url,
            ttl=ttl,
        )
