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

from dots_python_sdk.pydantic.user_compliance import UserCompliance
from dots_python_sdk.pydantic.user_phone_number import UserPhoneNumber
from dots_python_sdk.pydantic.wallet import Wallet

class User(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    first_name: typing.Optional[str] = Field(None, alias='first_name')

    last_name: typing.Optional[str] = Field(None, alias='last_name')

    email: typing.Optional[str] = Field(None, alias='email')

    phone_number: typing.Optional[UserPhoneNumber] = Field(None, alias='phone_number')

    wallet: typing.Optional[Wallet] = Field(None, alias='wallet')

    compliance: typing.Optional[UserCompliance] = Field(None, alias='compliance')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
