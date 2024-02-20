#!/usr/bin/python3
"""
New engine DBStorage
"""

import os
#  import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from dotenv import load_dotenv
from models.base_model import Base, BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.review import Review


"""
Loading all files from environment (env)
"""
load_dotenv()


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

        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Function to return a dictionary
        """

        classes = ['User', 'State', 'City', 'Amenity', 'Place', 'Review']

        if cls is None:
            objs = []
            for table_cls in classes:
                objs.extend(self.__session.query(table_cls).all())
        else:
            if isinstance(cls, str):
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        dic = {"{}.{}".format(type(ob).__name__, ob.id): ob for ob in objs}

        return dic

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
                bind=self.__engine, expire_on_commit=True)
        Session = scoped_session(session_expire)
        self.__session = Session()
