#!/usr/bin/python3
"""Initialize BaseModel and FileStorage"""
from models.base_model import BaseModel
from models.engine import file_storage


storage = FileStorage()
storage.reload()
