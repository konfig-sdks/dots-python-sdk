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

from dots_python_sdk.type.payoutrequests_submit_request_request_payee import PayoutrequestsSubmitRequestRequestPayee

class RequiredPayoutrequestsSubmitRequestRequest(TypedDict):
    # The amount in cents to pay the user.
    amount: int

class OptionalPayoutrequestsSubmitRequestRequest(TypedDict, total=False):
    # The user's id. `user_id` or `payee` is required.
    user_id: str

    payee: PayoutrequestsSubmitRequestRequestPayee

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Add a memo to payout request
    memo: str

class PayoutrequestsSubmitRequestRequest(RequiredPayoutrequestsSubmitRequestRequest, OptionalPayoutrequestsSubmitRequestRequest):
    pass
