#!/usr/bin/env python3
"""ALX SE Backend Redis Module."""
import redis
from typing import Union, Callable, Any
import uuid
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """
      Keep track of the amount of times a method with
      access to a redis instance is call.
    """
    @wraps(fn)
    def wrapper(self, *args, **kwargs) -> Any:
        """This is the wrapper itself."""
        key = fn.__qualname__
        if self._redis.get(key):
            self._redis.incr(key)
        else:
            self._redis.set(key, 1)
        return fn(self, *args, **kwargs)
    return wrapper


class Cache:
    """This model implement a simple caching machanism using redis."""
    def __init__(self) -> None:
        """Initialize my cache model."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
          Store the data with a random key generated
          from uuid4 and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn: Union[Callable, None] = None):
        """Return the value of a key in its rightful type."""
        value: Any = self._redis.get(key)

        if value is None:
            return value
        if fn is None:
            return value
        if fn is int:
            value = self.get_int(value)
        elif fn is str:
            value = self.get_str(value)
        else:
            value = fn(value)
        return value

    def get_str(self, value: bytes) -> str:
        """Return the string version of a btye."""
        return str(value)

    def get_int(self, value: bytes) -> int:
        """Return the integer version of a btye."""
        return int(value)
