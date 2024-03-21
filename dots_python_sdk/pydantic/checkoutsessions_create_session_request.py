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

from dots_python_sdk.pydantic.checkoutsessions_create_session_request_line_items import CheckoutsessionsCreateSessionRequestLineItems

class CheckoutsessionsCreateSessionRequest(BaseModel):
    line_items: CheckoutsessionsCreateSessionRequestLineItems = Field(alias='line_items')

    success_url: str = Field(alias='success_url')

    mode: Literal["payment"] = Field(alias='mode')

    customer_email: typing.Optional[str] = Field(None, alias='customer_email')

    client_reference_id: typing.Optional[str] = Field(None, alias='client_reference_id')

    cancel_url: typing.Optional[str] = Field(None, alias='cancel_url')

    # Supply a Dots user ID in place of a customer ID
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    customer_id: typing.Optional[str] = Field(None, alias='customer_id')

    expires_in: typing.Optional[int] = Field(None, alias='expires_in')

    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
