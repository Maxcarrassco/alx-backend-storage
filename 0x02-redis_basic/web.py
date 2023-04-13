#!/usr/bin/env python3
"""ALX SE Redis Module."""
import requests
import redis
from functools import wraps
from typing import Callable


def store_cache(fn: Callable) -> Callable:
    """Cache a value for 10 seconds."""
    @wraps(fn)
    def wrapper(url):
        """The function wrapper."""
        cache = redis.Redis()
        cache.incr(f'count:{url}')
        if cache.get(url):
            return cache.get(url).decode()
        content = fn(url)
        cache.setex(url, 10, content)
        return content
    return wrapper


@store_cache
def get_page(url: str) -> str:
    """Get the content of a webpage."""
    content = requests.get(url)
    return content.text
