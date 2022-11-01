#!/usr/bin/python3
"""
Contains BaseModels class
"""


import uuid
import models
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Represents a BaseModel of the AirBnB project
       Attributes:
    """
    def __init__(self, *args, **kwargs):
        """initializing of class BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at

    def __str__(self):
        """string representation of BaseModel"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """updates public instance attribute update_at with curr datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns dictionary containing all key/values"""
        dict_new = self.__dict__.copy()
        if "created_at" in dict_new:
            dict_new["created_at"] = dict_new["created_at"].strftime(time)

        if "updated_at" in dict_new:
            dict_new["updated_at"] = dict_new["updated_at"].strftime(time)

        dict_new["__class__"] = self.__class__.__name__
        return dict_new
        dict_new["__class__"] = self.__class__.__name__
        return dict_new
