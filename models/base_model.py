#!/usr/bin/python3
"""The start of the airbnb clone"""
from uuid import uuid4
import datetime


class BaseModel:
    """Class BaseModel that defines all common attributes/methods
       for other classes"""
    def __init__(self, *args, **kwargs):
        """Initialization of the BaseModel class
        Conversion to ISO format
        """
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """Converts to string"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates to current time"""
        return self.updated_at

    def to_dict(self):
        """Creates a dictionary with attributes as key and
        its value as value"""
        return {key: value for key, value in self.__dict__.items()}
        holder = self.__dict__.copy
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == created_at or key == updated_at:
                    holder[key] = datetime.datetime.fromisoformat(value)
            return holder
