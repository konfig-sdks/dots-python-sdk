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

from dots_python_sdk.pydantic.business_compliance_info_directors_item_address import BusinessComplianceInfoDirectorsItemAddress

class BusinessComplianceInfoDirectorsItem(BaseModel):
    # Employee title or ownership role
    title: str = Field(alias='title')

    address: BusinessComplianceInfoDirectorsItemAddress = Field(alias='address')

    # Date of birth
    dob: date = Field(alias='dob')

    # Contact email, needs to be verifiable
    email: str = Field(alias='email')

    first_name: str = Field(alias='first_name')

    last_name: str = Field(alias='last_name')

    # Percentage of company owned by this person
    ownership_percentage: typing.Union[int, float] = Field(alias='ownership_percentage')

    phone: str = Field(alias='phone')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
