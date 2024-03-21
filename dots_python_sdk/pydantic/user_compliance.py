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


class UserCompliance(BaseModel):
    tax_id_collected: typing.Optional[bool] = Field(None, alias='tax_id_collected')

    address_collected: typing.Optional[bool] = Field(None, alias='address_collected')

    date_of_birth_collected: typing.Optional[bool] = Field(None, alias='date_of_birth_collected')

    must_collect_1099: typing.Optional[bool] = Field(None, alias='must_collect_1099')

    1099_collected_: typing.Optional[bool] = Field(None, alias='1099_collected')

    w8_ben_collected: typing.Optional[bool] = Field(None, alias='w8_ben_collected')

    flagged: typing.Optional[bool] = Field(None, alias='flagged')

    id_verified: typing.Optional[bool] = Field(None, alias='id_verified')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
