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

from dots_python_sdk.type.flow_completed_steps import FlowCompletedSteps
from dots_python_sdk.type.flow_steps import FlowSteps

class RequiredFlow(TypedDict):
    pass

class OptionalFlow(TypedDict, total=False):
    # ID of the `flow`.
    id: str

    # Date that the `flow` was created.
    created: datetime

    # ID of the `user` that has claimed the `flow`.
    user_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    steps: FlowSteps

    completed_steps: FlowCompletedSteps

    # URL to access the `flow`. Can be embedded in an `iframe`.
    link: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class Flow(RequiredFlow, OptionalFlow):
    pass
