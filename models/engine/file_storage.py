#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""

import json
<<<<<<< HEAD
import models
=======
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560


class FileStorage:
    """
    Serializes instances to JSON file and deserializes to JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Return the dictionary
        """

        if not cls:
            return self.__objects
        else:
            new = {obj: key for obj, key in self.__objects.items()
                   if type(key) is cls}
            return new

    def new(self, obj):
        """
        Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        """

        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        """
        Serializes __objects attribute to JSON file.
        """

<<<<<<< HEAD
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()

        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)
=======
        obj_dic = {obj: self.__objects[obj].to_dict(
            ) for obj in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dic, f)
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """

        try:
<<<<<<< HEAD
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = models.classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
        except FileNotFoundError:
            pass
=======
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))

        except FileNotFoundError:
            pass
        except json.JSONDecodeError:
            pass
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it’s inside
        """

<<<<<<< HEAD
        FileStorage.__objects = {
            key: value for key,
            value in FileStorage.__objects.items() if value != obj}

    def close(self):
        self.reload()
=======
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]
>>>>>>> 48abb15b0ad04aafda82669c739f860618105560
