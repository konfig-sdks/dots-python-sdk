# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

import unittest

import os
from pprint import pprint
from dots_python_sdk import Dots

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        dots = Dots(
        
            username = 'YOUR_USERNAME',
            password = 'YOUR_PASSWORD'
        )
        self.assertIsNotNone(dots)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
