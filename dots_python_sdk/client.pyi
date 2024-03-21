# coding: utf-8
"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

import typing
import inspect
from datetime import date, datetime
from dots_python_sdk.client_custom import ClientCustom
from dots_python_sdk.configuration import Configuration
from dots_python_sdk.api_client import ApiClient
from dots_python_sdk.type_util import copy_signature
from dots_python_sdk.apis.tags.apps_api import AppsApi
from dots_python_sdk.apis.tags.checkout_sessions_api import CheckoutSessionsApi
from dots_python_sdk.apis.tags.disputes_api import DisputesApi
from dots_python_sdk.apis.tags.flows_api import FlowsApi
from dots_python_sdk.apis.tags.payment_customers_api import PaymentCustomersApi
from dots_python_sdk.apis.tags.payment_intents_api import PaymentIntentsApi
from dots_python_sdk.apis.tags.payment_methods_api import PaymentMethodsApi
from dots_python_sdk.apis.tags.payments_api import PaymentsApi
from dots_python_sdk.apis.tags.payout_links_api import PayoutLinksApi
from dots_python_sdk.apis.tags.payout_requests_api import PayoutRequestsApi
from dots_python_sdk.apis.tags.payouts_api import PayoutsApi
from dots_python_sdk.apis.tags.refunds_api import RefundsApi
from dots_python_sdk.apis.tags.transactions_api import TransactionsApi
from dots_python_sdk.apis.tags.transfer_batches_api import TransferBatchesApi
from dots_python_sdk.apis.tags.transfers_api import TransfersApi
from dots_python_sdk.apis.tags.users_api import UsersApi



class Dots(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.apps: AppsApi = AppsApi(api_client)
        self.checkout_sessions: CheckoutSessionsApi = CheckoutSessionsApi(api_client)
        self.disputes: DisputesApi = DisputesApi(api_client)
        self.flows: FlowsApi = FlowsApi(api_client)
        self.payment_customers: PaymentCustomersApi = PaymentCustomersApi(api_client)
        self.payment_intents: PaymentIntentsApi = PaymentIntentsApi(api_client)
        self.payment_methods: PaymentMethodsApi = PaymentMethodsApi(api_client)
        self.payments: PaymentsApi = PaymentsApi(api_client)
        self.payout_links: PayoutLinksApi = PayoutLinksApi(api_client)
        self.payout_requests: PayoutRequestsApi = PayoutRequestsApi(api_client)
        self.payouts: PayoutsApi = PayoutsApi(api_client)
        self.refunds: RefundsApi = RefundsApi(api_client)
        self.transactions: TransactionsApi = TransactionsApi(api_client)
        self.transfer_batches: TransferBatchesApi = TransferBatchesApi(api_client)
        self.transfers: TransfersApi = TransfersApi(api_client)
        self.users: UsersApi = UsersApi(api_client)
