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

from dots_python_sdk.type.dispute import Dispute

class RequiredDisputesGetAllResponse(TypedDict):
    pass

class OptionalDisputesGetAllResponse(TypedDict, total=False):
    has_more: bool

    data: typing.List[Dispute]

class DisputesGetAllResponse(RequiredDisputesGetAllResponse, OptionalDisputesGetAllResponse):
    pass
