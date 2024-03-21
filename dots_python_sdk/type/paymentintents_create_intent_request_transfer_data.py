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


class RequiredPaymentintentsCreateIntentRequestTransferData(TypedDict):
    pass

class OptionalPaymentintentsCreateIntentRequestTransferData(TypedDict, total=False):
    # The destination user to send the funds to. This is `amount` - transactions fees - `application_fee`.
    destination_user_id: str

class PaymentintentsCreateIntentRequestTransferData(RequiredPaymentintentsCreateIntentRequestTransferData, OptionalPaymentintentsCreateIntentRequestTransferData):
    pass
