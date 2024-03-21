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

from dots_python_sdk.pydantic.app_metrics import AppMetrics

class App(BaseModel):
    id: str = Field(alias='id')

    name: str = Field(alias='name')

    metrics: AppMetrics = Field(alias='metrics')

    # App verification status. Some Dots use cases require newly created apps to pass KYB review.
    status: typing.Optional[Literal["created", "in_review", "approved"]] = Field(None, alias='status')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
