#!/usr/bin/python3
"""Test console"""
import os
import uuid
import unittest
import models
from io import StringIO
from unittest.mock import patch
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittesting the HBNB command interpreter"""

    @classmethod
    def setUpClass(test_cls):
        try:
            os.rename("file.json", "tmp_file")
        except IOError:
            pass
        test_cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(test_cls):
        try:
            os.rename("tmp_file", "file.json")
        except IOError:
            pass
        del test_cls.HBNB
        if isinstance(models.storage, DBStorage):
            models.storage._DBStorage__session.close()

    def setUp(self):
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    @unittest.skipIf(
            isinstance(models.storage, DBStorage), "Testing DBstorage")
    def test_create(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create BaseModel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("create Amenity")
            new_amenity = test.getvalue().strip()

    @unittest.skipIf(
            isinstance(models.storage, DBStorage), "Testing DBStorage")
    def test_all(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all BaseModel")
            new_bm = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all State")
            new_state = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all User")
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all City")
            new_city = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Place")
            new_place = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Review")
            new_review = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all Amenity")
            new_amenity = test.getvalue().strip()

    @unittest.skipIf(
            isinstance(models.storage, DBStorage), "Testing DBstorage")
    def test_create_kwargs(self):
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd('create User first_name="John" '
                             'email="john@example.com '
                             'password="1234"')
            new_user = test.getvalue().strip()
        with patch("sys.stdout", new=StringIO()) as test:
            self.HBNB.onecmd("all User")
            user_output = test.getvalue()
            self.assertIn(new_user, user_output)
            self.assertIn("'first_name': 'John'", user_output)
            self.assertIn("'email': 'john@example.com'", user_output)
            self.assertNotIn("'last_name': 'Snow'", user_output)
            self.assertIn("'password': '1234'", user_output)


class TestBaseModel(unittest.TestCase):
    """Unittesting the BaseModel class"""

    def test_kwargs_one(self):
        # Test scenario: Passing unexpected kwargs should raise KeyError
        with self.assertRaises(KeyError):
            # Passing unexpected key 'unexpected_key' to BaseModel
            new_instance = BaseModel(unexpected_key="unexpected_value")


if __name__ == '__main__':
    unittest.main()
