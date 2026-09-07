#!/usr/bin/python3
"""Tests for the FileStorage class."""

import unittest
from models import storage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class."""

    def test_all(self):
        """Test that all returns a dictionary."""
        self.assertIsInstance(storage.all(), dict)

    def test_new(self):
        """Test adding an object to storage."""
        model = BaseModel()
        storage.new(model)

        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, storage.all())
        self.assertIs(storage.all()[key], model)

    def test_save_reload(self):
        """Test saving and reloading an object."""
        model = BaseModel()
        model.name = "Test"
        storage.new(model)
        storage.save()

        storage.reload()

        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, storage.all())


if __name__ == "__main__":
    unittest.main()
