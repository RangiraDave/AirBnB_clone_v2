#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
<<<<<<< HEAD
=======
#  from .engine.file_storage import FileStorage
#  from .engine.db_storage import DBStorage
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560

classes = {"User": User, "BaseModel": BaseModel,
           "Place": Place, "State": State,
           "City": City, "Amenity": Amenity,
           "Review": Review}

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
<<<<<<< HEAD
    from models.engine.db_storage import DBStorage
=======
    from .engine.db_storage import DBStorage
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
    storage = DBStorage()
    storage.reload()
else:
<<<<<<< HEAD
    from models.engine.file_storage import FileStorage
=======
    from .engine.file_storage import FileStorage
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
    storage = FileStorage()
    storage.reload()
