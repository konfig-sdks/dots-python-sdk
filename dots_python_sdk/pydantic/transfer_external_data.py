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


class TransferExternalData(BaseModel):
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    external_id: typing.Optional[str] = Field(None, alias='external_id')

    platform: typing.Optional[Literal["ach", "paypal", "venmo", "visa", "amazon", "cash_app", "intl_bank", "intl_transfer", "bank_transfer", "payoneer", "airtm"]] = Field(None, alias='platform')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
