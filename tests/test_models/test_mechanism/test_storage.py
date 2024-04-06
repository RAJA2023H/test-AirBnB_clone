#!/usr/bin/python3
"""
"""
import unitest
from models.base_model import BaseModel
import json
import os


class StorageTestCase(ynittest.TestCase):
    """ """
    def test_Storage_init(self):
        """ """
        Path = models.storage.__Storage__json_file
