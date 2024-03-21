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


RequiredUserCompliance = TypedDict("RequiredUserCompliance", {
    })

OptionalUserCompliance = TypedDict("OptionalUserCompliance", {
    "tax_id_collected": bool,

    "address_collected": bool,

    "date_of_birth_collected": bool,

    "must_collect_1099": bool,

    "1099_collected": bool,

    "w8_ben_collected": bool,

    "flagged": bool,

    "id_verified": bool,
    }, total=False)

class UserCompliance(RequiredUserCompliance, OptionalUserCompliance):
    pass
