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

from dots_python_sdk.type.payment_customer import PaymentCustomer

class RequiredPaymentcustomersListAllResponse(TypedDict):
    pass

class OptionalPaymentcustomersListAllResponse(TypedDict, total=False):
    data: typing.List[PaymentCustomer]

    # `true` if there are more objects.
    has_more: bool

class PaymentcustomersListAllResponse(RequiredPaymentcustomersListAllResponse, OptionalPaymentcustomersListAllResponse):
    pass
