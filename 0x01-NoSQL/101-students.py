#!/usr/bin/env python3
"""Defines a function to return all students sorted by average score."""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    Args:
    - mongo_collection: A PyMongo collection object.

    Returns:
    - A list of students sorted and each item containing averageScore key.
    """
    pipeline = [
        {"$unwind": "$scores"},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": "$scores.score"}}},
        {"$sort": {"averageScore": -1}}
    ]
    students = mongo_collection.aggregate(pipeline)
    return list(students)
