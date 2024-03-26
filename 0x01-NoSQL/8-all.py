#!/usr/bin/env python3
"""
Defines a function to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in the given MongoDB collection.

    Args:
    - mongo_collection: A PyMongo collection object.

    Returns:
    - A list containing all documents in the collection.
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
