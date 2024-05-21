"""Test Case For City Inheritance of BaseModel"""
import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Class of TestUser To Test City"""

    def test_instance(self):
        """Test that City is an instance"""
        city = City()
        self.assertIsInstance(city, City)

    def setUp(self):
        """Set up City Test fixtures"""
        self.city = City(state_id="", name="")

    def test_inheritance(self):
        """Test that User is an inheritance of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test attributes of User are empty"""
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")
