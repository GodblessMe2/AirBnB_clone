#!/usr/bin/python3
"""Contains tests for the City Class"""

import unittest
import models
import time 
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
import inspect
module_doc = models.city.__doc__


class TestCityDoc(unittest.TestCase):
    """To check doxumentation"""
    @classmethod
    def setUpClass(self):
        """docstring test"""
        cls.city_funcs = inspect.getmembers(City, inspect.isfunction)

    def test_module_docstring(self):
        """test for module docstring"""
        self.assertIsNot(module_doc, None, "city.py needs a docstring")
        self.asserTrue(len(module_doc) > 1, "city.py needs a docstring")

    def test_class_docstring(self):
        """test for class docstring"""
        self.assertIsNot(City.__doc__, None, "City needs a docstring")
        self.asserTrue(len(City.__doc__) > 1, "City needs a docstring")

    def test_fnc_docstring(self):
        """test for method docstring"""
        for func in self.city:
            with self.subTest(function=func):
                self.assertIsNot(
                        func[1].__doc__,
                        None,
                        "{:s} method needs a doctsring".format(func[0])
                        )
                self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0]))

class TestCity(unittest.TestCase):
     """ Test city"""
    def test_is_subclass(self):
        """Test user is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_state_id(self):
        """test user has attr email and is not empty"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_name(self):
        """test city has attr name and is not empty"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
