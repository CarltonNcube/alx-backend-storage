#!/usr/bin/env python3

"""
Cache module utilizing Redis
"""

import redis
from uuid import uuid4
from functools import wraps
from typing import Union, Callable, Optional


class Cache:
    """
    Cache class for storing data using Redis
    """

    def __init__(self) -> None:
        """
        Initializes the Cache object with a Redis client as a private variable _redis
        and flushes the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis with a random key and returns the key.
        
        Args:
            data: Data to be stored. Can be str, bytes, int, or float.
        
        Returns:
            str: Randomly generated key used to store the data in Redis.
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis using the given key.
        
        Args:
            key: Key used to retrieve data from Redis.
            fn: Optional function to convert the retrieved data to the desired format.
        
        Returns:
            Union[str, bytes, int, float, None]: Retrieved data, converted to the desired format if specified.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def count_calls(self, method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.
        
        Args:
            method: The method to be decorated.
        
        Returns:
            Callable: Decorated method.
        """
        @wraps(method)
        def wrapper(*args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(*args, **kwargs)
        return wrapper

    def call_history(self, method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a particular function.
        
        Args:
            method: The method to be decorated.
        
        Returns:
            Callable: Decorated method.
        """
        @wraps(method)
        def wrapper(*args, **kwargs):
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"

            self._redis.rpush(inputs_key, str(args))
            output = method(*args, **kwargs)
            self._redis.rpush(outputs_key, output)

            return output
        return wrapper

    def replay(self, method: Callable) -> None:
        """
        Displays the history of calls of a particular function.
        
        Args:
            method: The method for which to display the history of calls.
        """
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for input_, output in zip(inputs, outputs):
            print(f"{method.__qualname__}{input_} -> {output}")
