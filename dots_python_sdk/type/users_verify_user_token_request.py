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


class RequiredUsersVerifyUserTokenRequest(TypedDict):
    # The token sent to the user.
    token: str

class OptionalUsersVerifyUserTokenRequest(TypedDict, total=False):
    pass

class UsersVerifyUserTokenRequest(RequiredUsersVerifyUserTokenRequest, OptionalUsersVerifyUserTokenRequest):
    pass
