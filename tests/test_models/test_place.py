"""Test Case For Place Inheritance of BaseModel"""
import unittest
from models.place import Place
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Class of TestPlace To Test Place"""

    def test_instance(self):
        """Test that Place is an instance"""
        place = Place()
        self.assertIsInstance(place, Place)

    def setUp(self):
        """Set up Place Test fixtures"""
        self.place = Place(city_id="", user_id="", name="", description="",
                           number_rooms=0, max_guest=0, number_bathrooms=0,
                           price_by_night=0, latitude=0.0, longitude=0.0,
                           amenity_id=[""])

    def test_inheritance(self):
        """Test that Place is an inheritance of BaseModel"""
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test attributes of Place are correct"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_id, [""])
