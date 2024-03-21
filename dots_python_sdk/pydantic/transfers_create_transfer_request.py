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


class TransfersCreateTransferRequest(BaseModel):
    # The amount in cents to transfer. Negative amount transfers money from the `app` to the `user`.
    amount: int = Field(alias='amount')

    # The user's id.
    user_id: str = Field(alias='user_id')

    # Transfers marked as `tax_exempt` will not be counted towards the 1099 threshold.
    tax_exempt: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='tax_exempt')

    # UUID that will be used to idempotently handle requests. Transfers with existing idempotency keys will be rejected.
    idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='idempotency_key')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
