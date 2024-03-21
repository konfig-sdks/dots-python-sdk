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


class RequiredPaymentintentsConfirmIntentRequest(TypedDict):
    # ID of the payment method to confirm the intent with.
    payment_method_id: str

class OptionalPaymentintentsConfirmIntentRequest(TypedDict, total=False):
    pass

class PaymentintentsConfirmIntentRequest(RequiredPaymentintentsConfirmIntentRequest, OptionalPaymentintentsConfirmIntentRequest):
    pass
