#!/usr/bin/python3
"""
Storage mechanism
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
        sets in __instances the 'instance' with key '<instance classname>.id'
        """
        u_classname = user.__class__.__name__
        u_id = user.id
        FileStorage.__users[f"{u_classname}.{u_id}"] = user

    def save(self):
        """
        Saves the instance to a JSON file.
        we pass the instance itself as an argument to the save method.
        """
        data = dict(FileStorage.__users)
        filepath = FileStorage.__json_file
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as file:
            json.dump(data, file)

    def reload(self):
        """
        Loads instances of the given class from a JSON file.
        """
        data = FileStorage.__users
        filepath = FileStorage.__json_file
        if os.path.exists(filepath):
            try:
                with open(filepath) as file:
                    content = json.load(file)
                    for key, value in content.items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
            except Exception:
                pass  # File doesn't exist yet, return empty list
