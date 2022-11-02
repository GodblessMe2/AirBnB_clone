#!/usr/bin/python3
"""Test basemodel"""
from datetime import datetime
from models.base_model import BaseModel
import unittest
import models
import pep8 as pycodestyle
import time
import inspect
module_doc = models.base_model.__doc__


class TestBaseModelDoc(unittest.TestCase):
    """To check documentation and style"""
    @classmethod
    def setUpClass(self):
        """docstring test"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pycodestyle(self):
        """pycodestyle"""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """test for module docstring"""
        self.assertIsNot(module_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "base_model.py needs a docstring")

    def test_class_docstring(self):
        """test for class doctsring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel needs a docstring")

    def test_fnc_docstring(self):
        """test for method docstring"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                        func[1].__doc__,
                        None,
                        "{:s} method needs a docstring".format(func[0])
                        )
                self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0])
                        )


class TestBaseModel(unittest.TestCase):
    """Test BaseModel"""
    def test_init(self):
        """Test instantiation"""
        init = BaseModel()
        self.assertIs(type(init), BaseModel)
        attrs_type = {
                "id": str,
                "created_at": datetime,
                "updated_at": datetime
                }
        for attr, typ in attrs_type.items():
            with self.subTest(attr=attr, typ=typ):
                self.assertIn(attr, init.__dict__)
                self.assertIs(type(init.__dict__[attr]), typ)

    def test_datetime(self):
        """Test that 2 basemodelshave diff datetime obj"""
        tic = datetime.now()
        init1 = BaseModel()
        toc = datetime.now()
        """self.assertTrue(tic <= init1.created_at <= toc)"""
        time.sleep(1e-4)
        tic = datetime.now()
        init2 = BaseModel()
        toc = datetime.now()
        """self.assertTrue(tic <= init2.created_at <= toc)"""
        self.assertEqual(init1.created_at, init1.updated_at)
        self.assertEqual(init2.created_at, init2.updated_at)
        self.assertNotEqual(init1.created_at, init2.created_at)
        self.assertNotEqual(init1.updated_at, init2.updated_at)

    def test_to_dict(self):
        """Test conversion to dictionary for json"""
        my_model = BaseModel()
        d = my_model.to_dict()
        expected_attr = ['id',
                         'created_at',
                         'updated_at',
                         '__class__']
        self.assertCountEqual(d.keys(), expected_attr)
        self.assertEqual(d['__class__'], 'BaseModel')

    def test_to_dict_val(self):
        """test vals in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        base = BaseModel()
        new_d = base.to_dict()
        self.assertEqual(new_d['__class__'], 'BaseModel')
        self.assertEqual(type(new_d['created_at']), str)
        self.assertEqual(type(new_d['updated_at']), str)
        self.assertEqual(new_d['created_at'],
                         base.created_at.strftime(t_format))
        self.assertEqual(new_d['updated_at'],
                         base.updated_at.strftime(t_format))

    def test_str(self):
        """test correct output for str"""
        init = BaseModel()
        string = "[BaseModel] ({}) {}".format(init.id, init.__dict__)
        self.assertEqual(string, str(init))

    def test_uuid(self):
        """test id is a valid uuid"""
        init1 = BaseModel()
        init2 = BaseModel()
        for init in [init1, init2]:
            uuid = init.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(init1.id, init2.id)
