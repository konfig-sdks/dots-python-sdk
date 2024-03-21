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
from dots_python_sdk.type.payout_request_payee import PayoutRequestPayee
from dots_python_sdk.type.user import User

RequiredPayoutRequest = TypedDict("RequiredPayoutRequest", {
    })

OptionalPayoutRequest = TypedDict("OptionalPayoutRequest", {
    # ID of the `payout-request`.
    "id": str,

    # Date that the `payout-request` was created.
    "created": datetime,

    # Amount in cents of the `payout-request`.
    "amount": typing.Union[int, float],

    # Status of the `payout-request`.
    "status": str,

    "payee": PayoutRequestPayee,

    "payout-link": PayoutLink,

    "user": User,

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    "metadata": typing.Union[bool, date, datetime, dict, float, int, list, str, None],

    "memo": typing.Union[bool, date, datetime, dict, float, int, list, str, None],
    }, total=False)

class PayoutRequest(RequiredPayoutRequest, OptionalPayoutRequest):
    pass
