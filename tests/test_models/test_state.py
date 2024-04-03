#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class TestState(test_basemodel):
    """Represents the tests for the State model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests the type of name."""
        new = self.value(name="California")
        expected_type = str if new.name is not None else type(None)
        self.assertEqual(type(new.name), expected_type)
