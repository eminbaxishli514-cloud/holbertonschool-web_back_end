#!/usr/bin/env python3
""" 10-update_topics """

def update_topics(mongo_collection, name, topics):
    """
    Update all documents in the collection with the given school name,
    setting their 'topics' field to the provided list.

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list of str): list of topics to set

    Returns:
        None
    """
    if mongo_collection is None or not name or not isinstance(topics, list):
        return

    mongo_collection.update_many(
        {"name": name},       # Filter: select documents by school name
        {"$set": {"topics": topics}}  # Update: set the 'topics' field
    )
