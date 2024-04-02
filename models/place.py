#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []


    # for DBStorage
    # one to many
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
                                "Review",
                                backref="place",
                                cascade="all, delete"
                                )
    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review

            all_reviews = storage.all(Review)
            reviews_of_place = [v if v.place_id == self.id else "" for k, v
                               in all_reviews.items()]
            return reviews_of_place
