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

from dots_python_sdk.type.checkoutsessions_create_session_request_line_items import CheckoutsessionsCreateSessionRequestLineItems

class RequiredCheckoutsessionsCreateSessionRequest(TypedDict):
    line_items: CheckoutsessionsCreateSessionRequestLineItems

    success_url: str

    mode: str

class OptionalCheckoutsessionsCreateSessionRequest(TypedDict, total=False):
    customer_email: str

    client_reference_id: str

    cancel_url: str

    # Supply a Dots user ID in place of a customer ID
    user_id: str

    customer_id: str

    expires_in: int

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class CheckoutsessionsCreateSessionRequest(RequiredCheckoutsessionsCreateSessionRequest, OptionalCheckoutsessionsCreateSessionRequest):
    pass
