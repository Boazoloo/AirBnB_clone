#!/usr/bin/python3
"""Tests for the Place class."""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class."""

    def test_create_instance(self):
        """Test creating a Place instance."""
        place = Place()

        self.assertIsInstance(place, Place)
        self.assertIsInstance(place.id, str)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
