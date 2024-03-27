Project 0x02: Redis Basics


This project is designed to enhance your understanding and proficiency in working with Redis, a powerful in-memory data structure store, and its Python client library, redis-py. Below, you will find detailed explanations of each task along with the resources and requirements for completing them.


Overview

Redis is an open-source, in-memory data structure store that can be used as a database, cache, and message broker. It supports various data structures such as strings, lists, sets, sorted sets, hashes, bitmaps, and more. Redis provides high performance, high availability, and easy scalability, making it a popular choice for building real-time applications, caching systems, and message queues.
Learning Objectives



Resources

Before starting the project, you may find the following resources helpful:

    Redis Crash Course Tutorial: A comprehensive tutorial covering the basics of Redis.
    Redis Commands: Official documentation providing a complete list of Redis commands and their usage.
    Redis Python Client Documentation: Documentation for redis-py, the Python client library for Redis.
    How to Use Redis With Python: A tutorial on integrating Redis with Python applications.

Installation

To install Redis on Ubuntu 18.04, run the following commands:

bash

 sudo apt-get -y install redis-server
 pip3 install redis
 sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf


Tasks

  1   Writing strings to Redis: Create a Cache class to store and retrieve strings in Redis.

    Description: Implement a Cache class with methods to store and retrieve strings in Redis. The class should establish a connection to the Redis 
    server and provide methods for setting and getting string values.

    Details: The Cache class should use the redis-py library to establish a connection to the Redis server. It should provide methods like 
    set_string to store a string value and get_string to retrieve a string value.

  2  Reading from Redis and recovering original type: Implement methods to retrieve data from Redis and convert it to the original type.

    Description: Develop methods to retrieve data from Redis and convert it to the original Python data type. This task involves handling different     data types stored in Redis and ensuring that the retrieved data matches the original type.

    Details: The methods should handle conversions for various data types such as strings, integers, floats, and lists. They should retrieve data 
    from Redis and convert it back to the original Python data type using appropriate conversion functions.

 3  Incrementing values: Implement a decorator to count method calls and increment values in Redis.

    Description: Create a decorator to count the number of times a method is called and increment values in Redis based on method calls. This task 
    requires understanding how decorators work in Python and how to interact with Redis using redis-py.

    Details: The decorator should wrap methods of a class and count the number of times each method is called. It should increment values in Redis      corresponding to the method names and maintain a count of method calls.

 4  Storing lists: Implement a decorator to store the history of inputs and outputs for a function.

    Description: Develop a decorator to store the history of inputs and outputs for a function in Redis. This task involves tracking function calls     and their corresponding inputs and outputs to provide a history of function execution.

    Details: The decorator should wrap functions and store the input parameters and return values in Redis. It should maintain separate lists for in    put and output data associated with each function.

5    Retrieving lists: Develop a function to replay the history of calls for a specific function.

    Description: Write a function to retrieve and replay the history of calls for a specific function stored in Redis. This task requires fetching 
    stored function call data from Redis and replaying the function calls with their original inputs.

    Details: The function should retrieve stored input and output data for a specific function from Redis and replay the function calls with their 
    original inputs. It should provide a mechanism to replay function calls in the same order as they were originally executed.

 6   Implementing an expiring web cache and tracker: Create a function to cache web pages with an expiration time and track URL accesses.

    Description: Implement a function to cache web pages with an expiration time in Redis. Additionally, track URL accesses by counting the number 
    of times each URL is accessed. This task involves setting expiration times for cached web pages and updating access counts for URLs.

    Details: The function should cache web pages retrieved from URLs with an expiration time specified in seconds. 
    It should track the number of times each URL is accessed and update access counts in Redis accordingly.
