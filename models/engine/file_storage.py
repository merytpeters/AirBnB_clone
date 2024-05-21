#!/usr/bin/python3
"""File storage that serializes instances to a JSON file.
It also deserializes JSON file to instances.
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from datetime import datetime


class FileStorage:
    """performs serialization and deserialization"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        if not os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'w') as f:
                f.write('{}')

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj
        with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file
        path: __file_path
        """
        obj_dict = {
            key: obj.to_dict()
            for key, obj in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserilalizes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)

                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    classes = globals().get(class_name)
                    # del key["__class__"]
                    # self.new(eval(class_name)(**key))
                    if classes:
                        self.new(classes(**value))
        except FileNotFoundError:
            pass
