#!/usr/bin/python3
"""Tests for the City class."""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class."""

    def test_create_instance(self):
        """Test creating a City instance."""
        city = City()

        self.assertIsInstance(city, City)
        self.assertIsInstance(city.id, str)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
