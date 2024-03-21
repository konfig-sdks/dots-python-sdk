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


class RequiredPaymentIntent(TypedDict):
    id: str

    # Amount in cents
    amount: int

    currency: str

class OptionalPaymentIntent(TypedDict, total=False):
    user_id: str

    status: str

    transfer_id: str

    payment_method_id: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Only availble on payment intent creation.
    client_secret: str

class PaymentIntent(RequiredPaymentIntent, OptionalPaymentIntent):
    pass
