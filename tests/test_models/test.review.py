#!/usr/bin/python3
"""
A module that contains the test suite for the BaseModel class
"""
import unittest
from time import sleep
import os
from datetime import datetime
from uuid import uuid4

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model.BaseModel
    """

    def test_if_BaseModel_instance_has_id(self):
        """
        Checks that instance has an id assigned on initialization
        """
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        
        

    def test_str_representation(self):
        """
        Checks if the string representation is appropriate
        """
        b = BaseModel()
        self.assertEqual(str(b),
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    def test_ids_is_unique(self):
        """
        Checks if id is generated randomly and uniquely
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    def test_type_of_id_is_str(self):
        """
        Checks that id generated is a str object
        """
        b = BaseModel()
        self.assertTrue(type(b.id) is str)
