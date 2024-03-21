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

from dots_python_sdk.type.payout_link_delivery import PayoutLinkDelivery
from dots_python_sdk.type.payout_link_payee import PayoutLinkPayee

class RequiredPayoutLink(TypedDict):
    pass

class OptionalPayoutLink(TypedDict, total=False):
    # ID of the `payout-link`.
    id: str

    # Date the `payout-link` was created.
    created: datetime

    # URL to access the `payout-link`.
    link: str

    # The amount to pay in cents.
    amount: typing.Union[int, float]

    # Status of the `payout-link`.
    status: str

    payee: PayoutLinkPayee

    delivery: PayoutLinkDelivery

    # Transfers marked as `tax_exempt` will not be counted towards the 1099 threshold.
    tax_exempt: bool

    # ID of the `user` that has claimed the `payout-link`.
    claimed_user_id: str

    # ID of the payout flow UI that is sent to the user.
    flow_id: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

class PayoutLink(RequiredPayoutLink, OptionalPayoutLink):
    pass
