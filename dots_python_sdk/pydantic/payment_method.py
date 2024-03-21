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


class PaymentMethod(BaseModel):
    platform: Literal["ach", "paypal", "venmo", "cash_app", "intl_transfer"] = Field(alias='platform')

    description: typing.Optional[str] = Field(None, alias='description')

    # ID of the `payment-method`.
    id: typing.Optional[str] = Field(None, alias='id')

    mask: typing.Optional[str] = Field(None, alias='mask')

    email: typing.Optional[str] = Field(None, alias='email')

    phone_number: typing.Optional[str] = Field(None, alias='phone_number')

    cash_tag: typing.Optional[str] = Field(None, alias='cash_tag')

    country: typing.Optional[str] = Field(None, alias='country')

    currency: typing.Optional[str] = Field(None, alias='currency')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
