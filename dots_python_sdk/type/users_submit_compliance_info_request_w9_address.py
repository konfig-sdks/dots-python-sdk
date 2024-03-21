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


class RequiredUsersSubmitComplianceInfoRequestW9Address(TypedDict):
    # Address line 1.
    line_1: str

    # City.
    city: str

    # State.
    state: str

    # Country.
    country: str

    # Postal code or Zip code.
    postcode: str

class OptionalUsersSubmitComplianceInfoRequestW9Address(TypedDict, total=False):
    # Address Line 2
    line_2: str

class UsersSubmitComplianceInfoRequestW9Address(RequiredUsersSubmitComplianceInfoRequestW9Address, OptionalUsersSubmitComplianceInfoRequestW9Address):
    pass
