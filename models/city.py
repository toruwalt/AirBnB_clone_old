#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for a City.

    Attributes:
        state_id (str): The State id.
        name (str): The name of the City.
    """

    state_id = ""
    name = ""
