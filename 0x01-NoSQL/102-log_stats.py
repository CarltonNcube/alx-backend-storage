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

    total_logs = mongo_collection.count_documents({})
    stats['Total logs'] = total_logs

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {
        method: mongo_collection.count_documents({"method": method})
        for method in methods
    }
    stats['Methods'] = method_stats

    specific_log_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    stats['GET /status'] = specific_log_count

    top_ips_pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = mongo_collection.aggregate(top_ips_pipeline)
    top_ips_list = [entry['_id'] for entry in top_ips]
    stats['Top 10 IPs'] = top_ips_list

    return stats
