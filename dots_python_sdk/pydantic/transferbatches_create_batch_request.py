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

from dots_python_sdk.pydantic.transferbatches_create_batch_request_items import TransferbatchesCreateBatchRequestItems

class TransferbatchesCreateBatchRequest(BaseModel):
    items: typing.Optional[TransferbatchesCreateBatchRequestItems] = Field(None, alias='items')

    idempotency_key: typing.Optional[str] = Field(None, alias='idempotency_key')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
