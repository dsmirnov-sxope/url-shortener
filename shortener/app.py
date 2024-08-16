"""
Application entry point.
"""
# pylint: disable=[too-few-public-methods]
from shortener.container import create_container
from shortener.views import app


class Application:
    """
    Application entry point.
    """
    def __init__(self):
        self.container = create_container()
        self.app = app

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
