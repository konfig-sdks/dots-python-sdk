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

from dots_python_sdk.type.user_compliance import UserCompliance
from dots_python_sdk.type.user_phone_number import UserPhoneNumber
from dots_python_sdk.type.wallet import Wallet

class RequiredUser(TypedDict):
    pass

class OptionalUser(TypedDict, total=False):
    id: str

    first_name: str

    last_name: str

    email: str

    phone_number: UserPhoneNumber

    wallet: Wallet

    compliance: UserCompliance

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class User(RequiredUser, OptionalUser):
    pass
