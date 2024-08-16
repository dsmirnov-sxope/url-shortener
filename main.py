"""
Main module for running the URL Shortener service.
"""

from shortener.app import Application


def run() -> None:
    """
    Runs the URL Shortener service.
    Returns:
        None
    """
    app = Application()
    app.run(debug=True)


if __name__ == "__main__":
    run()
