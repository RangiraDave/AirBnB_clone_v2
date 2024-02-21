#!/usr/bin/python3
<<<<<<< HEAD
"""
Implementation of the User class which inherits from BaseModel
"""

from models.base_model import BaseModel, Base
=======
'''
    Implementation of the User class which inherits from BaseModel
'''

from models.base_model import Base, BaseModel
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
<<<<<<< HEAD
    """
    Definition of the User class
    """
=======
    '''
        Definition of the User class
    '''
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560

    __tablename__ = "users"

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship('Place', backref='user',
            cascade='delete')
    reviews = relationship('Review', backref='user',
            cascade='delete')
