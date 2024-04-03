#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class TestAmenity(test_basemodel):
    """Represents the tests for the Amenity model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests the type of name."""
        new = self.value(name="Test Amenity")
        expected_type = str if new.name is not None else type(None)
        self.assertEqual(type(new.name), expected_type)


