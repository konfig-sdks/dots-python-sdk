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

from dots_python_sdk.type.dispute_file import DisputeFile

class RequiredDispute(TypedDict):
    pass

class OptionalDispute(TypedDict, total=False):
    id: str

    payment_intent_id: str

    status: str

    evidence: typing.List[DisputeFile]

class Dispute(RequiredDispute, OptionalDispute):
    pass
