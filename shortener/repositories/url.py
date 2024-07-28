"""
URlRepository module.
"""

from shortener.models.url import URL


class URLRepository:
    """
    Repository class for managing URLs in the database.
    """

    def __init__(self, session) -> None:  # noqa
        """
        Initialize the URLRepository with a database session.

        :param session: Database session
        """
        self.session = session()  # TODO: fix this.

    def add_url(
        self,
        original_url: str,
        short_url: str,
    ) -> None:
        """
        Adds a new URL to the database.

        :param original_url: String representing original URL.
        :param short_url: String representing shortened URL.
        :return: None.
        """
        url = URL(
            original_url=original_url,
            short_url=short_url,
        )
        self.session.add(url)
        self.session.commit()

    def get_url_by_short_url(
        self,
        short_url: str,
    ) -> URL | None:
        """
        Retrieves the URL model object associated with a shortened URL.

        :param short_url: String representing the shortened URL.
        :return: Shortened URL if exists, none otherwise.
        """
        return (
            self.session.query(
                URL,
            )
            .filter_by(
                short_url=short_url,
            )
            .first()
        )

    def get_url_by_original_url(
        self,
        original_url: str,
    ) -> URL | None:
        """
        Retrieves the URL model object associated with an original URL.

        :param original_url: String representing original URL.
        :return: Original URL if exists, none otherwise.
        """
        return (
            self.session.query(
                URL,
            )
            .filter_by(
                original_url=original_url,
            )
            .first()
        )
