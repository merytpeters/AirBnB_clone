"""Test Case For Amenity Inheritance of BaseModel"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Class of TestAmenity To Test Inheritance Amenity"""

    def test_instance(self):
        """Test that Amenity is an instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def setUp(self):
        """Set up Amenity fixtures"""
        self.amenity = Amenity(name="")

    def test_inheritance(self):
        """Test that Amenity is an inheritance of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test attribute of Amenity is empty"""
        self.assertEqual(self.amenity.name, "")
