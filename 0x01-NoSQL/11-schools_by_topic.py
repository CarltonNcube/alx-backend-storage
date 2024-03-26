#!/usr/bin/env python3
"""Defines function to return list of schools having a specific topic."""

import pymongo

def schools_by_topic(mongo_collection, topic):
    """Returns list of schools having a specific topic.

    Args:
    - mongo_collection: PyMongo collection object.
    - topic: Topic to search (string).

    Returns:
    - List of schools having the specified topic.
    """
    # Find documents in the collection with the specified topic
    schools = mongo_collection.find({"topics": topic})

    # Convert the cursor to a list of dictionaries
    school_list = list(schools)

    return school_list
