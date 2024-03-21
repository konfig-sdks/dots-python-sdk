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


class PaymentCustomer(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    user_id: typing.Optional[str] = Field(None, alias='user_id')

    email: typing.Optional[str] = Field(None, alias='email')

    country_code: typing.Optional[str] = Field(None, alias='country_code')

    phone_number: typing.Optional[str] = Field(None, alias='phone_number')

    first_name: typing.Optional[str] = Field(None, alias='first_name')

    middle_name: typing.Optional[str] = Field(None, alias='middle_name')

    last_name: typing.Optional[str] = Field(None, alias='last_name')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    created: typing.Optional[datetime] = Field(None, alias='created')

    updated: typing.Optional[datetime] = Field(None, alias='updated')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
