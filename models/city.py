#!/usr/bin/python3
""" City Module for HBNB project """

<<<<<<< HEAD
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
=======
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560


class City(BaseModel, Base):
    """
    Define the class City that inherits from BaseModel.
    """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
<<<<<<< HEAD
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
=======

    places = relationship('Place', backref='cities', cascade='delete')
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
