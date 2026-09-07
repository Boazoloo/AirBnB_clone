#!/usr/bin/python3
"""Tests for the User class."""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class."""

    def test_create_instance(self):
        """Test creating a User instance."""
        user = User()

        self.assertIsInstance(user, User)
        self.assertIsInstance(user.id, str)
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        from models.base_model import BaseModel

        self.assertIsInstance(User(), BaseModel)


if __name__ == "__main__":
    unittest.main()
