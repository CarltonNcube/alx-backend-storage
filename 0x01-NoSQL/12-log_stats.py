#!/usr/bin/env python3
"""
Python script that provides stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient

def print_stats(collection):
    """
    Prints stats about Nginx logs.
    """
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = collection.count_documents({
        "method": "GET",
        "path": "/status"
    })
    print(f"\tmethod=GET path=/status: {status_count}")

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db.nginx
    print_stats(collection)
