#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
   """Represents a City of the AirBnB project
      Attributes:
         state_id (int): The State ID
         name (str): The name of the city
   """

   state_id = 0
   name = ""
