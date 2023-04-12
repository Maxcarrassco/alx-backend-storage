#!/usr/bin/env python3
"""ALX SE Backend Redis Module."""
import redis
from typing import Union
import uuid


class Cache:
    """This model implement a simple caching machanism using redis."""
    def __init__(self) -> None:
        """Initialize my cache model."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
          Store the data with a random key generated
          from uuid4 and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
