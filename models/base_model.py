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
    def __init__(self, *args, **kwargs) -> None:
        """ initializes the object's attributes when an object created """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    self.__dict__[key] = value
        else:
            from models import storage
            storage.new(self)

    def __str__(self) -> str:
        """ Returns a string representation of the object """
        
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = {}
        obj_dict.update(self.__dict__)
        obj_dict.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
