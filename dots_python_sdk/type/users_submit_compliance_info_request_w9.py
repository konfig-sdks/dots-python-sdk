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

from dots_python_sdk.type.users_submit_compliance_info_request_w9_address import UsersSubmitComplianceInfoRequestW9Address

class RequiredUsersSubmitComplianceInfoRequestW9(TypedDict):
    # Type of entity filling out the W-9, `business` or `individual`.
    entity_type: str

    # Required if `entity_type` is `individual`.
    date_of_birth: date

    # SSN if `entity_type` is `individual`. EIN if `entity_type` is `business`.
    tin: str

    address: UsersSubmitComplianceInfoRequestW9Address

class OptionalUsersSubmitComplianceInfoRequestW9(TypedDict, total=False):
    # Legal bussiness name. Required if `entity_type` is `business`.
    business_name: str

    first_name: str

    last_name: str

class UsersSubmitComplianceInfoRequestW9(RequiredUsersSubmitComplianceInfoRequestW9, OptionalUsersSubmitComplianceInfoRequestW9):
    pass
