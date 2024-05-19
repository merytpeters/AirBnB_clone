#!/usr/bin/python3
"""File storage that serializes instances to a JSON file.
It also deserializes JSON file to instances.
"""

import json
from models.base_model import BaseModel
from datetime import datetime


class FileStorage:
    """performs serialization and deserialization"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialize the Filestorage instance."""
        self.classes = {
                'BaseModel': BaseModel
                }

    def all(self):
        """Returns the dictionary __objects"""

        return self.__objects

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id
        """
        key = f"{obj.__class__.name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        path: __file_path
        """
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserilalizes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    self.__objects[key] = self.classes[class_name](**value)
        except FileNotFoundError:
            pass
