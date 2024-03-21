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


class UsersCreateNewUserRequest(BaseModel):
    # The user's first name.
    first_name: str = Field(alias='first_name')

    # The user's last name.
    last_name: str = Field(alias='last_name')

    # The user's email address.
    email: str = Field(alias='email')

    # The user's phone number country code. e.g. \"1\"
    country_code: str = Field(alias='country_code')

    # The user's phone number. e.g. \"4157223331\".
    phone_number: str = Field(alias='phone_number')

    # Username to assign the user.
    username: typing.Optional[str] = Field(None, alias='username')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
