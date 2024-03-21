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

from dots_python_sdk.pydantic.payments_create_transaction_request_ach_info import PaymentsCreateTransactionRequestAchInfo

class PaymentsCreateTransactionRequest(BaseModel):
    amount: int = Field(alias='amount')

    platform: Literal["ach"] = Field(alias='platform')

    user_id: typing.Optional[str] = Field(None, alias='user_id')

    customer_id: typing.Optional[str] = Field(None, alias='customer_id')

    ach_info: typing.Optional[PaymentsCreateTransactionRequestAchInfo] = Field(None, alias='ach_info')

    # The user's ACH account ID.
    account_id: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='account_id')

    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
PaymentsCreateTransactionRequest = typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None],typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
