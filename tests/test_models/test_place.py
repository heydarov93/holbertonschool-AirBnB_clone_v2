#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class TestPlace(test_basemodel):
    """Represents the tests for the Place model."""
    def __init__(self, *args, **kwargs):
        """Initializes the test class."""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """Tests the type of city_id."""
        new = self.value(city_id="test_city_id")
        expected_type = str if new.city_id is not None else type(None)
        self.assertEqual(type(new.city_id), expected_type)

    def test_user_id(self):
        """Tests the type of user_id."""
        new = self.value(user_id="test_user_id")
        expected_type = str if new.user_id is not None else type(None)
        self.assertEqual(type(new.user_id), expected_type)

    def test_name(self):
        """Tests the type of name."""
        new = self.value(name="test_name")
        expected_type = str if new.name is not None else type(None)
        self.assertEqual(type(new.name), expected_type)

    def test_description(self):
        """Tests the type of description."""
        new = self.value(description="test_description")
        expected_type = str if new.description is not None else type(None)
        self.assertEqual(type(new.description), expected_type)

    def test_number_rooms(self):
        """Tests the type of number_rooms."""
        new = self.value(number_rooms=5)
        expected_type = int if new.number_rooms is not None else type(None)
        self.assertEqual(type(new.number_rooms), expected_type)

    def test_number_bathrooms(self):
        """Tests the type of number_bathrooms."""
        new = self.value(number_bathrooms=3)
        expected_type = int if new.number_bathrooms is not None else type(None)
        self.assertEqual(type(new.number_bathrooms), expected_type)

    def test_max_guest(self):
        """Tests the type of max_guest."""
        new = self.value(max_guest=10)
        expected_type = int if new.max_guest is not None else type(None)
        self.assertEqual(type(new.max_guest), expected_type)

    def test_price_by_night(self):
        """Tests the type of price_by_night."""
        new = self.value(price_by_night=100)
        expected_type = int if new.price_by_night is not None else type(None)
        self.assertEqual(type(new.price_by_night), expected_type)

    def test_latitude(self):
        """Tests the type of latitude."""
        new = self.value(latitude=37.7749)
        expected_type = float if new.latitude is not None else type(None)
        self.assertEqual(type(new.latitude), expected_type)

    def test_longitude(self):
        """Tests the type of longitude."""
        new = self.value(longitude=-122.4194)
        expected_type = float if new.longitude is not None else type(None)
        self.assertEqual(type(new.longitude), expected_type)

    def test_amenity_ids(self):
        """Tests the type of amenity_ids."""
        new = self.value(amenity_ids=['1', '2', '3'])
        self.assertEqual(
            type(new.amenity_ids),
            list
        )

if __name__ == '__main__':
    unittest.main()
