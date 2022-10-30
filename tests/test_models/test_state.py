#!/usr/bin/python3
"""Contains tests for the State Class"""

import unittest
import models
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
import time
import inspect
module_doc = models.state.__doc__


class TestStateDoc(unittest.TestCase):
    """To check doxumentation"""
    @classmethod
    def setUpClass(self):
        """docstring test"""
        cls.state_funcs = inspect.getmembers(State, inspect.isfunction)

    def test_module_docstring(self):
        """test for module docstring"""
        self.assertIsNot(module_doc, None, "state.py needs a docstring")
        self.asserTrue(len(module_doc) > 1, "state.py needs a docstring")

    def test_class_docstring(self):
        """test for class docstring"""
        self.assertIsNot(State.__doc__, None, "State needs a docstring")
        self.asserTrue(len(State.__doc__) > 1, "State needs a docstring")

    def test_fnc_docstring(self):
        """test for method docstring"""
        for func in self.state:
            with self.subTest(function=func):
                 self.assertIsNot(
                        func[1].__doc__,
                        None,
                        "{:s} method needs a doctsring".format(func[0])
                        )
                self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0]))

class TestState(unittest.TestCase):
    """ Test state"""
    def test_is_subclass(self):
        """Test user is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name(self):
        """test state has attrbute name and is not empty"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
