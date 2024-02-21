#!/usr/bin/python3
"""
Review module for the HBNB project
"""

<<<<<<< HEAD
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base


class Review(BaseModel, Base):
    """
    Implementation for the Review.
    """

    __tablename__ = "reviews"

=======
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """

    __tablename__ = 'reviews'
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
