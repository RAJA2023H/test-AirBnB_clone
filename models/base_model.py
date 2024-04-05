#!/usr/bin/python3
"""
class BaseModel
"""
import uuid
import datetime
from models.storage_mechanism.storage import Storage 

class BaseModel:
    """
    Class BaseModel that defines all common
    attributes/methods for other classes:
    """
    def __init__(self, id: str = None, created_at=None, updated_at=None):
        """ initializes the object's attributes when an object created """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        """ Returns a string representation of the object """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.datetime.utcnow()
        Storage.save_to_file(self)

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict  # dynamically generates the dictionary
