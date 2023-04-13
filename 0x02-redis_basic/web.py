#!/usr/bin/env python3
"""ALX SE Redis Module."""
import requests
import redis
from functools import wraps
from typing import Callable


def store_cache(fn: Callable) -> Callable:
    """Cache a value for 10 seconds."""
    @wraps(fn)
    def wrapper(url: str) -> str:
        """The function wrapper."""
        cache = redis.Redis()
        key = f'count:{url}'
        if cache.get(key) is None:
            cache.set(key, 0, 10)
        cache.incr(key)
        return fn(url)
    return wrapper


@store_cache
def get_page(url: str) -> str:
    """Get the content of a webpage."""
    content = requests.get(url)
    return content.text
