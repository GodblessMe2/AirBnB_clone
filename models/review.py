#!/usr/bin/python3
"""Defines the user Review"""
from models.base_model import BaseModel


class Review(BaseModel):
   """Represents a Review of the AirBnB project
      Attributes:
         user_id (str): The User ID
         place_id (str): The Place ID
         text (str): The text review after using the service
   """

   user_id = 0
   place_id = 0
   text = ""
