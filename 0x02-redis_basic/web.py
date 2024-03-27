#!/usr/bin/env python3

"""
This script defines a function to get the HTML content of a URL while
tracking the number of times the URL was accessed and caching the result.
"""

import requests
import redis
import time
from functools import wraps

# Initialize Redis connection
redis_conn = redis.Redis()

def cache_page(func):
    @wraps(func)
    def wrapper(url):
        # Check if URL access count is cached
        count_key = f"count:{url}"
        access_count = redis_conn.get(count_key)
        
        if access_count:
            access_count = int(access_count)
        else:
            access_count = 0

        # Increment URL access count and cache with expiration time of 10 seconds
        access_count += 1
        redis_conn.setex(count_key, 10, access_count)

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
    response = requests.get(url)
    return response.text
