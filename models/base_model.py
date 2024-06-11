#!/usr/bin/python3
"""
class BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Class BaseModel that defines all common
    attributes/methods for other classes:
    """


    def __init__(self, *args, **kwargs) -> None:
        """ initializes the object's attributes when an object created """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key,value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    self.__dict__[key] = value
        else:
            models.storage.new(self)


    def __str__(self) -> str:
        """ Returns a string representation of the object """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)


    def save(self) -> None:
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()


    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        if not isinstance(dictionary["created_at"], str):
            dictionary["created_at"] = dictionary["created_at"].isoformat()
        if not isinstance(dictionary["updated_at"], str):
            dictionary["updated_at"] = dictionary["updated_at"].isoformat()
        return dictionary
