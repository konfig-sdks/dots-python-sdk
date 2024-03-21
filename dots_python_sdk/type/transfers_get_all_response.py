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

from dots_python_sdk.type.transfer import Transfer

class RequiredTransfersGetAllResponse(TypedDict):
    pass

class OptionalTransfersGetAllResponse(TypedDict, total=False):
    # `true` if there are more `transfers`.
    has_more: bool

    # Array of `transfers`.
    data: typing.List[Transfer]

class TransfersGetAllResponse(RequiredTransfersGetAllResponse, OptionalTransfersGetAllResponse):
    pass
