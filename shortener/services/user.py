import uuid
from typing import TYPE_CHECKING

from flask import make_response, redirect, url_for

if TYPE_CHECKING:
    from shortener.repositories.user import UserRepository


class UserService:
    """
    Service for managing user sessions.
    """
    repo: 'UserRepository'

    def start_session(
            self,
            request,
    ):
        user_id = str(uuid.uuid4())
        response = make_response(redirect(url_for('shorten_url')))
        response.set_cookie('user_id', user_id)
        self.repo.start_session(user_id, request.remote_addr)
        return response
