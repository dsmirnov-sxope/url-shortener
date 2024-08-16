"""
Application entry point.
"""
import redis
from flask_session import Session

# pylint: disable=[too-few-public-methods]
from shortener.container import create_container
from shortener.views import app


class Application:
    """
    Application entry point.
    """
    def __init__(self):
        self.container = create_container()
        self.container.init_resources()
        app.secret_key = 'default'
        app.config['SESSION_TYPE'] = 'redis'
        app.config['SESSION_PERMANENT'] = False
        app.config['SESSION_USE_SIGNER'] = True
        app.config['SESSION_KEY_PREFIX'] = 'session:'
        app.config['SESSION_REDIS'] = redis.from_url('redis://redis:6379')
        # TODO: configurate properly
        self.app = app
        self.session = Session(app)

    def run(
        self,
        host: str = "0.0.0.0",
        port: int = 5000,
        debug: bool = False,
    ) -> None:
        """
        Runs the Flask application.

        Args:
            host (str, optional): The host to bind the server to. Defaults to "0.0.0.0".
            port (int, optional): The port to bind the server to. Defaults to 5000.
            debug (bool, optional): Whether to run the server in debug mode. Defaults to False.
        """
        self.app.run(
            host=host,
            port=port,
            debug=debug,
        )
