#!/usr/bin/python3
"""Test file module for base model"""
from models.base_model import BaseModel
import os
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Checks that BaseModel work as required"""

    def setUp(self):
        """Checks the class exists"""
        self.instance = BaseModel()

    def test_kwargs_attributes(self):
        """Checks for the correct time attributes and
        that they are datetime objects and also creates
        new instance attributes otherwise"""
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_new_attributes(self):
        self.assertIsInstance(self.instance.id)

    def test_id_unique(self):
        """Test that id is unique"""
        base1 = BaseModel()
        self.assertIsNotEqual(self.instance.id, base1.id)


if __name__ == '__main__':
    unittest.main()
