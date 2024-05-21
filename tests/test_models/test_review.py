"""Test Case For Review Inheritance of BaseModel"""
import unittest
from models.review import Review
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Class of TestReview To Test Inheritance Review"""

    def test_instance(self):
        """Test that Review is an instance"""
        review = Review()
        self.assertIsInstance(review, Review)

    def setUp(self):
        """Set up Review fixtures"""
        self.review = Review(place_id="", user_id="", text="")

    def test_inheritance(self):
        """Test that Review is an inheritance of BaseModel"""
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test attribute of State is empty"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")
