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

from dots_python_sdk.pydantic.dispute_file import DisputeFile

class Dispute(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    payment_intent_id: typing.Optional[str] = Field(None, alias='payment_intent_id')

    status: typing.Optional[Literal["needs_response", "under_review", "closed", "warning_needs_response", "warning_under_review", "warning_closed", "won", "lost"]] = Field(None, alias='status')

    evidence: typing.Optional[typing.List[DisputeFile]] = Field(None, alias='evidence')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
