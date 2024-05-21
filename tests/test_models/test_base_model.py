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
        self.model = BaseModel()

    def test_kwargs_attributes(self):
        """Checks for the correct time attributes and
        that they are datetime objects and also creates
        new instance attributes otherwise"""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_new_attributes(self):
        self.assertIsInstance(self.model.id, str)

    def test_id_unique(self):
        """Test that id is unique"""
        base1 = BaseModel()
        self.assertNotEqual(self.model.id, base1.id)

    def test_to_dict(self):
        """Test that Dictionary Works"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_recreation_from_dict(self):
        """Test that recreation of instance from dictionary Works"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model, BaseModel)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        datetime.fromisoformat(model_dict['created_at'])
        datetime.fromisoformat(model_dict['updated_at'])

    def test_save(self):
        """Test thst save method updated the time in updated_at"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
