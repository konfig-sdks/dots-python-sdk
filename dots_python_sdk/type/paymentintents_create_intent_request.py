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

from dots_python_sdk.type.paymentintents_create_intent_request_payment_method_types import PaymentintentsCreateIntentRequestPaymentMethodTypes
from dots_python_sdk.type.paymentintents_create_intent_request_transfer_data import PaymentintentsCreateIntentRequestTransferData

class RequiredPaymentintentsCreateIntentRequest(TypedDict):
    # Amount in cents
    amount: int

    # Currency of the payment. Currently only `usd` is supported.
    currency: str

class OptionalPaymentintentsCreateIntentRequest(TypedDict, total=False):
    # An arbitrary string attached to the object. Often useful for displaying to users.
    description: str

    # Set to `true` to attempt to confirm this payment intent immediately. Defaults to `false`.
    confirm: bool

    # ID of a Dots `user` making this payment.
    user_id: str

    # ID of a Dots `payment_customer` making this payment.
    customer_id: str

    # ID of the payment method to attach to this payment intent.
    payment_method_id: str

    payment_method_types: PaymentintentsCreateIntentRequestPaymentMethodTypes

    setup_future_usage: str

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: bool

    transfer_data: PaymentintentsCreateIntentRequestTransferData

    # Amount in cents to transfer to the application's wallet as a platform fee.
    application_fee_amount: int

class PaymentintentsCreateIntentRequest(RequiredPaymentintentsCreateIntentRequest, OptionalPaymentintentsCreateIntentRequest):
    pass
