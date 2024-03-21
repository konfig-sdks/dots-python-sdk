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


class RequiredPaymentmethodsDetachPaymentMethodRequest(TypedDict):
    pass

class OptionalPaymentmethodsDetachPaymentMethodRequest(TypedDict, total=False):
    # ID of the payment customer to detach the payment method from.
    customer_id: str

class PaymentmethodsDetachPaymentMethodRequest(RequiredPaymentmethodsDetachPaymentMethodRequest, OptionalPaymentmethodsDetachPaymentMethodRequest):
    pass
