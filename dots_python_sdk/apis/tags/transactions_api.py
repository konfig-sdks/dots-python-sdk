# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from dots_python_sdk.paths.v2_transactions_transaction_id.get import GetById
from dots_python_sdk.paths.v2_transactions.get import ListAll
from dots_python_sdk.apis.tags.transactions_api_raw import TransactionsApiRaw


class TransactionsApi(
    GetById,
    ListAll,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TransactionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TransactionsApiRaw(api_client)
