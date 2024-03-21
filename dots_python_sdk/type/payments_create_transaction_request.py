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

from dots_python_sdk.type.payments_create_transaction_request_ach_info import PaymentsCreateTransactionRequestAchInfo

class RequiredPaymentsCreateTransactionRequest(TypedDict):
    amount: int

    platform: str

class OptionalPaymentsCreateTransactionRequest(TypedDict, total=False):
    user_id: str

    customer_id: str

    ach_info: PaymentsCreateTransactionRequestAchInfo

    # The user's ACH account ID.
    account_id: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class PaymentsCreateTransactionRequest(RequiredPaymentsCreateTransactionRequest, OptionalPaymentsCreateTransactionRequest):
    pass
PaymentsCreateTransactionRequest = typing.Union[typing.Union[bool, date, datetime, dict, float, int, list, str, None],typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
