#!/usr/bin/python3
"""This script is the base model"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This represents the BaseModel of the hbnb project."""

    def __init__(self, *args, **kwargs):
        """Initializes instance attributes: new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): key-values pairs of attributes.
        """
        dtform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for ke, val in kwargs.items():
                if ke == "created_at" or ke == "updated_at":
                    self.__dict__[ke] = datetime.strptime(val, dtform)
                else:
                    self.__dict__[ke] = val
        else:
            models.storage.new(self)

    def save(self):
        """To update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing

	all keys-values of __dict__:the BaseModel instance.
        """
        rtdict = self.__dict__.copy()
        rtdict["created_at"] = self.created_at.isoformat()
        rtdict["updated_at"] = self.updated_at.isoformat()
        rtdict["__class__"] = self.__class__.__name__
        return rtdict

    def __str__(self):
        """returns the string representation of the BaseModel instance."""
        cl_name = self.__class__.__name__
        return "[{}] ({}) {}".format(cl_name, self.id, self.__dict__)
