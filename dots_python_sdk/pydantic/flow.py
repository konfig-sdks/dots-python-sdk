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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from dots_python_sdk.pydantic.flow_completed_steps import FlowCompletedSteps
from dots_python_sdk.pydantic.flow_steps import FlowSteps

class Flow(BaseModel):
    # ID of the `flow`.
    id: typing.Optional[str] = Field(None, alias='id')

    # Date that the `flow` was created.
    created: typing.Optional[datetime] = Field(None, alias='created')

    # ID of the `user` that has claimed the `flow`.
    user_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='user_id')

    steps: typing.Optional[FlowSteps] = Field(None, alias='steps')

    completed_steps: typing.Optional[FlowCompletedSteps] = Field(None, alias='completed_steps')

    # URL to access the `flow`. Can be embedded in an `iframe`.
    link: typing.Optional[str] = Field(None, alias='link')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
