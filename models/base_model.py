#!/usr/bin/python3
"""
class BaseModel
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    Class BaseModel that defines all common
    attributes/methods for other classes:
    """


    def __init__(self):
        """ initializes the object's attributes when an object created """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


    def __str__(self):
        """ Returns a string representation of the object """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary
