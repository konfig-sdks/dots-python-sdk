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

from dots_python_sdk.type.checkout_session_line_items import CheckoutSessionLineItems

class RequiredCheckoutSession(TypedDict):
    pass

class OptionalCheckoutSession(TypedDict, total=False):
    id: str

    status: str

    payment_intent_id: str

    success_url: str

    cancel_url: str

    checkout_session_url: str

    client_reference_id: str

    expiry: datetime

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    line_items: CheckoutSessionLineItems

    created: datetime

    updated: datetime

    # `payment-customer` ID
    customer_id: str

    customer_email: str

    amount_total: int

class CheckoutSession(RequiredCheckoutSession, OptionalCheckoutSession):
    pass
