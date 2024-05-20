#!/usr/bin/python3
""" Class that inherits from BaseModel"""
from model.base_model import BaseModel


class User(BaseModel):
    """ class User, aninheritance of BaseModel"""
    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
    super().__init__(*args, **kwargs)
