#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class TestReview(test_basemodel):
    """Represents the tests for the Review model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """Tests the type of place_id."""
        new = self.value(place_id="test_place_id")
        self.assertEqual(
            type(new.place_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """Tests the type of user_id."""
        new = self.value(user_id="test_user_id")
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_text(self):
        """Tests the type of text."""
        new = self.value(text="This is a review text")
        self.assertEqual(
            type(new.text),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

