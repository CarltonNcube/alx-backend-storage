#!/usr/bin/env python3

"""
Cache module utilizing Redis
"""

import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Any, Callable, Optional

class Cache:
    """
    Cache class for storing data using Redis
    """

    def __init__(self) -> None:
        """
        Initializes the Cache object with a Redis client and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a randomly generated key and returns the key.
        
        Args:
            data: Data to be stored. Can be str, bytes, int, or float.
        
        Returns:
            str: Randomly generated key used to store the data in Redis.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieves data from Redis using the provided key and optionally applies a conversion function.

        Args:
            key: The key used to retrieve the data from Redis.
            fn: Optional conversion function to be applied to the retrieved data.

        Returns:
            Any: The retrieved data, optionally converted based on the provided function.
        """
        value = self._redis.get(key)
        if not value:
            return None
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """
        Converts bytes to string.

        Args:
            data: Bytes to be converted to string.

        Returns:
            str: Converted string.
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        Converts bytes to integers.

        Args:
            data: Bytes to be converted to integer.

        Returns:
            int: Converted integer.
        """
        return int(data)

