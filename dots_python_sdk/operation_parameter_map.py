operation_parameter_map = {
    '/v2/apps/{app_id}/ach-account-PUT': {
        'parameters': [
            {
                'name': 'account_number'
            },
            {
                'name': 'routing_number'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'app_id'
            },
        ]
    },
    '/v2/apps-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/apps/{app_id}/deposit-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'idempotency_key'
            },
        ]
    },
    '/v2/apps/{app_id}/ach-account-GET': {
        'parameters': [
            {
                'name': 'app_id'
            },
        ]
    },
    '/v2/apps/{app_id}-GET': {
        'parameters': [
            {
                'name': 'app_id'
            },
        ]
    },
    '/v2/apps/{app_id}/compliance-GET': {
        'parameters': [
            {
                'name': 'app_id'
            },
        ]
    },
    '/v2/apps-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/apps/{app_id}/compliance-PUT': {
        'parameters': [
            {
                'name': 'company_info'
            },
            {
                'name': 'contact_info'
            },
            {
                'name': 'directors'
            },
            {
                'name': 'flow_of_funds'
            },
            {
                'name': 'app_id'
            },
        ]
    },
    '/v2/apps/{app_id}/withdraw-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'idempotency_key'
            },
        ]
    },
    '/v2/checkout-sessions-POST': {
        'parameters': [
            {
                'name': 'line_items'
            },
            {
                'name': 'success_url'
            },
            {
                'name': 'mode'
            },
            {
                'name': 'customer_email'
            },
            {
                'name': 'client_reference_id'
            },
            {
                'name': 'cancel_url'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'customer_id'
            },
            {
                'name': 'expires_in'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/checkout-sessions/{checkout_session_id}-GET': {
        'parameters': [
            {
                'name': 'checkout_session_id'
            },
        ]
    },
    '/v2/checkout-sessions-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/disputes/{dispute_id}/evidence-POST': {
        'parameters': [
            {
                'name': 'dispute_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'content'
            },
        ]
    },
    '/v2/disputes-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/disputes/{dispute_id}-GET': {
        'parameters': [
            {
                'name': 'dispute_id'
            },
        ]
    },
    '/v2/disputes/{dispute_id}/submit-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'dispute_id'
            },
        ]
    },
    '/v2/flows-POST': {
        'parameters': [
            {
                'name': 'steps'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/flows/{flow_id}-GET': {
        'parameters': [
            {
                'name': 'flow_id'
            },
        ]
    },
    '/v2/flows-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/payment-customers-POST': {
        'parameters': [
            {
                'name': 'id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'email'
            },
            {
                'name': 'country_code'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'first_name'
            },
            {
                'name': 'middle_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'created'
            },
            {
                'name': 'updated'
            },
        ]
    },
    '/v2/payment-customers/{payment_customer_id}-GET': {
        'parameters': [
            {
                'name': 'payment_customer_id'
            },
        ]
    },
    '/v2/payment-customers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/payment-intents/{payment_intent_id}/confirm-POST': {
        'parameters': [
            {
                'name': 'payment_method_id'
            },
            {
                'name': 'payment_intent_id'
            },
        ]
    },
    '/v2/payment-intents-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'currency'
            },
            {
                'name': 'description'
            },
            {
                'name': 'confirm'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'customer_id'
            },
            {
                'name': 'payment_method_id'
            },
            {
                'name': 'payment_method_types'
            },
            {
                'name': 'setup_future_usage'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'transfer_data'
            },
            {
                'name': 'application_fee_amount'
            },
        ]
    },
    '/v2/payment-intents/{payment_intent_id}-GET': {
        'parameters': [
            {
                'name': 'payment_intent_id'
            },
        ]
    },
    '/v2/payment-intents-GET': {
        'parameters': [
        ]
    },
    '/v2/payment-methods/{payment_method_id}/attach-POST': {
        'parameters': [
            {
                'name': 'customer_id'
            },
            {
                'name': 'payment_method_id'
            },
        ]
    },
    '/v2/payment-methods/{payment_method_id}/detach-POST': {
        'parameters': [
            {
                'name': 'payment_method_id'
            },
            {
                'name': 'customer_id'
            },
        ]
    },
    '/v2/payment-methods/{payment_method_id}-GET': {
        'parameters': [
            {
                'name': 'payment_method_id'
            },
        ]
    },
    '/v2/payment-methods-GET': {
        'parameters': [
            {
                'name': 'customer_id'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/v2/payments-POST': {
        'parameters': [
        ]
    },
    '/v2/payout-links/{payout_link_id}-DELETE': {
        'parameters': [
            {
                'name': 'payout_link_id'
            },
        ]
    },
    '/v2/payout-links-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'payee'
            },
            {
                'name': 'delivery'
            },
            {
                'name': 'force_collect_compliance_information'
            },
            {
                'name': 'tax_exempt'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'idempotency_key'
            },
            {
                'name': 'payout_fee_party'
            },
            {
                'name': 'additional_steps'
            },
        ]
    },
    '/v2/payout-links/{payout_link_id}-GET': {
        'parameters': [
            {
                'name': 'payout_link_id'
            },
        ]
    },
    '/v2/payout-links-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/payout-requests-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/payout-requests/{payout_request_id}-GET': {
        'parameters': [
            {
                'name': 'payout_request_id'
            },
        ]
    },
    '/v2/payout-requests-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'payee'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'memo'
            },
        ]
    },
    '/v2/payouts-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'amount'
            },
            {
                'name': 'platform'
            },
            {
                'name': 'account_id'
            },
            {
                'name': 'fund'
            },
            {
                'name': 'idempotency_key'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/payouts/send-payout-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'payee'
            },
            {
                'name': 'delivery'
            },
            {
                'name': 'force_collect_compliance_information'
            },
            {
                'name': 'additional_steps'
            },
            {
                'name': 'tax_exempt'
            },
            {
                'name': 'metadata'
            },
            {
                'name': 'memo'
            },
            {
                'name': 'idempotency_key'
            },
            {
                'name': 'payout_fee_party'
            },
        ]
    },
    '/v2/refunds-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'payment_intent_id'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/refunds-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/refunds/{refund_id}-GET': {
        'parameters': [
            {
                'name': 'refund_id'
            },
        ]
    },
    '/v2/transactions/{transaction_id}-GET': {
        'parameters': [
            {
                'name': 'transaction_id'
            },
        ]
    },
    '/v2/transactions-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/transfer-batches-POST': {
        'parameters': [
            {
                'name': 'items'
            },
            {
                'name': 'idempotency_key'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/transfer-batches/{transfer_batch_id}-GET': {
        'parameters': [
            {
                'name': 'transfer_batch_id'
            },
        ]
    },
    '/v2/transfer-batches-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/organization-transfers-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'api_app_id'
            },
            {
                'name': 'idempotency_key'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/transfers-POST': {
        'parameters': [
            {
                'name': 'amount'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'tax_exempt'
            },
            {
                'name': 'idempotency_key'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/organization-transfers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/v2/transfers/{transfer_id}-GET': {
        'parameters': [
            {
                'name': 'transfer_id'
            },
        ]
    },
    '/v2/organization-transfers/{transfer_id}-GET': {
        'parameters': [
            {
                'name': 'transfer_id'
            },
        ]
    },
    '/v2/transfers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'starting_after'
            },
            {
                'name': 'ending_before'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/v2/users/{user_id}/payout-methods-PUT': {
        'parameters': [
            {
                'name': 'platform'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'routing_number'
            },
            {
                'name': 'account_number'
            },
            {
                'name': 'account_type'
            },
            {
                'name': 'email'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'handle'
            },
            {
                'name': 'cash_tag'
            },
        ]
    },
    '/v2/users-POST': {
        'parameters': [
            {
                'name': 'first_name'
            },
            {
                'name': 'last_name'
            },
            {
                'name': 'email'
            },
            {
                'name': 'country_code'
            },
            {
                'name': 'phone_number'
            },
            {
                'name': 'username'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/users/{user_id}-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/v2/users-GET': {
        'parameters': [
            {
                'name': 'starting_after'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'ending_before'
            },
        ]
    },
    '/v2/users/{user_id}/payout-methods-GET': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/v2/users/{user_id}-DELETE': {
        'parameters': [
            {
                'name': 'user_id'
            },
        ]
    },
    '/v2/users/{user_id}/send-verification-token-POST': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'use_voice'
            },
        ]
    },
    '/v2/users/{user_id}/compliance-PUT': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'w9'
            },
            {
                'name': 'w8ben'
            },
        ]
    },
    '/v2/users/{user_id}-PATCH': {
        'parameters': [
            {
                'name': 'user_id'
            },
            {
                'name': 'default_payout_method'
            },
            {
                'name': 'auto_payout_enabled'
            },
            {
                'name': 'metadata'
            },
        ]
    },
    '/v2/users/{user_id}/verify-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user_id'
            },
        ]
    },
};