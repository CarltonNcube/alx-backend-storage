#!/usr/bin/env python3

"""
This script defines a function to get the HTML content.
"""

import redis
import requests
from functools import wraps
from typing import Callable


redis_conn = redis.Redis()

def cache_page(func):
    """
    Decorator for caching page content and tracking access count
    """
    @wraps(func)
    def wrapper(url):
        """
        Wrapper that:
        - Checks whether a URL's data is cached
        - Tracks how many times get_page is called
        """
        # Increment URL access count
        redis_conn.incr(f'count:{url}')

        # Check if page content is cached
        page_content = redis_conn.get(url)
        if page_content:
            return page_content.decode('utf-8')

        # If not cached, request the page content
        response = func(url)
        redis_conn.setex(url, 10, response)

        return response

    return wrapper

@cache_page
def get_page(url: str) -> str:
    """
    Makes an HTTP request to a given endpoint
    """
    response = requests.get(url)
    return response.text

