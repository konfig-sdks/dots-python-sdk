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


class RequiredBusinessComplianceInfoContactInfo(TypedDict):
    city: str

    # Country name or country code
    country: str

    # Primary contact email address. Service emails will be sent to this address.
    email: str

    # Address line 1
    line1: str

    phone_number: str

    # State when applicable
    state: str

    # ZIP or postal code
    zip: str

class OptionalBusinessComplianceInfoContactInfo(TypedDict, total=False):
    # Address line 2
    line2: str

class BusinessComplianceInfoContactInfo(RequiredBusinessComplianceInfoContactInfo, OptionalBusinessComplianceInfoContactInfo):
    pass
