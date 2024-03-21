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


class RequiredUsersAddPayoutMethodRequest(TypedDict):
    # Payout platform to add.
    platform: str

class OptionalUsersAddPayoutMethodRequest(TypedDict, total=False):
    # Bank account or Cash App routing number. Required if `platform` = `ach` or `cash_app`.
    routing_number: str

    # Bank account or Cash App account number. Required if `platform` = `ach` or `cash_app`.
    account_number: str

    # Bank account type. Required if `platform` = `ach`.
    account_type: str

    # PayPal email address. Required if `platform` = `paypal`.
    email: str

    # Venmo phone number. One of `phone_number` or `handle` is required if `platform` = `venmo`.
    phone_number: str

    # Venmo handle. One of `phone_number` or `handle` is required if `platform` = `venmo`.
    handle: str

    # Cash App Cash Tag. Required if `platform` = `cash_app`.
    cash_tag: str

class UsersAddPayoutMethodRequest(RequiredUsersAddPayoutMethodRequest, OptionalUsersAddPayoutMethodRequest):
    pass
