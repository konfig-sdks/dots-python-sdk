# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

import unittest
from unittest.mock import patch

import urllib3

import dots_python_sdk
from dots_python_sdk.paths.v2_payment_intents import get
from dots_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2PaymentIntents(ApiTestMixin, unittest.TestCase):
    """
    V2PaymentIntents unit test stubs
        List all Payment Intents
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
