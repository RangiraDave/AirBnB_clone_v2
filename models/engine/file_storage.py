#!/usr/bin/python3
"""
This module defines a class to manage file storage for hbnb clone
"""

import json


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format
    """

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dictionary of models currently in storage
        """

        if cls is None:
            return self.__objects
        objs = self.__objects.items()
        return {k: v for k, v in objs if isinstance(v, cls)}

    def new(self, obj):
        """
        Adds new object to storage dictionary
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves storage dictionary to file
        """

        obj_dic = {obj: self.__objects[obj].to_dict(
            ) for obj in self.__objects.keys()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dic, f)

    def reload(self):
        """
        Loads storage dictionary from file
        """

        from models.base_model import BaseModel, Base
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.state import State
        from models.user import User


        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(name)(**obj))

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except json.JSONDecodeError as e:
            pass

    def delete(self, obj=None):
        """
        Function to delete object from __objects if it's inside.
        """

        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def reloader(self):
        """
        Function to call relaod
        """

        self.reload()
