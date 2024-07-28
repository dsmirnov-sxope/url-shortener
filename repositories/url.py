from models.url import URL


class URLRepository:
    def __init__(self, session):
        self.session = session()

    def add_url(self, original_url, short_url):
        url = URL(original_url=original_url, short_url=short_url)
        self.session.add(url)
        self.session.commit()

    def get_url_by_short_url(self, short_url):
        return self.session.query(
            URL,
        ).filter_by(
            short_url=short_url
        ).first()

    def get_url_by_original_url(self, original_url):
        return self.session.query(
            URL,
        ).filter_by(
            original_url=original_url
        ).first()
