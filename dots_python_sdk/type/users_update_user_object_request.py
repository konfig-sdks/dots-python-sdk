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


class RequiredUsersUpdateUserObjectRequest(TypedDict):
    pass

class OptionalUsersUpdateUserObjectRequest(TypedDict, total=False):
    # Configures the user's default payout method. Must be a payout method already configured by the user.
    default_payout_method: str

    # Enables auto payout for the user whenever a default payout method is defined
    auto_payout_enabled: bool

    # Arbitrary metadata
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class UsersUpdateUserObjectRequest(RequiredUsersUpdateUserObjectRequest, OptionalUsersUpdateUserObjectRequest):
    pass
