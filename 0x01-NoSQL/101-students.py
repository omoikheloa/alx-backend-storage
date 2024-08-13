#!/usr/bin/env python3
""" Top students
"""


def top_students(mongo_collection):
    """ top students by avg score
    """
    return mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
