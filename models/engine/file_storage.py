#!/usr/bin/python3
"""
Contains FileStorage class
"""


import json
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}


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
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserialize JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                new = json.load(f)
            for key in new:
                self.__objects[key] = classe[new[key]["__class__"]](**new[key])
        except:
            pass
