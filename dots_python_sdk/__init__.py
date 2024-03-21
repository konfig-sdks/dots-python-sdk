# coding: utf-8

# flake8: noqa

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

__version__ = "1.0"

# import ApiClient
from dots_python_sdk.api_client import ApiClient

# import Configuration
from dots_python_sdk.configuration import Configuration

# import exceptions
from dots_python_sdk.exceptions import OpenApiException
from dots_python_sdk.exceptions import ApiAttributeError
from dots_python_sdk.exceptions import ApiTypeError
from dots_python_sdk.exceptions import ApiValueError
from dots_python_sdk.exceptions import ApiKeyError
from dots_python_sdk.exceptions import ApiException

from dots_python_sdk.client import Dots
