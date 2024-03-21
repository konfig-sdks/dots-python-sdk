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


class RequiredBusinessComplianceInfoFlowOfFunds(TypedDict):
    # Flow of funds
    reasons: str

    # Description of the business
    usage: str

class OptionalBusinessComplianceInfoFlowOfFunds(TypedDict, total=False):
    pass

class BusinessComplianceInfoFlowOfFunds(RequiredBusinessComplianceInfoFlowOfFunds, OptionalBusinessComplianceInfoFlowOfFunds):
    pass
