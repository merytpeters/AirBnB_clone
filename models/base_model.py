#!/usr/bin/python3
"""The start of the airbnb clone"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Class BaseModel that defines all common attributes/methods
       for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel class
        Conversion to ISO format
        """
        if len(kwargs):
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, iso_format)
                else:
                    self.__dict__[key] = value

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Converts to string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates to current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Creates a dictionary with attributes as key and
        its value as value"""
        dict_obj = self.__dict__.copy()
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        dict_obj["__class__"] = self.__class__.__name__

        return dict_obj
