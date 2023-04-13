#!/usr/bin/env python3
"""ALX SE Redis Module."""
import requests
import redis


def get_page(url: str) -> str:
    """Cache a value for 10 seconds."""
    cache = redis.Redis()
    key = f'count:{url}'
    content = requests.get(url)
    if cache.get(key) is None:
        cache.set(key, 0, 10)
    cache.incr(key)
    return content.text
