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
