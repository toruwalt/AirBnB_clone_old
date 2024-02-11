#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class for a review.

    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The Text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
