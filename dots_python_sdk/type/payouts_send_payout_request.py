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

from dots_python_sdk.type.payouts_send_payout_request_additional_steps import PayoutsSendPayoutRequestAdditionalSteps
from dots_python_sdk.type.payouts_send_payout_request_delivery import PayoutsSendPayoutRequestDelivery
from dots_python_sdk.type.payouts_send_payout_request_payee import PayoutsSendPayoutRequestPayee

class RequiredPayoutsSendPayoutRequest(TypedDict):
    # The amount in cents to pay the user.
    amount: int

class OptionalPayoutsSendPayoutRequest(TypedDict, total=False):
    # The user's id. `user_id` or `payee` is required.
    user_id: str

    payee: PayoutsSendPayoutRequestPayee

    delivery: PayoutsSendPayoutRequestDelivery

    # Collect 1099 or w8-ben information.
    force_collect_compliance_information: bool

    additional_steps: PayoutsSendPayoutRequestAdditionalSteps

    # Payouts marked as `tax_exempt` will not be counted towards the 1099 threshold.
    tax_exempt: bool

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Add a memo to the top of the Payout Link
    memo: str

    # Unique UUID key that prevents duplicate requests from being processed. If a payout link with the idempotency key exists, a new link will not be created and the existing link will be returned instead.
    idempotency_key: typing.Union[bool, date, datetime, dict, float, int, list, str, None]

    # Overrides the setting for which party will pay fees on this payout. This takes precedence over the default for your application.
    payout_fee_party: str

class PayoutsSendPayoutRequest(RequiredPayoutsSendPayoutRequest, OptionalPayoutsSendPayoutRequest):
    pass
