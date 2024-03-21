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


class RequiredAppMetrics(TypedDict):
    wallet_balance: str

    money_out: str

    connected_users: int

class OptionalAppMetrics(TypedDict, total=False):
    pass

class AppMetrics(RequiredAppMetrics, OptionalAppMetrics):
    pass
