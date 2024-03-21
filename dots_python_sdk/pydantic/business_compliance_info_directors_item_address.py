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


class BusinessComplianceInfoDirectorsItemAddress(BaseModel):
    city: str = Field(alias='city')

    country: str = Field(alias='country')

    line1: str = Field(alias='line1')

    zip: str = Field(alias='zip')

    line2: typing.Optional[str] = Field(None, alias='line2')

    state: typing.Optional[str] = Field(None, alias='state')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
