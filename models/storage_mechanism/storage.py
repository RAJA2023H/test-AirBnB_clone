#!/usr/bin/python3
"""
Storage mechanism
"""
import json


class Storage:
    """
    Encapsulates the logic for saving and loading instances to and from a JSON file.
    """
    @staticmethod
    def save_to_file(instance):
        """
        Saves the instance to a JSON file.
        we pass the instance itself as an argument to the save method.
        """
        serialized_data = instance.to_dict()
        with open('storage.json', 'a') as file:
            json.dump(serialized_data, file)
            file.write('\n')

    @staticmethod
    def load_from_file(cls):
        """
        Loads instances of the given class from a JSON file.
        """
        instances = []
        try:
            with open('storage.json', 'r') as file:
                for line in file:
                    data = json.loads(line)
                    if data['__class__'] == cls.__name__:
                        instance = cls(**data)
                        instances.append(instance)
        except FileNotFoundError:
            pass  # File doesn't exist yet, return empty list
        return instances
