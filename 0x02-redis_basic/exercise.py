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
        Initializes the Cache object with a Redis client and flushes the
        database.
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
        Retrieves data from Redis using the provided key and optionally applies
        a conversion function.

        Args:
            key: The key used to retrieve the data from Redis.
            fn: Optional conversion function to be applied to the retrieved data.

        Returns:
            Any: The retrieved data, optionally converted based on the provided
            function.
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

    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count the number of times a method is called.
        
        Args:
            method: The method to be decorated.
        
        Returns:
            Callable: Decorated method.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            Wraps the called method and increments the call count in Redis
            before execution.
            """
            self._redis.incr(method.__qualname__)
            return method(self, *args, **kwargs)
        return wrapper

    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a particular
        function.
        
        Args:
            method: The method to be decorated.
        
        Returns:
            Callable: Decorated method.
        """
        @wraps(method)
        def wrapper(self, *args, **kwargs):
            """
            Wraps the called method and tracks its passed arguments by storing
            them in Redis.
            """
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"

            self._redis.rpush(inputs_key, str(args))
            output = method(self, *args, **kwargs)
            self._redis.rpush(outputs_key, output)

            return output
        return wrapper

    def replay(fn: Callable) -> None:
        """
        Check Redis for how many times a function was called and display:
            - How many times it was called
            - Function args and output for each call
        """
        client = redis.Redis()
        calls = client.get(fn.__qualname__).decode('utf-8')
        inputs = [input.decode('utf-8') for input in 
                client.lrange(f'{fn.__qualname__}:inputs', 0, -1)]
        outputs = [output.decode('utf-8') for output in 
                client.lrange(f'{fn.__qualname__}:outputs', 0, -1)]
        print(f'{fn.__qualname__} was called {calls} times:')
        for input, output in zip(inputs, outputs):
            print(f'{fn.__qualname__}(*{input}) -> {output}')

