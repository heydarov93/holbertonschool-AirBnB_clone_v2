#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
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


    place_amenity = Table("place_amenity", Base.metadata,
                          Column(
                                 "place_id",
                                 String(60),
                                 ForeignKey("places.id")
                                 primary_key=True,
                                 nullable=False
                                 ),
                          Column(
                                 "amenity_id",
                                 String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True,
                                 nullable=False
                                 ))


    # for DBStorage
    # one to many
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
                                "Review",
                                backref="place",
                                cascade="all, delete"
                                )
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            from models import storage
            from models.review import Review

            all_reviews = storage.all(Review)
            reviews_of_place = [v if v.place_id == self.id else "" for k, v
                               in all_reviews.items()]
            return reviews_of_place

        @property
        def amenities(self):
            """
            returns the list of Amenity instances based on the
            attribute amenity_ids that contains all Amenity.id
            linked to the Place
            """
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None)
        """
        Setter attribute amenities that handles append method for
        adding an Amenity.id to the attribute amenity_ids
        """
        from models.amenity import Amenity
        if type(obj) is Amenity and obj.id not in self.amenity_id:
            self.amenity_ids.append(obj.id)
















