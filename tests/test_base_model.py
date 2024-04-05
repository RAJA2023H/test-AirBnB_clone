#!/usr/bin/env python3
"""
tests BaseClass module
"""
from models.base_model import BaseModel
import unittest
import models.base_model as base
import datetime
import uuid
import os


class TestBaseClass(unittest.TestCase):
    """
    tests BaseClass module
    """
    def test_docstring(self):
        """ checks if the class is documented """
        # Check if the BaseModel class has a docstring
        self.assertTrue(BaseModel.__doc__)
        # Check if the docstring is not empty
        self.assertNotEqual(BaseModel.__doc__.strip(), '')

    def setUp(self):
        """ Sets up all values for each test case """
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj1.name = "My First Model"
        obj2.name = "My Second Model"
        obj1.number = 89
        obj2.number = 1

    def new_round(self):
        """
        removes all memory allocated or variables
        declared after each test
        """
        self.obj1 = None
        self.obj2 = None

    def test_id(self):
        """ checks the type and format of id generated """
        self.assertIsNotNone(obj1.id)
        self.assertIsInstance(obj1.id, str)
        self.assertIsNotNone(obj2.id)
        self.assertIsInstance(obj2.id, str)
        self.assertNotEqual(obj1.id, obj2.id)
        # Check if the ID follows the format of UUID version 4
        try:
            uuid.UUID(obj1.id, version=4)
        except ValueError:
            self.fail("ID is not in UUID version 4 format")

    def test_time(self):
        """ tests the value of created_at and updated_at """
        self.assertIsInstance(obj1.created_at, datetime.datetime)
        self.assertIsInstance(obj1.updated_at, datetime.datetime)
        self.assertIsInstance(obj2.created_at, datetime.datetime)
        self.assertIsInstance(obj2.updated_at, datetime.datetime)
        self.assertIsNotNone(self.obj1.created_at)
        self.assertIsNotNone(self.obj1.updated_at)
        self.assertIsNotNone(self.obj2.created_at)
        self.assertIsNotNone(self.obj2.updated_at)

    def test_save(self):
        """ checks the save method """
        previous_time = self.obj1.updated_at
        self.obj1.save()
        self.assertNotEqual(self.obj1.updated_at, previous_time)
