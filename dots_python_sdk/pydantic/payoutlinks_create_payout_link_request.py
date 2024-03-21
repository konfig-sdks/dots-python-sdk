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

from dots_python_sdk.pydantic.payoutlinks_create_payout_link_request_additional_steps import PayoutlinksCreatePayoutLinkRequestAdditionalSteps
from dots_python_sdk.pydantic.payoutlinks_create_payout_link_request_delivery import PayoutlinksCreatePayoutLinkRequestDelivery
from dots_python_sdk.pydantic.payoutlinks_create_payout_link_request_payee import PayoutlinksCreatePayoutLinkRequestPayee

class PayoutlinksCreatePayoutLinkRequest(BaseModel):
    # Amount to be paid in cents.
    amount: int = Field(alias='amount')

    # The user's id.
    user_id: typing.Optional[str] = Field(None, alias='user_id')

    payee: typing.Optional[PayoutlinksCreatePayoutLinkRequestPayee] = Field(None, alias='payee')

    delivery: typing.Optional[PayoutlinksCreatePayoutLinkRequestDelivery] = Field(None, alias='delivery')

    # Force the collection of 1099 or W-8 information. Defaults to `false`.
    force_collect_compliance_information: typing.Optional[bool] = Field(None, alias='force_collect_compliance_information')

    # Payout links marked as `tax_exempt` will not be counted towards the 1099 threshold.
    tax_exempt: typing.Optional[bool] = Field(None, alias='tax_exempt')

    # Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='metadata')

    # Add a memo to the top of the Payout Link
    memo: typing.Optional[str] = Field(None, alias='memo')

    # Unique UUID key that prevents duplicate requests from being processed. If a payout link with the idempotency key exists, a new link will not be created and the existing link will be returned instead.
    idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='idempotency_key')

    # Overrides the setting for which party will pay fees on this payout. This takes precedence over the default for your application.
    payout_fee_party: typing.Optional[Literal["user", "platform"]] = Field(None, alias='payout_fee_party')

    additional_steps: typing.Optional[PayoutlinksCreatePayoutLinkRequestAdditionalSteps] = Field(None, alias='additional_steps')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
