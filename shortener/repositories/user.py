"""
User Repository module.
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from shortener.cache.client import RedisClient


class UserRepository:
    """
    Redis based User repository.
    """
    cache: "RedisClient"

    def start_session(
            self,
            user_id: str,
            ip_address: str,
    ):
        self.cache.set(
            key=f"user-id:{user_id}:ip-address",
            value=ip_address,
        )
        self.cache.set(
            key=f"ip-address:{ip_address}:user-id",
            value=user_id,
        )
        self.cache.set(
            key=f"user-id:{user_id}:visits",
            value=1,
        )

    def increment_visits(
            self,
            user_id: str,
    ):
        self.cache.increment(
            key=f"user-id:{user_id}:visits",
        )


