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
        self.assertEqual(
            type(new.city_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_user_id(self):
        """Tests the type of user_id."""
        new = self.value(user_id="test_user_id")
        self.assertEqual(
            type(new.user_id),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_name(self):
        """Tests the type of name."""
        new = self.value(name="test_name")
        self.assertEqual(
            type(new.name),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_description(self):
        """Tests the type of description."""
        new = self.value(description="test_description")
        self.assertEqual(
            type(new.description),
            str if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_rooms(self):
        """Tests the type of number_rooms."""
        new = self.value(number_rooms=5)
        self.assertEqual(
            type(new.number_rooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_number_bathrooms(self):
        """Tests the type of number_bathrooms."""
        new = self.value(number_bathrooms=3)
        self.assertEqual(
            type(new.number_bathrooms),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_max_guest(self):
        """Tests the type of max_guest."""
        new = self.value(max_guest=10)
        self.assertEqual(
            type(new.max_guest),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_price_by_night(self):
        """Tests the type of price_by_night."""
        new = self.value(price_by_night=100)
        self.assertEqual(
            type(new.price_by_night),
            int if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_latitude(self):
        """Tests the type of latitude."""
        new = self.value(latitude=37.7749)
        self.assertEqual(
            type(new.latitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_longitude(self):
        """Tests the type of longitude."""
        new = self.value(longitude=-122.4194)
        self.assertEqual(
            type(new.longitude),
            float if os.getenv('HBNB_TYPE_STORAGE') != 'db' else type(None)
        )

    def test_amenity_ids(self):
        """Tests the type of amenity_ids."""
        new = self.value(amenity_ids=['1', '2', '3'])
        self.assertEqual(
            type(new.amenity_ids),
            list
        )

if __name__ == '__main__':
    unittest.main()
