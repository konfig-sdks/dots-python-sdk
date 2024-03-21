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


class RequiredPayoutsCreatePayoutRequest(TypedDict):
    # ID of the `user` who you are creating the payout for.
    user_id: str

    # Amount in cents to payout the user.
    amount: int

    # Platform that you are paying out the `user` through,
    platform: str

class OptionalPayoutsCreatePayoutRequest(TypedDict, total=False):
    # The bank account ID you are paying to. Required for `ach` and `intl_bank`.
    account_id: str

    # Creates a transfer for the amount to the user before creating the payout. The funds are returned if the payout does not succeed.
    fund: bool

    # UUID that will be used to idempotently handle requests. Transfers with existing idempotency keys will be rejected.
    idempotency_key: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class PayoutsCreatePayoutRequest(RequiredPayoutsCreatePayoutRequest, OptionalPayoutsCreatePayoutRequest):
    pass
