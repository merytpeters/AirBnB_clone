"""Test Case For User Inheritance of BaseModel"""
import unittest
from models.user import User
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Class of TestUser To Test User"""

    def test_instance(self):
        """Test that User is an instance"""
        user = User()
        self.assertIsInstance(user, User)

    def setUp(self):
        """Set up User Test fixtures"""
        self.user = User(email="", password="", first_name="", last_name="")

    def test_inheritance(self):
        """Test that User is an inheritance of BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test attributes of User are empty"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")
