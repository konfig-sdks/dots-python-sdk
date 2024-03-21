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

from dots_python_sdk.pydantic.flow import Flow

class FlowsListAllResponse(BaseModel):
    # `true` if there are more `flows`.
    has_more: typing.Optional[bool] = Field(None, alias='has_more')

    # Array of `flow` objects.
    data: typing.Optional[typing.List[Flow]] = Field(None, alias='data')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
