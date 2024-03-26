#!/usr/bin/env python3
"""Defines function to insert document in MongoDB collection based on kwargs."""

import pymongo

def insert_school(mongo_collection, **kwargs):
    """Inserts new document into given MongoDB collection using keyword arg.

    Args:
    - mongo_collection: PyMongo collection object.
    - **kwargs: Fields and values for new document.

    Returns:
    - New _id of inserted document.
    """
    # Insert document into collection and return _id
    return mongo_collection.insert_one(kwargs).inserted_id
