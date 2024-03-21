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

from dots_python_sdk.type.payment_method import PaymentMethod

class RequiredPaymentmethodsListAllPaymentCustomerResponse(TypedDict):
    pass

class OptionalPaymentmethodsListAllPaymentCustomerResponse(TypedDict, total=False):
    # List of payment methods.
    data: typing.List[PaymentMethod]

    has_more: bool

class PaymentmethodsListAllPaymentCustomerResponse(RequiredPaymentmethodsListAllPaymentCustomerResponse, OptionalPaymentmethodsListAllPaymentCustomerResponse):
    pass
