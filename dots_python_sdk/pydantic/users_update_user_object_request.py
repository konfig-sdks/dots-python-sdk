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


class UsersUpdateUserObjectRequest(BaseModel):
    # Configures the user's default payout method. Must be a payout method already configured by the user.
    default_payout_method: typing.Optional[Literal["paypal", "venmo", "cash_app", "ach", "intl_bank"]] = Field(None, alias='default_payout_method')

    # Enables auto payout for the user whenever a default payout method is defined
    auto_payout_enabled: typing.Optional[bool] = Field(None, alias='auto_payout_enabled')

    # Arbitrary metadata
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
