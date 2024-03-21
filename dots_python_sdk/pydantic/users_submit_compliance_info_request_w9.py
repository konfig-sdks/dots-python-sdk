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

from dots_python_sdk.pydantic.users_submit_compliance_info_request_w9_address import UsersSubmitComplianceInfoRequestW9Address

class UsersSubmitComplianceInfoRequestW9(BaseModel):
    # Type of entity filling out the W-9, `business` or `individual`.
    entity_type: Literal["individual", "business"] = Field(alias='entity_type')

    # Required if `entity_type` is `individual`.
    date_of_birth: date = Field(alias='date_of_birth')

    # SSN if `entity_type` is `individual`. EIN if `entity_type` is `business`.
    tin: str = Field(alias='tin')

    address: UsersSubmitComplianceInfoRequestW9Address = Field(alias='address')

    # Legal bussiness name. Required if `entity_type` is `business`.
    business_name: typing.Optional[str] = Field(None, alias='business_name')

    first_name: typing.Optional[str] = Field(None, alias='first_name')

    last_name: typing.Optional[str] = Field(None, alias='last_name')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
