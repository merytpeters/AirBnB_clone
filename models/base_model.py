#!/usr/bin/python3
"""The start of the airbnb clone"""


from uuid import uuid4
import datetime
class BaseModel:
    """Class BaseModel that defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = str(uuid4())  #instantiate all public instance attribute
        self.created_at = datetime.datetime.now().isoformat
        self.updated_at = datetime.datetime.now().isoformat  #Converts to ISO format also

    def __str__(self):
        return f"[{self.__class__.name}] ({self.id}) {self.dict}"  #Converts to string

    def save(self):
       return self.updated_at  #updates this public instance attribute with the current time

    def to_dict(self):
        return {key: value for key, value in self.__dict__.items()}
