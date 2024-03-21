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


class RequiredPayoutLinkPayee(TypedDict):
    pass

class OptionalPayoutLinkPayee(TypedDict, total=False):
    # Payee's first name.
    first_name: str

    # Payee's last name.
    last_name: str

    # Payee's email address.
    email: str

    # Country code of the payee's phone number e.g. \"1\" for USA.
    country_code: str

    # Rest of the payee's phone number.
    phone_number: str

class PayoutLinkPayee(RequiredPayoutLinkPayee, OptionalPayoutLinkPayee):
    pass
