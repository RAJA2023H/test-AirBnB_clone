#!/usr/bin/python3
"""
FileStorage
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """
    Encapsulates the logic for saving and loading instances to and from a JSON file.
    """
    __users = {}
    __json_file = 'file.json'

    def all(self):
        """
        returns the dictinary of __users dictionary
        """
        return FileStorage.__users

    def new(self,user):
        """
        sets in __users the 'instance' with key '<user classname>.id'
        """
        classname = user.to_dict()["__class__"]
        id = user.to_dict()["id"]
        keyname = classname+"."+id
        FileStorage.__users[keyname] = user

    def save(self):
        """
        Saves the user to a JSON file.
        we pass the user itself as an argument to the save method.
        """
        filepath = FileStorage.__json_file
        data = dict(FileStorage.__users)
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """
        Loads user of the given class from a JSON file.
        """
        data = FileStorage.__users
        filepath = FileStorage.__json_file
        if os.path.exists(filepath):
            try:
                with open(filepath) as file:
                    content = json.load(file).items()
                    for key, value in content:
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
            except Exception:
                pass  # File doesn't exist yet, return empty list
