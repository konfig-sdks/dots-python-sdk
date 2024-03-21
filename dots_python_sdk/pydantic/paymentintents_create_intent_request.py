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

from dots_python_sdk.pydantic.paymentintents_create_intent_request_payment_method_types import PaymentintentsCreateIntentRequestPaymentMethodTypes
from dots_python_sdk.pydantic.paymentintents_create_intent_request_transfer_data import PaymentintentsCreateIntentRequestTransferData

class PaymentintentsCreateIntentRequest(BaseModel):
    # Amount in cents
    amount: int = Field(alias='amount')

    # Currency of the payment. Currently only `usd` is supported.
    currency: Literal["usd"] = Field(alias='currency')

    # An arbitrary string attached to the object. Often useful for displaying to users.
    description: typing.Optional[str] = Field(None, alias='description')

    # Set to `true` to attempt to confirm this payment intent immediately. Defaults to `false`.
    confirm: typing.Optional[bool] = Field(None, alias='confirm')

    # ID of a Dots `user` making this payment.
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    # ID of a Dots `payment_customer` making this payment.
    customer_id: typing.Optional[str] = Field(None, alias='customer_id')

    # ID of the payment method to attach to this payment intent.
    payment_method_id: typing.Optional[str] = Field(None, alias='payment_method_id')

    payment_method_types: typing.Optional[PaymentintentsCreateIntentRequestPaymentMethodTypes] = Field(None, alias='payment_method_types')

    setup_future_usage: typing.Optional[Literal["on_session"]] = Field(None, alias='setup_future_usage')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[bool] = Field(None, alias='metadata')

    transfer_data: typing.Optional[PaymentintentsCreateIntentRequestTransferData] = Field(None, alias='transfer_data')

    # Amount in cents to transfer to the application's wallet as a platform fee.
    application_fee_amount: typing.Optional[int] = Field(None, alias='application_fee_amount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
