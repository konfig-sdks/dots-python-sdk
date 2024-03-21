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

from dots_python_sdk.type.transfer_batch_item import TransferBatchItem

class RequiredTransferbatchesGetByIdResponse(TypedDict):
    pass

class OptionalTransferbatchesGetByIdResponse(TypedDict, total=False):
    id: str

    status: str

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    items: typing.List[TransferBatchItem]

class TransferbatchesGetByIdResponse(RequiredTransferbatchesGetByIdResponse, OptionalTransferbatchesGetByIdResponse):
    pass
