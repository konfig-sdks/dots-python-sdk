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

from dots_python_sdk.pydantic.business_compliance_info_company_info import BusinessComplianceInfoCompanyInfo
from dots_python_sdk.pydantic.business_compliance_info_contact_info import BusinessComplianceInfoContactInfo
from dots_python_sdk.pydantic.business_compliance_info_directors import BusinessComplianceInfoDirectors
from dots_python_sdk.pydantic.business_compliance_info_flow_of_funds import BusinessComplianceInfoFlowOfFunds

class BusinessComplianceInfo(BaseModel):
    company_info: BusinessComplianceInfoCompanyInfo = Field(alias='company_info')

    contact_info: BusinessComplianceInfoContactInfo = Field(alias='contact_info')

    directors: BusinessComplianceInfoDirectors = Field(alias='directors')

    flow_of_funds: BusinessComplianceInfoFlowOfFunds = Field(alias='flow_of_funds')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
