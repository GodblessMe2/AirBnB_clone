#!/usr/bin/python3
"""Defines the user Amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents a Amenity of the AirBnB project
      Attributes:
         name (str): The name of the Amenity
         amenity_place_id (string): The Place ID
   """
    name = ""
    amenity_place_id = ""
