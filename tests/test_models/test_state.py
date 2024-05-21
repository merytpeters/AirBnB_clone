"""Test Case For State Inheritance of BaseModel"""
import unittest
from models.state import State
from datetime import datetime
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Class of TestState To Test Inheritance State"""

    def test_instance(self):
        """Test that State is an instance"""
        state = State()
        self.assertIsInstance(state, State)

    def setUp(self):
        """Set up State fixtures"""
        self.state = State(name="")

    def test_inheritance(self):
        """Test that State is an inheritance of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test attribute of State is empty"""
        self.assertEqual(self.state.name, "")
