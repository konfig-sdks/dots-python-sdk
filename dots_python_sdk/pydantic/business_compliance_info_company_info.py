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


class BusinessComplianceInfoCompanyInfo(BaseModel):
    # Federal Employer Identification Number
    ein: str = Field(alias='ein')

    # Date of incorporation
    incorporation_date: date = Field(alias='incorporation_date')

    # State where incorporated
    incorporation_state: str = Field(alias='incorporation_state')

    # The legal classification of the company's incorporation
    incorporation_type: Literal["sole_proprietorship", "partnership", "llc", "c_corporation", "s_corporation"] = Field(alias='incorporation_type')

    # Company's legal name
    name: str = Field(alias='name')

    # Company web address
    website: str = Field(alias='website')

    # Company DBA (Doing Business As)
    dba: typing.Optional[str] = Field(None, alias='dba')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
