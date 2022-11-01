#!/usr/bin/python3
"""Contains tests for the Amenity Class"""

import unittest
import models
import time 
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
import inspect
module_doc = models.amenity.__doc__


class TestStateDoc(unittest.TestCase):
    """To check doxumentation"""
    @classmethod
    def setUpClass(self):
        """docstring test"""
        cls.amenity_funcs = inspect.getmembers(Amenity, inspect.isfunction)

    def test_module_docstring(self):
        """test for module docstring"""
        self.assertIsNot(module_doc, None, "amenity.py needs a docstring")
        self.asserTrue(len(module_doc) > 1, "amenity.py needs a docstring")

    def test_class_docstring(self):
        """test for class docstring"""
        self.assertIsNot(Amenity.__doc__, None, "Amenity needs a docstring")
        self.asserTrue(len(Amenity.__doc__) > 1, "Amenity needs a docstring")

    def test_fnc_docstring(self):
        """test for method docstring"""
        for func in self.amenity:
            with self.subTest(function=func):
                self.assertIsNot(
                        func[1].__doc__,
                        None,
                        "{:s} method needs a docstring".format(func[0])
                        )
                self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0]))
            
class TestAmenity(unittest.TestCase):

    """ Test amenity"""
    def test_is_subclass(self):
        """Test amenity is a subclass of BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name(self):
        """test amenity has attrbute name and is not empty"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
