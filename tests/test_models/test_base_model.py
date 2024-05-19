#!/usr/bin/python3
"""Test file module for base model"""
import os
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.BaseModel):
    """Checks that BaseModel work as required"""


    def setUp(self):
        self.instance = BaseModel  
