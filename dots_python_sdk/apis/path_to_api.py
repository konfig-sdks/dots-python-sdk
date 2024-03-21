import typing_extensions

from dots_python_sdk.paths import PathValues
from dots_python_sdk.apis.paths.v2_users import V2Users
from dots_python_sdk.apis.paths.v2_users_user_id import V2UsersUserId
from dots_python_sdk.apis.paths.v2_users_user_id_compliance import V2UsersUserIdCompliance
from dots_python_sdk.apis.paths.v2_users_user_id_send_verification_token import V2UsersUserIdSendVerificationToken
from dots_python_sdk.apis.paths.v2_users_user_id_verify import V2UsersUserIdVerify
from dots_python_sdk.apis.paths.v2_users_user_id_payout_methods import V2UsersUserIdPayoutMethods
from dots_python_sdk.apis.paths.v2_transfers import V2Transfers
from dots_python_sdk.apis.paths.v2_transfers_transfer_id import V2TransfersTransferId
from dots_python_sdk.apis.paths.v2_flows import V2Flows
from dots_python_sdk.apis.paths.v2_flows_flow_id import V2FlowsFlowId
from dots_python_sdk.apis.paths.v2_payout_links import V2PayoutLinks
from dots_python_sdk.apis.paths.v2_payout_links_payout_link_id import V2PayoutLinksPayoutLinkId
from dots_python_sdk.apis.paths.v2_payouts import V2Payouts
from dots_python_sdk.apis.paths.v2_payments import V2Payments
from dots_python_sdk.apis.paths.v2_payouts_send_payout import V2PayoutsSendPayout
from dots_python_sdk.apis.paths.v2_payout_requests import V2PayoutRequests
from dots_python_sdk.apis.paths.v2_payout_requests_payout_request_id import V2PayoutRequestsPayoutRequestId
from dots_python_sdk.apis.paths.v2_transactions import V2Transactions
from dots_python_sdk.apis.paths.v2_transactions_transaction_id import V2TransactionsTransactionId
from dots_python_sdk.apis.paths.v2_payment_intents import V2PaymentIntents
from dots_python_sdk.apis.paths.v2_payment_intents_payment_intent_id import V2PaymentIntentsPaymentIntentId
from dots_python_sdk.apis.paths.v2_payment_intents_payment_intent_id_confirm import V2PaymentIntentsPaymentIntentIdConfirm
from dots_python_sdk.apis.paths.v2_transfer_batches import V2TransferBatches
from dots_python_sdk.apis.paths.v2_transfer_batches_transfer_batch_id import V2TransferBatchesTransferBatchId
from dots_python_sdk.apis.paths.v2_payment_customers import V2PaymentCustomers
from dots_python_sdk.apis.paths.v2_payment_customers_payment_customer_id import V2PaymentCustomersPaymentCustomerId
from dots_python_sdk.apis.paths.v2_checkout_sessions import V2CheckoutSessions
from dots_python_sdk.apis.paths.v2_checkout_sessions_checkout_session_id import V2CheckoutSessionsCheckoutSessionId
from dots_python_sdk.apis.paths.v2_apps import V2Apps
from dots_python_sdk.apis.paths.v2_apps_app_id import V2AppsAppId
from dots_python_sdk.apis.paths.v2_apps_app_id_compliance import V2AppsAppIdCompliance
from dots_python_sdk.apis.paths.v2_apps_app_id_ach_account import V2AppsAppIdAchAccount
from dots_python_sdk.apis.paths.v2_apps_app_id_deposit import V2AppsAppIdDeposit
from dots_python_sdk.apis.paths.v2_apps_app_id_withdraw import V2AppsAppIdWithdraw
from dots_python_sdk.apis.paths.v2_payment_methods import V2PaymentMethods
from dots_python_sdk.apis.paths.v2_payment_methods_payment_method_id import V2PaymentMethodsPaymentMethodId
from dots_python_sdk.apis.paths.v2_payment_methods_payment_method_id_attach import V2PaymentMethodsPaymentMethodIdAttach
from dots_python_sdk.apis.paths.v2_payment_methods_payment_method_id_detach import V2PaymentMethodsPaymentMethodIdDetach
from dots_python_sdk.apis.paths.v2_disputes import V2Disputes
from dots_python_sdk.apis.paths.v2_disputes_dispute_id import V2DisputesDisputeId
from dots_python_sdk.apis.paths.v2_disputes_dispute_id_evidence import V2DisputesDisputeIdEvidence
from dots_python_sdk.apis.paths.v2_disputes_dispute_id_submit import V2DisputesDisputeIdSubmit
from dots_python_sdk.apis.paths.v2_refunds import V2Refunds
from dots_python_sdk.apis.paths.v2_refunds_refund_id import V2RefundsRefundId
from dots_python_sdk.apis.paths.v2_organization_transfers import V2OrganizationTransfers
from dots_python_sdk.apis.paths.v2_organization_transfers_transfer_id import V2OrganizationTransfersTransferId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_USERS: V2Users,
        PathValues.V2_USERS_USER_ID: V2UsersUserId,
        PathValues.V2_USERS_USER_ID_COMPLIANCE: V2UsersUserIdCompliance,
        PathValues.V2_USERS_USER_ID_SENDVERIFICATIONTOKEN: V2UsersUserIdSendVerificationToken,
        PathValues.V2_USERS_USER_ID_VERIFY: V2UsersUserIdVerify,
        PathValues.V2_USERS_USER_ID_PAYOUTMETHODS: V2UsersUserIdPayoutMethods,
        PathValues.V2_TRANSFERS: V2Transfers,
        PathValues.V2_TRANSFERS_TRANSFER_ID: V2TransfersTransferId,
        PathValues.V2_FLOWS: V2Flows,
        PathValues.V2_FLOWS_FLOW_ID: V2FlowsFlowId,
        PathValues.V2_PAYOUTLINKS: V2PayoutLinks,
        PathValues.V2_PAYOUTLINKS_PAYOUT_LINK_ID: V2PayoutLinksPayoutLinkId,
        PathValues.V2_PAYOUTS: V2Payouts,
        PathValues.V2_PAYMENTS: V2Payments,
        PathValues.V2_PAYOUTS_SENDPAYOUT: V2PayoutsSendPayout,
        PathValues.V2_PAYOUTREQUESTS: V2PayoutRequests,
        PathValues.V2_PAYOUTREQUESTS_PAYOUT_REQUEST_ID: V2PayoutRequestsPayoutRequestId,
        PathValues.V2_TRANSACTIONS: V2Transactions,
        PathValues.V2_TRANSACTIONS_TRANSACTION_ID: V2TransactionsTransactionId,
        PathValues.V2_PAYMENTINTENTS: V2PaymentIntents,
        PathValues.V2_PAYMENTINTENTS_PAYMENT_INTENT_ID: V2PaymentIntentsPaymentIntentId,
        PathValues.V2_PAYMENTINTENTS_PAYMENT_INTENT_ID_CONFIRM: V2PaymentIntentsPaymentIntentIdConfirm,
        PathValues.V2_TRANSFERBATCHES: V2TransferBatches,
        PathValues.V2_TRANSFERBATCHES_TRANSFER_BATCH_ID: V2TransferBatchesTransferBatchId,
        PathValues.V2_PAYMENTCUSTOMERS: V2PaymentCustomers,
        PathValues.V2_PAYMENTCUSTOMERS_PAYMENT_CUSTOMER_ID: V2PaymentCustomersPaymentCustomerId,
        PathValues.V2_CHECKOUTSESSIONS: V2CheckoutSessions,
        PathValues.V2_CHECKOUTSESSIONS_CHECKOUT_SESSION_ID: V2CheckoutSessionsCheckoutSessionId,
        PathValues.V2_APPS: V2Apps,
        PathValues.V2_APPS_APP_ID: V2AppsAppId,
        PathValues.V2_APPS_APP_ID_COMPLIANCE: V2AppsAppIdCompliance,
        PathValues.V2_APPS_APP_ID_ACHACCOUNT: V2AppsAppIdAchAccount,
        PathValues.V2_APPS_APP_ID_DEPOSIT: V2AppsAppIdDeposit,
        PathValues.V2_APPS_APP_ID_WITHDRAW: V2AppsAppIdWithdraw,
        PathValues.V2_PAYMENTMETHODS: V2PaymentMethods,
        PathValues.V2_PAYMENTMETHODS_PAYMENT_METHOD_ID: V2PaymentMethodsPaymentMethodId,
        PathValues.V2_PAYMENTMETHODS_PAYMENT_METHOD_ID_ATTACH: V2PaymentMethodsPaymentMethodIdAttach,
        PathValues.V2_PAYMENTMETHODS_PAYMENT_METHOD_ID_DETACH: V2PaymentMethodsPaymentMethodIdDetach,
        PathValues.V2_DISPUTES: V2Disputes,
        PathValues.V2_DISPUTES_DISPUTE_ID: V2DisputesDisputeId,
        PathValues.V2_DISPUTES_DISPUTE_ID_EVIDENCE: V2DisputesDisputeIdEvidence,
        PathValues.V2_DISPUTES_DISPUTE_ID_SUBMIT: V2DisputesDisputeIdSubmit,
        PathValues.V2_REFUNDS: V2Refunds,
        PathValues.V2_REFUNDS_REFUND_ID: V2RefundsRefundId,
        PathValues.V2_ORGANIZATIONTRANSFERS: V2OrganizationTransfers,
        PathValues.V2_ORGANIZATIONTRANSFERS_TRANSFER_ID: V2OrganizationTransfersTransferId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_USERS: V2Users,
        PathValues.V2_USERS_USER_ID: V2UsersUserId,
        PathValues.V2_USERS_USER_ID_COMPLIANCE: V2UsersUserIdCompliance,
        PathValues.V2_USERS_USER_ID_SENDVERIFICATIONTOKEN: V2UsersUserIdSendVerificationToken,
        PathValues.V2_USERS_USER_ID_VERIFY: V2UsersUserIdVerify,
        PathValues.V2_USERS_USER_ID_PAYOUTMETHODS: V2UsersUserIdPayoutMethods,
        PathValues.V2_TRANSFERS: V2Transfers,
        PathValues.V2_TRANSFERS_TRANSFER_ID: V2TransfersTransferId,
        PathValues.V2_FLOWS: V2Flows,
        PathValues.V2_FLOWS_FLOW_ID: V2FlowsFlowId,
        PathValues.V2_PAYOUTLINKS: V2PayoutLinks,
        PathValues.V2_PAYOUTLINKS_PAYOUT_LINK_ID: V2PayoutLinksPayoutLinkId,
        PathValues.V2_PAYOUTS: V2Payouts,
        PathValues.V2_PAYMENTS: V2Payments,
        PathValues.V2_PAYOUTS_SENDPAYOUT: V2PayoutsSendPayout,
        PathValues.V2_PAYOUTREQUESTS: V2PayoutRequests,
        PathValues.V2_PAYOUTREQUESTS_PAYOUT_REQUEST_ID: V2PayoutRequestsPayoutRequestId,
        PathValues.V2_TRANSACTIONS: V2Transactions,
        PathValues.V2_TRANSACTIONS_TRANSACTION_ID: V2TransactionsTransactionId,
        PathValues.V2_PAYMENTINTENTS: V2PaymentIntents,
        PathValues.V2_PAYMENTINTENTS_PAYMENT_INTENT_ID: V2PaymentIntentsPaymentIntentId,
        PathValues.V2_PAYMENTINTENTS_PAYMENT_INTENT_ID_CONFIRM: V2PaymentIntentsPaymentIntentIdConfirm,
        PathValues.V2_TRANSFERBATCHES: V2TransferBatches,
        PathValues.V2_TRANSFERBATCHES_TRANSFER_BATCH_ID: V2TransferBatchesTransferBatchId,
        PathValues.V2_PAYMENTCUSTOMERS: V2PaymentCustomers,
        PathValues.V2_PAYMENTCUSTOMERS_PAYMENT_CUSTOMER_ID: V2PaymentCustomersPaymentCustomerId,
        PathValues.V2_CHECKOUTSESSIONS: V2CheckoutSessions,
        PathValues.V2_CHECKOUTSESSIONS_CHECKOUT_SESSION_ID: V2CheckoutSessionsCheckoutSessionId,
        PathValues.V2_APPS: V2Apps,
        PathValues.V2_APPS_APP_ID: V2AppsAppId,
        PathValues.V2_APPS_APP_ID_COMPLIANCE: V2AppsAppIdCompliance,
        PathValues.V2_APPS_APP_ID_ACHACCOUNT: V2AppsAppIdAchAccount,
        PathValues.V2_APPS_APP_ID_DEPOSIT: V2AppsAppIdDeposit,
        PathValues.V2_APPS_APP_ID_WITHDRAW: V2AppsAppIdWithdraw,
        PathValues.V2_PAYMENTMETHODS: V2PaymentMethods,
        PathValues.V2_PAYMENTMETHODS_PAYMENT_METHOD_ID: V2PaymentMethodsPaymentMethodId,
        PathValues.V2_PAYMENTMETHODS_PAYMENT_METHOD_ID_ATTACH: V2PaymentMethodsPaymentMethodIdAttach,
        PathValues.V2_PAYMENTMETHODS_PAYMENT_METHOD_ID_DETACH: V2PaymentMethodsPaymentMethodIdDetach,
        PathValues.V2_DISPUTES: V2Disputes,
        PathValues.V2_DISPUTES_DISPUTE_ID: V2DisputesDisputeId,
        PathValues.V2_DISPUTES_DISPUTE_ID_EVIDENCE: V2DisputesDisputeIdEvidence,
        PathValues.V2_DISPUTES_DISPUTE_ID_SUBMIT: V2DisputesDisputeIdSubmit,
        PathValues.V2_REFUNDS: V2Refunds,
        PathValues.V2_REFUNDS_REFUND_ID: V2RefundsRefundId,
        PathValues.V2_ORGANIZATIONTRANSFERS: V2OrganizationTransfers,
        PathValues.V2_ORGANIZATIONTRANSFERS_TRANSFER_ID: V2OrganizationTransfersTransferId,
    }
)
