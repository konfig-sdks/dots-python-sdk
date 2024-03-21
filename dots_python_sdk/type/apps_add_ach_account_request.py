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


class RequiredAppsAddAchAccountRequest(TypedDict):
    # The bank account number.
    account_number: str

    # The bank's ABA routing number.
    routing_number: str

    # The type of bank account.
    account_type: str

class OptionalAppsAddAchAccountRequest(TypedDict, total=False):
    pass

class AppsAddAchAccountRequest(RequiredAppsAddAchAccountRequest, OptionalAppsAddAchAccountRequest):
    pass
