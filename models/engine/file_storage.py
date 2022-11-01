#!/usr/bin/python3
"""
Contains FileStorage class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


classes = {"BaseModel" : BaseModel, "User" : User, "State" : State,
           "City" : City, "Amenity" : Amenity, "Place" : Place,
           "Review" : Review}


class FileStorage:
    """serialization and deserialization"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serialize __objects to the JSON file"""
        json_obj = FileStorage.__objects
        json_objs = {obj: json_obj[obj].to_dict() for obj in json_obj.keys()}
        with open(self.__file_path, 'w') as f:
            json.dump(json_objs, f)

    def reload(self):
        """deserialize JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                new = json.load(f)
            for key in new:
                self.__objects[key] = classes[new[key]
                                              ["__class__"]](**new[key])
        except FileNotFoundError:
            return
