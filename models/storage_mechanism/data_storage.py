#!/usr/bin/python3
"""
Storage mechanism
"""
import json
import os
from models.base_model import BaseModel


class Storage:
    """
    Encapsulates the logic for saving and loading instances to and from a JSON file.
    """
    __users = {}
    __json_file = 'file.json'

    def base(self):
        """
        returns the dictinary a copy of __users dictionary
        """
        return Storage.__users

    def new(self,user):
        """
        sets in __instances the 'instance' with key '<instance classname>.id'
        """
        user_classname = user.__class__.__name__
        user_id = user.id
        Storage.__users[f"{user_classname}.{user_id}"] = user


    def save_to_file(self):
        """
        Saves the instance to a JSON file.
        we pass the instance itself as an argument to the save method.
        """
        data = Storage.__users
        filepath = Storage.__json_file
        for key, value in data.items():
            data[key] = value.to_dict()
        with open(filepath, 'w') as file:
            json.dump(data, file)

    def load_from_file(self):
        """
        Loads instances of the given class from a JSON file.
        """
        data = Storage.__users
        filepath = Storage.__json_file
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r') as file:
                    content = json.load(file)
                    for key, value in content.items():
                        if "BaseModel" in key:
                            data[key] = BaseModel(**value)
            except FileNotFoundError:
                pass  # File doesn't exist yet, return empty list
