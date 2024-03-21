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


class UsersSubmitComplianceInfoRequestW9Address(BaseModel):
    # Address line 1.
    line_1: str = Field(alias='line_1')

    # City.
    city: str = Field(alias='city')

    # State.
    state: str = Field(alias='state')

    # Country.
    country: str = Field(alias='country')

    # Postal code or Zip code.
    postcode: str = Field(alias='postcode')

    # Address Line 2
    line_2: typing.Optional[str] = Field(None, alias='line_2')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
