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


class PaymentIntent(BaseModel):
    id: str = Field(alias='id')

    # Amount in cents
    amount: int = Field(alias='amount')

    currency: Literal["usd"] = Field(alias='currency')

    user_id: typing.Optional[str] = Field(None, alias='user_id')

    status: typing.Optional[Literal["initialized", "created", "requires_payment_method", "requires_confirmation", "requires_action", "processing", "succeeded", "requires_capture", "canceled", "failed"]] = Field(None, alias='status')

    transfer_id: typing.Optional[str] = Field(None, alias='transfer_id')

    payment_method_id: typing.Optional[str] = Field(None, alias='payment_method_id')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    # Only availble on payment intent creation.
    client_secret: typing.Optional[str] = Field(None, alias='client_secret')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
