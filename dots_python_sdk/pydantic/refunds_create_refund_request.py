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


class RefundsCreateRefundRequest(BaseModel):
    # Amount in cents
    amount: int = Field(alias='amount')

    # ID of the `payment_intent` you are refunding.
    payment_intent_id: str = Field(alias='payment_intent_id')

    reason: typing.Optional[Literal["duplicate", "fraudulent", "requested_by_customer", "expired_uncaptured_charge", "partial_capture"]] = Field(None, alias='reason')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[bool] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
