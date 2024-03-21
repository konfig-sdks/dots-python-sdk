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


class PaymentsCreateTransactionRequestAchInfo(BaseModel):
    account_number: typing.Optional[str] = Field(None, alias='account_number')

    routing_number: typing.Optional[str] = Field(None, alias='routing_number')

    account_type: typing.Optional[Literal["checking", "savings"]] = Field(None, alias='account_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
