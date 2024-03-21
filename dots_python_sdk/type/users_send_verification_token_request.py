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


class RequiredUsersSendVerificationTokenRequest(TypedDict):
    pass

class OptionalUsersSendVerificationTokenRequest(TypedDict, total=False):
    # Defaults to `false` which sends token via SMS. Set `true` to receive via call instead.
    use_voice: bool

class UsersSendVerificationTokenRequest(RequiredUsersSendVerificationTokenRequest, OptionalUsersSendVerificationTokenRequest):
    pass
