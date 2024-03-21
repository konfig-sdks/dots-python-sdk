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

from dots_python_sdk.type.transferbatches_create_batch_request_items import TransferbatchesCreateBatchRequestItems

class RequiredTransferbatchesCreateBatchRequest(TypedDict):
    pass

class OptionalTransferbatchesCreateBatchRequest(TypedDict, total=False):
    items: TransferbatchesCreateBatchRequestItems

    idempotency_key: str

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class TransferbatchesCreateBatchRequest(RequiredTransferbatchesCreateBatchRequest, OptionalTransferbatchesCreateBatchRequest):
    pass
