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

from dots_python_sdk.pydantic.payout_link import PayoutLink
from dots_python_sdk.pydantic.payout_request_payee import PayoutRequestPayee
from dots_python_sdk.pydantic.user import User

class PayoutRequest(BaseModel):
    # ID of the `payout-request`.
    id: typing.Optional[str] = Field(None, alias='id')

    # Date that the `payout-request` was created.
    created: typing.Optional[datetime] = Field(None, alias='created')

    # Amount in cents of the `payout-request`.
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Status of the `payout-request`.
    status: typing.Optional[Literal["created", "approved", "rejected"]] = Field(None, alias='status')

    payee: typing.Optional[PayoutRequestPayee] = Field(None, alias='payee')

    payout-link_: typing.Optional[PayoutLink] = Field(None, alias='payout-link')

    user: typing.Optional[User] = Field(None, alias='user')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    memo: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='memo')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
