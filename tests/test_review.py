#!/usr/bin/python3
"""Tests for the Review class."""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class."""

    def test_create_instance(self):
        """Test creating a Review instance."""
        review = Review()

        self.assertIsInstance(review, Review)
        self.assertIsInstance(review.id, str)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
