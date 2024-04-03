#!/usr/bin/python3
""" """
import os
from sqlalchemy import Column

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class TestUser(test_basemodel):
    """Represents the tests for the User model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """Tests the type of first_name."""
        new = self.value(first_name="John")
        expected_type = str if new.first_name is not None else type(None)
        self.assertEqual(type(new.first_name), expected_type)

    def test_last_name(self):
        """Tests the type of last_name."""
        new = self.value(last_name="Doe")
        expected_type = str if new.last_name is not None else type(None)
        self.assertEqual(type(new.last_name), expected_type)

    def test_email(self):
        """Tests the type of email."""
        new = self.value(email="john.doe@example.com")
        expected_type = str if new.email is not None else type(None)
        self.assertEqual(type(new.email), expected_type)

    def test_password(self):
        """Tests the type of password."""
        new = self.value(password="password123")
        expected_type = str if new.password is not None else type(None)
        self.assertEqual(type(new.password), expected_type)
