#!/usr/bin/python3
"""
State Module for HBNB project
"""

import os
from models.base_model import BaseModel, Base
#  from models.storage import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state', cascade='all, delete')

    if os.getenv("HBNB_TYPE_STORAGE") != "db":

            @property
            def cities(self):
                """
                Function to get list of all related City objects.
                """

                city_list = []
                for city in list(models.storage.all(City).values()):
                    if city.state_id == self.id:
                        city_list.append(city)
                return city_list
