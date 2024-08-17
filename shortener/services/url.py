"""
URL shortener service module.
"""

import random
import re
import string
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from shortener.repositories.url import URLRepository


class URLShortenerService:
    """
    Service class for URL shortening and resolution.
    """
    repo: "URLRepository"

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
        if not self.validate_url(url=original_url):
            raise ValueError("Invalid URL")
        existing_url = self.repo.get_url_by_original_url(
            original_url=original_url,
        )
        if existing_url:
            return existing_url
        shorten_url = self.generate_short_url()
        self.repo.add_url(
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
        url = self.repo.get_url_by_short_url(short_url=short_url)
        return url

    def validate_url(self, url: str) -> bool:
        """
        Checks if a string is a valid URL.

        Args:
            url (str): URL to check.

        Returns:
            bool: True if the URL is correct, False otherwise.
        """
        regex = re.compile(
            r'^(?:http|ftp)s?://'
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
            r'localhost|'
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
            r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
            r'(?::\d+)?'
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        return re.match(regex, url) is not None
