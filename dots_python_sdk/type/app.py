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

from dots_python_sdk.type.app_metrics import AppMetrics

class RequiredApp(TypedDict):
    id: str

    name: str

    metrics: AppMetrics

class OptionalApp(TypedDict, total=False):
    # App verification status. Some Dots use cases require newly created apps to pass KYB review.
    status: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class App(RequiredApp, OptionalApp):
    pass
