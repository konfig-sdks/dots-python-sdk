import typing_extensions

from dots_python_sdk.apis.tags import TagValues
from dots_python_sdk.apis.tags.users_api import UsersApi
from dots_python_sdk.apis.tags.apps_api import AppsApi
from dots_python_sdk.apis.tags.transfers_api import TransfersApi
from dots_python_sdk.apis.tags.disputes_api import DisputesApi
from dots_python_sdk.apis.tags.payment_intents_api import PaymentIntentsApi
from dots_python_sdk.apis.tags.payment_methods_api import PaymentMethodsApi
from dots_python_sdk.apis.tags.payout_links_api import PayoutLinksApi
from dots_python_sdk.apis.tags.checkout_sessions_api import CheckoutSessionsApi
from dots_python_sdk.apis.tags.flows_api import FlowsApi
from dots_python_sdk.apis.tags.payment_customers_api import PaymentCustomersApi
from dots_python_sdk.apis.tags.payout_requests_api import PayoutRequestsApi
from dots_python_sdk.apis.tags.refunds_api import RefundsApi
from dots_python_sdk.apis.tags.transfer_batches_api import TransferBatchesApi
from dots_python_sdk.apis.tags.payouts_api import PayoutsApi
from dots_python_sdk.apis.tags.transactions_api import TransactionsApi
from dots_python_sdk.apis.tags.payments_api import PaymentsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.USERS: UsersApi,
        TagValues.APPS: AppsApi,
        TagValues.TRANSFERS: TransfersApi,
        TagValues.DISPUTES: DisputesApi,
        TagValues.PAYMENTINTENTS: PaymentIntentsApi,
        TagValues.PAYMENTMETHODS: PaymentMethodsApi,
        TagValues.PAYOUTLINKS: PayoutLinksApi,
        TagValues.CHECKOUTSESSIONS: CheckoutSessionsApi,
        TagValues.FLOWS: FlowsApi,
        TagValues.PAYMENTCUSTOMERS: PaymentCustomersApi,
        TagValues.PAYOUTREQUESTS: PayoutRequestsApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.TRANSFERBATCHES: TransferBatchesApi,
        TagValues.PAYOUTS: PayoutsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.PAYMENTS: PaymentsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.USERS: UsersApi,
        TagValues.APPS: AppsApi,
        TagValues.TRANSFERS: TransfersApi,
        TagValues.DISPUTES: DisputesApi,
        TagValues.PAYMENTINTENTS: PaymentIntentsApi,
        TagValues.PAYMENTMETHODS: PaymentMethodsApi,
        TagValues.PAYOUTLINKS: PayoutLinksApi,
        TagValues.CHECKOUTSESSIONS: CheckoutSessionsApi,
        TagValues.FLOWS: FlowsApi,
        TagValues.PAYMENTCUSTOMERS: PaymentCustomersApi,
        TagValues.PAYOUTREQUESTS: PayoutRequestsApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.TRANSFERBATCHES: TransferBatchesApi,
        TagValues.PAYOUTS: PayoutsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.PAYMENTS: PaymentsApi,
    }
)
