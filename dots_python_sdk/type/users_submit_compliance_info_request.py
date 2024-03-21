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

from dots_python_sdk.type.users_submit_compliance_info_request_w8_ben import UsersSubmitComplianceInfoRequestW8Ben
from dots_python_sdk.type.users_submit_compliance_info_request_w9 import UsersSubmitComplianceInfoRequestW9

class RequiredUsersSubmitComplianceInfoRequest(TypedDict):
    pass

class OptionalUsersSubmitComplianceInfoRequest(TypedDict, total=False):
    w9: UsersSubmitComplianceInfoRequestW9

    w8ben: UsersSubmitComplianceInfoRequestW8Ben

class UsersSubmitComplianceInfoRequest(RequiredUsersSubmitComplianceInfoRequest, OptionalUsersSubmitComplianceInfoRequest):
    pass
