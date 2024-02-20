#!/usr/bin/python3
"""
New engine DBStorage
"""

import os
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv



"""
Loading all files from environment (env)

load_dotenv()
"""
class DBStorage:
    """
    The database class definition
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        The storage engine class constructor.
        """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Function to return a dictionary
        """

        if cls is None:
            obj = self.__session.query(State).all()
            obj.extend(self.__session.query(City).all())
            obj.extend(self.__session.query(User).all())
            obj.extend(self.__session.query(Place).all())
            obj.extend(self.__session.query(Review).all())
            obj.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            obj = self.__session.query(cls)
        return {"{}.{}".format(type(i).__name__, i.id): i for i in obj}

    def new(self, obj):
        """
        Function to add object in session if not there.
        """

        if obj not in self.__session:
            self.__session.add(obj)

    def save(self):
        """
        Function to commit all changes that are in session.
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Function to delete obj in the current session if exists.
        """

        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Function to create all tables in the db and the current
        database session form the engine
        """

        Base.metadata.create_all(self.__engine)
        session_expire = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_expire)
        self.__session = Session()
