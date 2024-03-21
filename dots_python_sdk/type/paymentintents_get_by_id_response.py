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


class RequiredPaymentintentsGetByIdResponse(TypedDict):
    pass

class OptionalPaymentintentsGetByIdResponse(TypedDict, total=False):
    error: str

class PaymentintentsGetByIdResponse(RequiredPaymentintentsGetByIdResponse, OptionalPaymentintentsGetByIdResponse):
    pass
