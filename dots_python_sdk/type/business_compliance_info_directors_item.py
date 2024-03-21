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

from dots_python_sdk.type.business_compliance_info_directors_item_address import BusinessComplianceInfoDirectorsItemAddress

class RequiredBusinessComplianceInfoDirectorsItem(TypedDict):
    # Employee title or ownership role
    title: str

    address: BusinessComplianceInfoDirectorsItemAddress

    # Date of birth
    dob: date

    # Contact email, needs to be verifiable
    email: str

    first_name: str

    last_name: str

    # Percentage of company owned by this person
    ownership_percentage: typing.Union[int, float]

    phone: str

class OptionalBusinessComplianceInfoDirectorsItem(TypedDict, total=False):
    pass

class BusinessComplianceInfoDirectorsItem(RequiredBusinessComplianceInfoDirectorsItem, OptionalBusinessComplianceInfoDirectorsItem):
    pass
