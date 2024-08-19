"""Test file Module for file storage """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """Test that FileStorage works as required"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.storage._FileStorage__objects = {}

    def test_json_file_created(self):
        """Tests the json file is created"""
        file_path = self.storage._FileStorage__file_path
        self.assertIsNotNone(file_path)
        self.assertTrue(os.path.exists(file_path))
        self.assertEqual(self.storage._FileStorage__objects, {})

    """def test_obj_dict(self):
        Tests that test that __object dictionary is not empty
        new_object = BaseModel()
        self.storage.new(new_object)
        self.assertNotEqual(self.storage._FileStorage__objects, {})
        self.assertGreater(len(self.storage._FileStorage__objects), 0)
    """
