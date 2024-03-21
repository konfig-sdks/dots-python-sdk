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


class RequiredPaymentMethod(TypedDict):
    platform: str

class OptionalPaymentMethod(TypedDict, total=False):
    description: str

    # ID of the `payment-method`.
    id: str

    mask: str

    email: str

    phone_number: str

    cash_tag: str

    country: str

    currency: str

class PaymentMethod(RequiredPaymentMethod, OptionalPaymentMethod):
    pass
