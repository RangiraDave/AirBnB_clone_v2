#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
import models
#  from models import storage

#  import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class BaseModel:
    """A definition of the base class for all hbnb models"""

    id = Column(String(60),
            primary_key=True,
            nullable=False)
    created_at = Column(DateTime,
            nullable=False,
            default=datetime.utcnow)
    updated_at = Column(DateTime,
            nullable=False,
            default=datetime.utcnow,
            onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self,key, value)

#        else:  # kwargs managed here to create instance
#            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
#                                                     '%Y-%m-%dT%H:%M:%S.%f')
#            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
#                                                     '%Y-%m-%dT%H:%M:%S.%f')
#            del kwargs['__class__']
#           self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)  # Moved from __init__
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """
        Function to delete the current instance
        """

        models.storage.delete(self)
