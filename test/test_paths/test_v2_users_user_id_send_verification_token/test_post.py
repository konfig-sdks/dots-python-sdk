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
from dots_python_sdk.paths.v2_users_user_id_send_verification_token import post
from dots_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV2UsersUserIdSendVerificationToken(ApiTestMixin, unittest.TestCase):
    """
    V2UsersUserIdSendVerificationToken unit test stubs
        Send a Verification Token
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 202
    response_body = ''


if __name__ == '__main__':
    unittest.main()
