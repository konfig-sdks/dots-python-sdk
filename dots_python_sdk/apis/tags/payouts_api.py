# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from dots_python_sdk.paths.v2_payouts.post import CreatePayout
from dots_python_sdk.paths.v2_payouts_send_payout.post import SendPayout
from dots_python_sdk.apis.tags.payouts_api_raw import PayoutsApiRaw


class PayoutsApi(
    CreatePayout,
    SendPayout,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: PayoutsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = PayoutsApiRaw(api_client)
