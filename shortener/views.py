"""
URL Shortener endpoints.
"""
import uuid
# pylint: disable=[no-member]
from typing import TYPE_CHECKING

from dependency_injector.wiring import Provide, inject
from flask import Flask, make_response, render_template, render_template_string, Response, jsonify, redirect, request, \
    session, url_for


if TYPE_CHECKING:
    from shortener.services.url import URLShortenerService
    from shortener.services.user import UserService

app = Flask(__name__)


@inject
def url_shortener_service(
    service: "URLShortenerService" = Provide["url_shortener_service"],
) -> "URLShortenerService":
    """
    Return a configured URL shortener service from container.

    Args:
        service (URLShortenerService): URL shortener service. Injects automatically.

    Returns:
        URLShortenerService: Injected URL shortener service.
    """
    return service

@inject
def user_service(
        service: "UserService" = Provide["user_service"],
) -> "UserService":
    """
    Return a configured user service from container.

    Args:
        service (UserService): User service. Injects automatically.

    Returns:
        UserService: Injected user service.

    """
    return service


@app.route("/")
def index() -> Response:
    """
    Check cookie, save cookie and redirect to URL shortener service.
    """
    service = user_service()
    user_id = request.cookies.get("user_id")
    if not user_id:
        response = service.start_session(request)
        return response
    return redirect(url_for('shorten_url'))


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
    short_url = None
    error_message = None
    if request.method == "POST":
        data = request.form
        original_url = data["url"]  # type: ignore[index]
        try:
            short_url = service.shorten_url(original_url=original_url)
        except ValueError:
            error_message = f"Cannot shorten {original_url}"
        # return jsonify({"short_url": short_url})
    return render_template("shorten.html", short_url=short_url, error_message=error_message)


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
