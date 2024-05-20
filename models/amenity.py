#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Inheritance of BaseModel"""
    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(*args, **kwargs)
