#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inheritance of BaseModel"""
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
