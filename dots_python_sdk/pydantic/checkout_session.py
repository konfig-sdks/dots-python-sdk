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

from dots_python_sdk.pydantic.checkout_session_line_items import CheckoutSessionLineItems

class CheckoutSession(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    status: typing.Optional[Literal["open", "complete", "expired"]] = Field(None, alias='status')

    payment_intent_id: typing.Optional[str] = Field(None, alias='payment_intent_id')

    success_url: typing.Optional[str] = Field(None, alias='success_url')

    cancel_url: typing.Optional[str] = Field(None, alias='cancel_url')

    checkout_session_url: typing.Optional[str] = Field(None, alias='checkout_session_url')

    client_reference_id: typing.Optional[str] = Field(None, alias='client_reference_id')

    expiry: typing.Optional[datetime] = Field(None, alias='expiry')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    line_items: typing.Optional[CheckoutSessionLineItems] = Field(None, alias='line_items')

    created: typing.Optional[datetime] = Field(None, alias='created')

    updated: typing.Optional[datetime] = Field(None, alias='updated')

    # `payment-customer` ID
    customer_id: typing.Optional[str] = Field(None, alias='customer_id')

    customer_email: typing.Optional[str] = Field(None, alias='customer_email')

    amount_total: typing.Optional[int] = Field(None, alias='amount_total')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
