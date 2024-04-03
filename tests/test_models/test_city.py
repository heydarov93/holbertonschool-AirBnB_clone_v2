#!/usr/bin/python3
""" """
import os

from models.city import City
from tests.test_models.test_base_model import test_basemodel


class TestCity(test_basemodel):
    """Represents the tests for the City model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """Tests the type of state_id."""
        new = self.value(state_id="test_city_id")
        expected_type = str if new.state_id is not None else type(None)
        self.assertEqual(type(new.state_id), expected_type)


    def test_name(self):
        """Tests the type of name."""
        new = self.value(name="Los Angeles")
        expected_type = str if new.name is not None else type(None)
        self.assertEqual(type(new.name), expected_type)

