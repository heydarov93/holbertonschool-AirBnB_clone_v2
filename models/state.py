#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ

Base = declarative_base()


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # for DBStorage
    # one to many
    if environ("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
                                "City",
                                back_populates="states",
                                cascade="all, delete"
                                )
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City

            all_cities = istorage.all(City)
            cities_of_state = [v if v.state_id == self.id for k, v
                               in all_cities.items()]
            return cities_of_state
