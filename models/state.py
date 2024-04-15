#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # for DBStorage
    # one to many
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
                                "City",
                                backref="state",
                                cascade="all, delete"
                                )
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City

            cities_of_state = []
            all_cities = storage.all(City)

            for obj in all_cities.values():
                if obj.state_id == self.id:
                    cities_of_state.append(obj)

            return cities_of_state
