# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from dots_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    USERS = "users"
    APPS = "apps"
    TRANSFERS = "transfers"
    DISPUTES = "disputes"
    PAYMENTINTENTS = "payment-intents"
    PAYMENTMETHODS = "payment-methods"
    PAYOUTLINKS = "payout-links"
    CHECKOUTSESSIONS = "checkout-sessions"
    FLOWS = "flows"
    PAYMENTCUSTOMERS = "payment-customers"
    PAYOUTREQUESTS = "payout-requests"
    REFUNDS = "refunds"
    TRANSFERBATCHES = "transfer-batches"
    PAYOUTS = "payouts"
    TRANSACTIONS = "transactions"
    PAYMENTS = "payments"
