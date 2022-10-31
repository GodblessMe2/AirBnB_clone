#!/usr/bin/python3
"""Defines the user state"""
from models.base_model import BaseModel


class State(BaseModel):
   """Represents a State of the AirBnB project
   Attributes:
      name (str): The User name
   """

   name = ""
