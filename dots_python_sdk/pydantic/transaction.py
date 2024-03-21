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


class Transaction(BaseModel):
    id: typing.Optional[int] = Field(None, alias='id')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    created: typing.Optional[datetime] = Field(None, alias='created')

    source_name: typing.Optional[str] = Field(None, alias='source_name')

    destination_name: typing.Optional[str] = Field(None, alias='destination_name')

    # The general category of the transaction
    type: typing.Optional[Literal["balance", "refill", "payout", "payment", "fee", "surrogate"]] = Field(None, alias='type')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
