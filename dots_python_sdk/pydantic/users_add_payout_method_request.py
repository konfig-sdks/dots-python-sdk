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


class UsersAddPayoutMethodRequest(BaseModel):
    # Payout platform to add.
    platform: Literal["paypal", "venmo", "cash_app", "ach"] = Field(alias='platform')

    # Bank account or Cash App routing number. Required if `platform` = `ach` or `cash_app`.
    routing_number: typing.Optional[str] = Field(None, alias='routing_number')

    # Bank account or Cash App account number. Required if `platform` = `ach` or `cash_app`.
    account_number: typing.Optional[str] = Field(None, alias='account_number')

    # Bank account type. Required if `platform` = `ach`.
    account_type: typing.Optional[Literal["checking", "savings"]] = Field(None, alias='account_type')

    # PayPal email address. Required if `platform` = `paypal`.
    email: typing.Optional[str] = Field(None, alias='email')

    # Venmo phone number. One of `phone_number` or `handle` is required if `platform` = `venmo`.
    phone_number: typing.Optional[str] = Field(None, alias='phone_number')

    # Venmo handle. One of `phone_number` or `handle` is required if `platform` = `venmo`.
    handle: typing.Optional[str] = Field(None, alias='handle')

    # Cash App Cash Tag. Required if `platform` = `cash_app`.
    cash_tag: typing.Optional[str] = Field(None, alias='cash_tag')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
