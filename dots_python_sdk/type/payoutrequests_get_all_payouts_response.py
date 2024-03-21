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

from dots_python_sdk.type.payout_request import PayoutRequest

class RequiredPayoutrequestsGetAllPayoutsResponse(TypedDict):
    pass

class OptionalPayoutrequestsGetAllPayoutsResponse(TypedDict, total=False):
    # `true` if there are more `payout-requests`.
    has_more: bool

    # Array of `payout-request`.
    data: typing.List[PayoutRequest]

class PayoutrequestsGetAllPayoutsResponse(RequiredPayoutrequestsGetAllPayoutsResponse, OptionalPayoutrequestsGetAllPayoutsResponse):
    pass
