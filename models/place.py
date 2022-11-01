#!/usr/bin/python3
"""Defines the user Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Place of the AirBnB project
    Attributes:
      user_id (str): The User ID
      city_id (str): The City ID
      name (str): The name of the place(Location)
      description (str): The User ID
      number_rooms (int): The number rooms in the location default: 0
      number_bathrooms (int): The number bathrooms in the location default: 0
      max_guest (int): The number of guest that can use the room
      price_by_night (int): The price of the room default: 0
      latitude (float): The latitude of the place
      longitude (float): The longitude of the place
      place_amenity_id (string): The Amenity ID
    """

    user_id = ""
    city_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    place_amenity_id = ""
