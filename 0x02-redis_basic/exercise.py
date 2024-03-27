#!/usr/bin/env python3

"""
Utilize Redis for caching operations
"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


class Cache:
    """
    Class for caching data using Redis
    """

    def __init__(self) -> None:
        """
        Initiates the Cache instance with a Redis client and clears the
        database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Places data into Redis with a randomly generated key and
        returns the key.

        Args:
            data: Data to be placed. Can be str, bytes, int, or float.

        Returns:
            str: Randomly generated key used for data storage in Redis.
        """
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieves data from Redis using the provided key and optionally
        applies a conversion function.

        Args:
            key: The key to retrieve data from Redis.
            fn: Optional conversion function to apply to the retrieved data.

        Returns:
            Any: The retrieved data, optionally converted based on the
            provided function.
        """
        client = self._redis
        value = client.get(key)
        if not value:
            return
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
            data: Bytes to convert to string.

        Returns:
            str: Converted string.
        """
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """
        Converts bytes to integers.

        Args:
            data: Bytes to convert to integer.

        Returns:
            int: Converted integer.
        """
        return int(data)


def count_calls(method: Callable) -> Callable:
    """
    Decorator for tracking the number of calls to Cache class methods
    """
    @wraps(method)
    def wrapper(self: Any, *args, **kwargs) -> str:
        """
        Wraps the called method, increments its call count in Redis,
        then executes it
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator for tracking arguments passed to Cache class methods
    """
    @wraps(method)
    def wrapper(self: Any, *args) -> str:
        """
        Wraps the called method, tracks its passed arguments by storing
        them in Redis
        """
        self._redis.rpush(f'{method.__qualname__}:inputs', str(args))
        output = method(self, *args)
        self._redis.rpush(f'{method.__qualname__}:outputs', output)
        return output
    return wrapper


def replay(fn: Callable) -> None:
    """
    Check Redis for the number of times a function was called and display:
            - The number of times it was called
            - Function arguments and output for each call
    """
    client = redis.Redis()
    calls = client.get(fn.__qualname__).decode('utf-8')
    inputs = [input.decode('utf-8') for input in
              client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
    outputs = [output.decode('utf-8') for output in
               client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
    print(f'{fn.__qualname__} was invoked {calls} times:')
    for input, output in zip(inputs, outputs):
        print(f'{fn.__qualname__}(*{input}) -> {output}')
