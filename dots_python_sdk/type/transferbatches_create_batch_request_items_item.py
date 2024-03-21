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


class RequiredTransferbatchesCreateBatchRequestItemsItem(TypedDict):
    pass

class OptionalTransferbatchesCreateBatchRequestItemsItem(TypedDict, total=False):
    amount: int

    user_id: str

    tax_exempt: bool

    allow_debit: bool

    idempotency_key: str

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class TransferbatchesCreateBatchRequestItemsItem(RequiredTransferbatchesCreateBatchRequestItemsItem, OptionalTransferbatchesCreateBatchRequestItemsItem):
    pass
