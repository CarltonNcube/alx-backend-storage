#!/usr/bin/env python3

"""
Script to fetch HTML content from a URL.
"""
import redis
import requests
from functools import wraps
from typing import Callable


def track_get_page(fn: Callable) -> Callable:
    """ Decorator for get_page function
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """ Wrapper function that:
            - Checks if the URL's data is cached
            - Tracks the number of times get_page is called
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(f'{url}')
        if cached_page:
            return cached_page.decode('utf-8')
        response = fn(url)
        client.set(f'{url}', response, 10)
        return response
    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """ Retrieves HTML content by making an HTTP request endpoint.
    """
    response = requests.get(url)
    return response.text
