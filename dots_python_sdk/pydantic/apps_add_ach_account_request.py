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


class AppsAddAchAccountRequest(BaseModel):
    # The bank account number.
    account_number: str = Field(alias='account_number')

    # The bank's ABA routing number.
    routing_number: str = Field(alias='routing_number')

    # The type of bank account.
    account_type: Literal["checking", "savings"] = Field(alias='account_type')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
