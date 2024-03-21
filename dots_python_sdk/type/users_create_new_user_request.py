# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredUsersCreateNewUserRequest(TypedDict):
    # The user's first name.
    first_name: str

    # The user's last name.
    last_name: str

    # The user's email address.
    email: str

    # The user's phone number country code. e.g. \"1\"
    country_code: str

    # The user's phone number. e.g. \"4157223331\".
    phone_number: str

class OptionalUsersCreateNewUserRequest(TypedDict, total=False):
    # Username to assign the user.
    username: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class UsersCreateNewUserRequest(RequiredUsersCreateNewUserRequest, OptionalUsersCreateNewUserRequest):
    pass
