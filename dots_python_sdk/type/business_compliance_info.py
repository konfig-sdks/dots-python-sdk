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

from dots_python_sdk.type.business_compliance_info_company_info import BusinessComplianceInfoCompanyInfo
from dots_python_sdk.type.business_compliance_info_contact_info import BusinessComplianceInfoContactInfo
from dots_python_sdk.type.business_compliance_info_directors import BusinessComplianceInfoDirectors
from dots_python_sdk.type.business_compliance_info_flow_of_funds import BusinessComplianceInfoFlowOfFunds

class RequiredBusinessComplianceInfo(TypedDict):
    company_info: BusinessComplianceInfoCompanyInfo

    contact_info: BusinessComplianceInfoContactInfo

    directors: BusinessComplianceInfoDirectors

    flow_of_funds: BusinessComplianceInfoFlowOfFunds

class OptionalBusinessComplianceInfo(TypedDict, total=False):
    pass

class BusinessComplianceInfo(RequiredBusinessComplianceInfo, OptionalBusinessComplianceInfo):
    pass
