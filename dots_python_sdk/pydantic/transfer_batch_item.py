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


class TransferBatchItem(BaseModel):
    transfer_id: typing.Optional[str] = Field(None, alias='transfer_id')

    amount: typing.Optional[int] = Field(None, alias='amount')

    user_id: typing.Optional[str] = Field(None, alias='user_id')

    tax_exempt: typing.Optional[bool] = Field(None, alias='tax_exempt')

    allow_debit: typing.Optional[bool] = Field(None, alias='allow_debit')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    error: typing.Optional[str] = Field(None, alias='error')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
