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

from dots_python_sdk.type.user import User

class RequiredUsersListAllUsersResponse(TypedDict):
    pass

class OptionalUsersListAllUsersResponse(TypedDict, total=False):
    # Array of `user` objects.
    data: typing.List[User]

    # `true` if there are more objects.
    has_more: bool

class UsersListAllUsersResponse(RequiredUsersListAllUsersResponse, OptionalUsersListAllUsersResponse):
    pass
