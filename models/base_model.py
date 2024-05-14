#!/usr/bin/python3
"""The start of the airbnb clone"""


from uuid import uuid4
from datetime import datetime
class BaseModel:
    """Class BaseModel that defines all common attributes/methods for other classes"""

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"{self.__class__.name} {self.id} {self.dict}"

    def save(self):
       self.updated_at = datetime.now()
       str(self.created_at)

Base1 = BaseModel()
Base2 = BaseModel()

print(Base1.id)
print(Base2.id)
