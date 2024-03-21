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


class RequiredDisputesSubmitDisputeRequest(TypedDict):
    description: str

class OptionalDisputesSubmitDisputeRequest(TypedDict, total=False):
    pass

class DisputesSubmitDisputeRequest(RequiredDisputesSubmitDisputeRequest, OptionalDisputesSubmitDisputeRequest):
    pass
