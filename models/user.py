#!/usr/bin/python3
""" Class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class User, aninheritance of BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
