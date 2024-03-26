#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB."""
from pymongo import MongoClient

def get_logs_stats(mongo_collection):
    """
    Retrieves statistics about Nginx logs stored in the MongoDB collection.

    Args:
    - mongo_collection: PyMongo collection object.

    Returns:
    - Dictionary containing statistics.
    """
    stats = {}

    # Total number of logs
    total_logs = mongo_collection.count_documents({})
    stats['Total logs'] = total_logs

    # Methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {
        method: mongo_collection.count_documents({"method": method})
        for method in methods
    }
    stats['Methods'] = method_stats

    # Specific method and path
    specific_log_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    stats['GET /status'] = specific_log_count

    return stats

if __name__ == "__main__":
    """Provides some stats about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    stats = get_logs_stats(nginx_collection)

    print("Statistics:")
    for key, value in stats.items():
        if isinstance(value, dict):
            print(f"\t{key}:")
            for method, count in value.items():
                print(f"\t\t{method}: {count}")
        else:
            print(f"\t{key}: {value}")

