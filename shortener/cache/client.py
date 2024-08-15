import pickle
from typing import Any

from redis import Redis


class RedisClient:
    client: Redis

    def set(
        self,
        key: str,
        value: str,
        ttl: int | None = None,
    ) -> Any:
        """
        Sets the value of the specified key with the given value.

        Args:
            key (str): The key to set.
            value (str): The value to associate with the key.
            ttl (int | None, optional): The time-to-live (TTL) for the key-value pair, in seconds. If not provided, the key-value pair will not expire.

        Returns:
            Any: The status code returned by Redis.
        """
        pickled = pickle.dumps(value)
        return self.client.set(
            name=key,
            value=pickled,
            ex=ttl,
        )

    def get(self, key: str) -> str | None:
        """
        Retrieves the value associated with the specified key.

        Args:
            key (str): The key to retrieve the value for.

        Returns:
            str | None: The value associated with the key, or None if the key does not exist.
        """
        value: str = self.client.get(name=key)
        if value:
            return pickle.loads(value)
        return value

    def expire(self, key: str, ttl: int | None = None) -> int:
        """
        Sets the time-to-live (TTL) for the specified key.

        Args:
            key (str): The key to set the TTL for.
            ttl (int | None, optional): The TTL value in seconds. If not provided, the key will not expire.

        Returns:
            int: 1 if the timeout was set, 0 if the key does not exist.
        """
        return self.client.expire(name=key, time=ttl)

    def delete(self, key: str) -> int:
        """
        Removes the specified key.

        Args:
            key (str): The key to delete.

        Returns:
            int: The number of keys that were removed.
        """
        return self.client.delete(key)
