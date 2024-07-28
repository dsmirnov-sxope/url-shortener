import string
import random
from typing import TYPE_CHECKING



if TYPE_CHECKING:
    from repositories.url import URLRepository


class URLShortenerService:
    def __init__(self, url_repository: "URLRepository"):
        self.url_repository = url_repository

    def generate_short_url(self, url, length=6):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(length))
        return short_url

    def shorten_url(self, original_url) -> str:
        existing_url = self.url_repository.get_url_by_original_url(
            original_url=original_url,
        )
        if existing_url:
            return existing_url.short_url
        shorten_url = self.generate_short_url(original_url)
        self.url_repository.add_url(
            original_url=original_url,
            short_url=shorten_url,
        )
        return shorten_url

    def resolve_url(self, short_url) -> str | None:
        print(f"{short_url=}")
        url = self.url_repository.get_url_by_short_url(short_url=short_url)
        print(f"{url=}")
        if url:
            return url.original_url
        return None
