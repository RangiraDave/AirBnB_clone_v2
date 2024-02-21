#!/usr/bin/python3
"""
New engine DBStorage
"""

<<<<<<< HEAD
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
=======
import os
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
from models.place import Place
from models.review import Review
from models.state import State
<<<<<<< HEAD
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}

=======
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv



"""
Loading all files from environment (env)
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560

load_dotenv()
"""
class DBStorage:
    """
    Database storage class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Defines DBStorage class instances
        """

        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            os.getenv("HBNB_MYSQL_USER"), os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"), os.getenv("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
<<<<<<< HEAD
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)
=======

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560

    def all(self, cls=None):
        """
        Returns dictionary of all objects in the database
        """

<<<<<<< HEAD
        allobjs = {}
        if cls:
            allobjs = {obj.__class__.__name__ + "." + obj.id: obj for
                       obj in self.__session.query(classes[cls]).all()}
        else:
            for tbl in Base.__subclasses__():
                table = self.__session.query(tbl).all()
                for obj in table:
                    allobjs[obj.__class__.__name__ + "." + obj.id] = obj
        return allobjs
=======
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
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560

    def new(self, obj):
        """
        Adds new object to current session
        """

        if obj:
            self.__session.add(obj)

    def save(self):
        """
        Saves new object to the database
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes object in current session
        """

        self.__session.delete(obj)

    def reload(self):
        """
        Loads all objects from database and creates new session
        """

        Base.metadata.create_all(self.__engine)
<<<<<<< HEAD
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
=======
        session_expire = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_expire)
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
        self.__session = Session()

    def close(self):
        self.__session.close()
