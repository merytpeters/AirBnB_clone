#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Inheritance of BaseModel"""
    state_id = ""
    name = ""
