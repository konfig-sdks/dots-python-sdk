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

from dots_python_sdk.type.payout_link import PayoutLink

class RequiredPayoutlinksListAllResponse(TypedDict):
    pass

class OptionalPayoutlinksListAllResponse(TypedDict, total=False):
    # `true` if there are more `payout-links`.
    has_more: bool

    # Array of `payout-links`.
    data: typing.List[PayoutLink]

class PayoutlinksListAllResponse(RequiredPayoutlinksListAllResponse, OptionalPayoutlinksListAllResponse):
    pass
