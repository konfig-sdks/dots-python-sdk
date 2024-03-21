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


class PayoutlinksCreatePayoutLinkRequestPayee(BaseModel):
    # First name of the payee.
    first_name: typing.Optional[str] = Field(None, alias='first_name')

    # Last name of the payee.
    last_name: typing.Optional[str] = Field(None, alias='last_name')

    # Country code of the payee's phone number e.g. \"1\" for USA.
    country_code: typing.Optional[str] = Field(None, alias='country_code')

    # Rest of the payee's phone number.
    phone_number: typing.Optional[str] = Field(None, alias='phone_number')

    # Payee's email address.
    email: typing.Optional[str] = Field(None, alias='email')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
