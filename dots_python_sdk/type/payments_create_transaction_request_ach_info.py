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


class RequiredPaymentsCreateTransactionRequestAchInfo(TypedDict):
    pass

class OptionalPaymentsCreateTransactionRequestAchInfo(TypedDict, total=False):
    account_number: str

    routing_number: str

    account_type: str

class PaymentsCreateTransactionRequestAchInfo(RequiredPaymentsCreateTransactionRequestAchInfo, OptionalPaymentsCreateTransactionRequestAchInfo):
    pass
