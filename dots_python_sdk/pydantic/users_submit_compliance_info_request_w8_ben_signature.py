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


class UsersSubmitComplianceInfoRequestW8BenSignature(BaseModel):
    # The consent of the beneficial owner to the disclosure of their information to the IRS.
    consent: bool = Field(alias='consent')

    # The name of the person signing the form.
    name: str = Field(alias='name')

    # The email address of the person signing the form.
    email: str = Field(alias='email')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
