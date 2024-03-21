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


class RequiredAppsWithdrawFundsRequest(TypedDict):
    # The amount to deposit in cents.
    amount: int

class OptionalAppsWithdrawFundsRequest(TypedDict, total=False):
    # Idempotency key in UUID format.
    idempotency_key: str

class AppsWithdrawFundsRequest(RequiredAppsWithdrawFundsRequest, OptionalAppsWithdrawFundsRequest):
    pass
