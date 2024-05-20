#!/usr/bin/python3
""" initialization of modules."""

from models.engine import file_storage

storage = file_storage.FileStorage
print("FileStorage._FileStorage__file.path")

storage.reload()
