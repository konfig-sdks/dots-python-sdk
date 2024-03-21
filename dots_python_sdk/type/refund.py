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


class RequiredRefund(TypedDict):
    pass

class OptionalRefund(TypedDict, total=False):
    id: str

class Refund(RequiredRefund, OptionalRefund):
    pass
