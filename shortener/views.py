"""
URL Shortener endpoints.
"""
# pylint: disable=[no-member]
from typing import TYPE_CHECKING

from dependency_injector.wiring import Provide, inject
from flask import Flask, Response, jsonify, redirect, request

from shortener.container import Container

if TYPE_CHECKING:
    from shortener.services.url import URLShortenerService

app = Flask(__name__)
container = Container()
container.init_resources()

# url_shortener_service = container.url_shortener_service


@inject
def url_shortener_service(
    service: "URLShortenerService" = Provide["url_shortener_service"],
) -> "URLShortenerService":
    """
    Return a configured URL shortener service from container
    Args:
        service (URLShortenerService): URL shortener service. Injects automatically.

    Returns:
        URLShortenerService: Injected URL shortener service.
    """
    return service


@app.route("/shorten", methods=["GET", "POST"])
def shorten_url() -> Response:
    """
    Endpoint to shorten a given URL.

    Accepts a JSON payload with the original URL
    and returns a JSON response containing the shortened URL.
    Methods:
        GET: Can be used to display the endpoint (optional).
        POST: Expects a JSON body with the key "url"
    :return: JSON response containing the shortened URL.
    """
    service = url_shortener_service()
    data = request.json
    original_url = data["url"]  # type: ignore[index]
    short_url = service.shorten_url(original_url=original_url)
    return jsonify({"short_url": short_url})


@app.route("/<short_url>", methods=["GET"])
def redirect_url(short_url: str) -> Response | tuple[Response, int]:
    """
    Endpoint to redirect to the original URL based on the shortened URL.

    :param short_url: String representing the shortened URL to resolve.
    :return: Redirects to the original URL if found, otherwise returns a JSON error message.
    """
    service = url_shortener_service()
    original_url = service.resolve_url(short_url)
    if original_url:
        return redirect(original_url)  # type: ignore[return-value,arg-type]
    return jsonify({"error": "URL not found"}), 404
