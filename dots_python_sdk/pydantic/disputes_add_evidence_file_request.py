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


class DisputesAddEvidenceFileRequest(BaseModel):
    type: typing.Optional[Literal["customer_communications", "refund_policy", "cancellation_policy", "customer_signature", "receipt", "service_documentation", "duplicate_charge_documentation", "shipping_documentation", "uncategorized"]] = Field(None, alias='type')

    content: typing.Optional[str] = Field(None, alias='content')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
