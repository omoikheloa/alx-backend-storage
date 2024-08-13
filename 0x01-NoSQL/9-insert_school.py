#!/usr/bin/env python3
""" Inserts a document in Python
"""


def insert_school(mongo_collection, **kwargs):
    """ inserts school
    """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
