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

from dots_python_sdk.pydantic.user import User

class UsersListAllUsersResponse(BaseModel):
    # Array of `user` objects.
    data: typing.Optional[typing.List[User]] = Field(None, alias='data')

    # `true` if there are more objects.
    has_more: typing.Optional[bool] = Field(None, alias='has_more')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
