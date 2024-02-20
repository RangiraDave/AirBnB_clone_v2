#!/usr/bin/python3
"""
State Module for HBNB project
"""

from os import getenv
from models.base_model import BaseModel, Base
#  from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

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
