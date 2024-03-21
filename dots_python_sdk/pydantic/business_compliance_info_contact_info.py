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


class BusinessComplianceInfoContactInfo(BaseModel):
    city: str = Field(alias='city')

    # Country name or country code
    country: str = Field(alias='country')

    # Primary contact email address. Service emails will be sent to this address.
    email: str = Field(alias='email')

    # Address line 1
    line1: str = Field(alias='line1')

    phone_number: str = Field(alias='phone_number')

    # State when applicable
    state: str = Field(alias='state')

    # ZIP or postal code
    zip: str = Field(alias='zip')

    # Address line 2
    line2: typing.Optional[str] = Field(None, alias='line2')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
