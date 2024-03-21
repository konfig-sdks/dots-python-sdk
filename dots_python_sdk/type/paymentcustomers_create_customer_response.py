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


class RequiredPaymentcustomersCreateCustomerResponse(TypedDict):
    pass

class OptionalPaymentcustomersCreateCustomerResponse(TypedDict, total=False):
    id: str

    user_id: str

    email: str

    country_code: str

    phone_number: str

class PaymentcustomersCreateCustomerResponse(RequiredPaymentcustomersCreateCustomerResponse, OptionalPaymentcustomersCreateCustomerResponse):
    pass
