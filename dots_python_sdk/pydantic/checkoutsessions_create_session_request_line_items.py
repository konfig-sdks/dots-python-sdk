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

from dots_python_sdk.pydantic.checkoutsessions_create_session_request_line_items_item import CheckoutsessionsCreateSessionRequestLineItemsItem

CheckoutsessionsCreateSessionRequestLineItems = typing.List[CheckoutsessionsCreateSessionRequestLineItemsItem]
