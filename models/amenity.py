#!/usr/bin/python3
"""Defines the Amenity Class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for amenity.

    Attributes:
        name (str): The Name of the amenity.
    """

    name = ""
