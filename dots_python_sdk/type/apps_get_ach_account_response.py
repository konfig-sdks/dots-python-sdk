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


class RequiredAppsGetAchAccountResponse(TypedDict):
    pass

class OptionalAppsGetAchAccountResponse(TypedDict, total=False):
    # The last four digits of the bank account number.
    mask: str

    # The name of the bank account.
    name: str

class AppsGetAchAccountResponse(RequiredAppsGetAchAccountResponse, OptionalAppsGetAchAccountResponse):
    pass
