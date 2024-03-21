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

from dots_python_sdk.pydantic.transfer_batch_item import TransferBatchItem

class TransferbatchesCreateBatchResponse(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    status: typing.Optional[Literal["pending", "completed"]] = Field(None, alias='status')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    items: typing.Optional[typing.List[TransferBatchItem]] = Field(None, alias='items')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
