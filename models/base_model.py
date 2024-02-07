#!/usr/bin/python3
"""This is the base model of the entire AirBnB clone web app"""
import uuid
import datetime
from datetime import datetime as dateTime


class BaseModel:
    """This class defines all common attributes \n
    and methods for other classes
    """

    def __init__(self, name="", my_number=0):
        """This runs anytime an object is instatntiated"""
        if((my_number) and (type(my_number) != int)):
            raise TypeError("number must be an integer")
        elif ((my_number) and (my_number < 0)):
            raise ValueError("number must be greater than 0")
        else:
            self.__my_number = my_number

        if((name) and type(name) != str):
            raise TypeError("name must be a string")
        else:
            self.__name = name

        self.__id = str(uuid.uuid4())
        self.__created_at = dateTime.now()
        slef.__updated_at = dateTime.now()

    @property
    def id(self):
        return self.__id

    @property
    def created_at(self):
        return self.__created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @property
    def name(self):
        """This is the getter of the name property"""
        return self.__name

    @name.setter
    def name(self, name_value):
        """This is the setter of the name porperty"""
        if ((name_value) and (type(name_value) != str)):
            raise TypeError("name must be a string")
        else:
            self.__name = name_value

    @property
    def my_number(self):
        """This is the getter of the name property"""
        return self.__my_number

    @my_number.setter
    def my_number(self, value_number):
        """This is the setter of the name porperty"""
        if ((value_number) and (type(value_number) != int)):
            raise TypeError("number must be an integer")
        elif ((value_number) and (value_number <= 0)):
            raise ValueError("number must be greater than 0")
        else:
            self.__my_number = value_number

    def save(self):
        """updates the updated_at with the current datetime"""
        self.__updated_at = dateTime.now()
