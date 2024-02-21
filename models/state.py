#!/usr/bin/python3
"""
State Module for HBNB project
"""

<<<<<<< HEAD
from sqlalchemy import Column, Integer, String
from models.base_model import BaseModel, Base
=======
from os import getenv
from models.base_model import BaseModel, Base
#  from models.city import City
from sqlalchemy import Column, String
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
from sqlalchemy.orm import relationship
import os
import models


class State(BaseModel, Base):
    """
    Implementation for the State.
    """

<<<<<<< HEAD
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            FLcity = models.storage.all(models.classes['City']).values()

            return [city for city in FLcity if city.state_id == self.id]
=======
    #  cities = relationship('City', backref='state', cascade='all, delete')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """
            Function to get list of all related City objects.
            """
            from models.city import City

            citys = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    citys.append(city)
            return citys

    cities = relationship('City', backref='state', cascade='delete')
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
