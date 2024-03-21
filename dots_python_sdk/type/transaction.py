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


class RequiredTransaction(TypedDict):
    pass

class OptionalTransaction(TypedDict, total=False):
    id: int

    amount: typing.Union[int, float]

    created: datetime

    source_name: str

    destination_name: str

    # The general category of the transaction
    type: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class Transaction(RequiredTransaction, OptionalTransaction):
    pass
