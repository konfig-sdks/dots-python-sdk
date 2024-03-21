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

from dots_python_sdk.pydantic.payout_link_delivery import PayoutLinkDelivery
from dots_python_sdk.pydantic.payout_link_payee import PayoutLinkPayee

class PayoutLink(BaseModel):
    # ID of the `payout-link`.
    id: typing.Optional[str] = Field(None, alias='id')

    # Date the `payout-link` was created.
    created: typing.Optional[datetime] = Field(None, alias='created')

    # URL to access the `payout-link`.
    link: typing.Optional[str] = Field(None, alias='link')

    # The amount to pay in cents.
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Status of the `payout-link`.
    status: typing.Optional[Literal["sent", "claimed", "delivery_pending", "delivery_failed", "delivered", "canceled"]] = Field(None, alias='status')

    payee: typing.Optional[PayoutLinkPayee] = Field(None, alias='payee')

    delivery: typing.Optional[PayoutLinkDelivery] = Field(None, alias='delivery')

    # Transfers marked as `tax_exempt` will not be counted towards the 1099 threshold.
    tax_exempt: typing.Optional[bool] = Field(None, alias='tax_exempt')

    # ID of the `user` that has claimed the `payout-link`.
    claimed_user_id: typing.Optional[str] = Field(None, alias='claimed_user_id')

    # ID of the payout flow UI that is sent to the user.
    flow_id: typing.Optional[str] = Field(None, alias='flow_id')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
