#!/usr/bin/env python3
"""Defines function to update topics of a school document based on name."""

import pymongo

def update_topics(mongo_collection, name, topics):
    """Updates topics of a school document based on the school's name.

    Args:
    - mongo_collection: PyMongo collection object.
    - name: Name of the school to update (string).
    - topics: List of topics approached in the school.

    Returns:
    - Number of documents updated.
    """
    # Update documents in the collection
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
