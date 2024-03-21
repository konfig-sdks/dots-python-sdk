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

from dots_python_sdk.pydantic.transaction import Transaction
from dots_python_sdk.pydantic.transfer_external_data import TransferExternalData

class Transfer(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    created: typing.Optional[datetime] = Field(None, alias='created')

    user_id: typing.Optional[str] = Field(None, alias='user_id')

    status: typing.Optional[Literal["created", "pending", "failed", "completed", "flagged"]] = Field(None, alias='status')

    type: typing.Optional[Literal["refill", "payout", "balance"]] = Field(None, alias='type')

    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    external_data: typing.Optional[TransferExternalData] = Field(None, alias='external_data')

    transactions: typing.Optional[typing.List[Transaction]] = Field(None, alias='transactions')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
