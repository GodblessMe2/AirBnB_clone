#!/usr/bin/python3
"""Defines the User details"""
from models.base_model import BaseModel

class User(BaseModel):
   """Represents a User of the AirBnB project
   Attributes:
      email (str): The User email
      first_name (str): The User First name
      last_name (str): The User Last name
      password (str): The User Password
   """

   first_name = ""
   last_name = ""
   email = ""
   password = ""
   