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


class RequiredPayoutlinksCreatePayoutLinkRequestDelivery(TypedDict):
    pass

class OptionalPayoutlinksCreatePayoutLinkRequestDelivery(TypedDict, total=False):
    # Message to send in the sms message that is sent to the payee.
    message: str

    # Delivery method. `sms` requires `payee.country_code` and `payee.phone_number`, `email` required `payee.email`. `all` will deliver to all the methods supplied in the payee object (e.g., `all` with empty `payee` has the same effect as `link`, and `all` with `payee.email` has the same effect as `email`).
    method: str

class PayoutlinksCreatePayoutLinkRequestDelivery(RequiredPayoutlinksCreatePayoutLinkRequestDelivery, OptionalPayoutlinksCreatePayoutLinkRequestDelivery):
    pass
