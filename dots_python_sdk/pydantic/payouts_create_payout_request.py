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


class PayoutsCreatePayoutRequest(BaseModel):
    # ID of the `user` who you are creating the payout for.
    user_id: str = Field(alias='user_id')

    # Amount in cents to payout the user.
    amount: int = Field(alias='amount')

    # Platform that you are paying out the `user` through,
    platform: Literal["paypal", "venmo", "ach", "bank_transfer", "cash_app", "payoneer", "airtm", "default"] = Field(alias='platform')

    # The bank account ID you are paying to. Required for `ach` and `intl_bank`.
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    # Creates a transfer for the amount to the user before creating the payout. The funds are returned if the payout does not succeed.
    fund: typing.Optional[bool] = Field(None, alias='fund')

    # UUID that will be used to idempotently handle requests. Transfers with existing idempotency keys will be rejected.
    idempotency_key: typing.Optional[str] = Field(None, alias='idempotency_key')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
