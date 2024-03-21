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


class RequiredRefundsCreateRefundRequest(TypedDict):
    # Amount in cents
    amount: int

    # ID of the `payment_intent` you are refunding.
    payment_intent_id: str

class OptionalRefundsCreateRefundRequest(TypedDict, total=False):
    reason: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: bool

class RefundsCreateRefundRequest(RequiredRefundsCreateRefundRequest, OptionalRefundsCreateRefundRequest):
    pass
