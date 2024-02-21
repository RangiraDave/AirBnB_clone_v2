#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity
import os


class Amenity(BaseModel, Base):
    """
    Implementation for the Amenities.
    """

    __tablename__ = "amenities"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities")
    else:
        name = ""
=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class Amenity(BaseModel, Base):
    """
    Definition of Amenity class
    """

    __tablename__ = 'amenities'
    name = Column(String)
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
