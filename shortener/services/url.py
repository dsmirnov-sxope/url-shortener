"""
URL shortener service module.
"""

import random
import string
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from shortener.repositories.url import URLRepository


class URLShortenerService:
    """
    Service class for URL shortening and resolution.
    """

    def __init__(self, url_repository: "URLRepository") -> None:
        """
        Initializes the URLShortenerService with a URLRepository.

        Args:
            url_repository (URLRepository): Repository for managing URLs.
        """
        self.url_repository = url_repository

    @staticmethod
    def generate_short_url(length: int = 6) -> str:
        """
        Generates a short URL.

        Args:
            length (int, optional): URL length. Defaults to 6.

        Returns:
            str: String representing shortened URL.
        """
        characters = string.ascii_letters + string.digits
        short_url = "".join(random.choice(characters) for _ in range(length))
        return short_url

    def shorten_url(
        self,
        original_url: str,
        ttl: int = 60,
    ) -> str:
        """
        Shortens the given URL and stores it in the database.

        Args:
            original_url (str): String representing the original URL.
            ttl (int, optional): Time to live for the shortened URL. Defaults to 60 seconds.

        Returns:
            str: String representing the shortened URL.
        """
        existing_url = self.url_repository.get_url_by_original_url(
            original_url=original_url,
        )
        if existing_url:
            return existing_url
        shorten_url = self.generate_short_url()
        self.url_repository.add_url(
            original_url=original_url,
            short_url=shorten_url,
            ttl=ttl,
        )
        return shorten_url

    def resolve_url(
        self,
        short_url: str,
    ) -> str | None:
        """
        Resolves the shortened URL to its original URL.

        Args:
            short_url (str): String representing the shortened URL.

        Returns:
            str | None: The original URL if found, otherwise None.
        """
        url = self.url_repository.get_url_by_short_url(short_url=short_url)
        return url
