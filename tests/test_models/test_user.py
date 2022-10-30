#!/usr/bin/python3
"""Contains tests for the user Class"""

import unittest
import models
import time
from datetime import datetime
from models.user import user
from models.base_model import BaseModel
import inspect
module_doc = models.user.__doc__


class TestUserDoc(unittest.TestCase):
    """To check doxumentation"""
    @classmethod
    def setUpClass(self):
        """docstring test"""
        cls.user_funcs = inspect.getmembers(User, inspect.isfunction)

    def test_module_docstring(self):
        """test for module docstring"""
        self.assertIsNot(module_doc, None, "user.py needs a docstring")
        self.asserTrue(len(module_doc) > 1, "user.py needs a docstring")

    def test_class_docstring(self):
        """test for class docstring"""
        self.assertIsNot(User.__doc__, None, "User needs a docstring")
        self.asserTrue(len(User.__doc__) > 1, "User needs a docstring")

    def test_fnc_docstring(self):
        """test for method docstring"""
        for func in self.user:
            with self.subTest(function=func):
                self.assertIsNot(
                        func[1].__doc__,
                        None,
                        "{:s} method needs a doctsring".format(func[0])
                        )
                self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0]))

class TestUser(unittest.TestCase):
    """ Test User"""
    def test_is_subclass(self):
        """Test user is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_email(self):
        """test user has attr email and is not empty"""
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_password(self):
        """test user has attr password and is not empty"""
        user = User()
        self.assertTrue(hasattr(user, "password"))
        self.assertEqual(user.password, "")

    def test_first_name:
        """test user has attr first_name and is not empty"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertEqual(user.first_name, "")

    def test_last_name:
        """test user has attr last_name and is not empty"""
        user = User()
        self.assertTrue(hasattr(user, "last_name"))
        self.assertEqual(user.last_name, "")
