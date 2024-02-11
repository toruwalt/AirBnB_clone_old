#!/usr/bin/python3
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """ Class for a state.

    Attributes:
        name (str): The Name of the State.
    """

    name = ""
