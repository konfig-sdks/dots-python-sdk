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


class RequiredBusinessComplianceInfoCompanyInfo(TypedDict):
    # Federal Employer Identification Number
    ein: str

    # Date of incorporation
    incorporation_date: date

    # State where incorporated
    incorporation_state: str

    # The legal classification of the company's incorporation
    incorporation_type: str

    # Company's legal name
    name: str

    # Company web address
    website: str

class OptionalBusinessComplianceInfoCompanyInfo(TypedDict, total=False):
    # Company DBA (Doing Business As)
    dba: str

class BusinessComplianceInfoCompanyInfo(RequiredBusinessComplianceInfoCompanyInfo, OptionalBusinessComplianceInfoCompanyInfo):
    pass
