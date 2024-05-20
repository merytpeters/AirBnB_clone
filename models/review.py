#!/usr/bin/python3
"""Class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inheritance of BaseModel"""
    place_id = ""
    user_id = ""
    text = ""
