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


class RequiredUsersSubmitComplianceInfoRequestW8BenAddress(TypedDict):
    # Address line 1.
    line_1: str

    # City.
    city: str

    # State.
    state: str

    # Country.
    country: str

    # Postal code or Zip Code.
    postcode: str

class OptionalUsersSubmitComplianceInfoRequestW8BenAddress(TypedDict, total=False):
    # Address line 2.
    line_2: str

class UsersSubmitComplianceInfoRequestW8BenAddress(RequiredUsersSubmitComplianceInfoRequestW8BenAddress, OptionalUsersSubmitComplianceInfoRequestW8BenAddress):
    pass
