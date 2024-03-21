<div align="center">

[![Visit Dots](./header.png)](https://dots.dev)

# Dots<a id="dots"></a>

Scalable and Flexible Payouts Infrastructure


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`dots.apps.add_ach_account`](#dotsappsadd_ach_account)
  * [`dots.apps.create_new_app`](#dotsappscreate_new_app)
  * [`dots.apps.deposit_funds`](#dotsappsdeposit_funds)
  * [`dots.apps.get_ach_account`](#dotsappsget_ach_account)
  * [`dots.apps.get_by_id`](#dotsappsget_by_id)
  * [`dots.apps.get_compliance_info`](#dotsappsget_compliance_info)
  * [`dots.apps.list_all`](#dotsappslist_all)
  * [`dots.apps.update_compliance_info`](#dotsappsupdate_compliance_info)
  * [`dots.apps.withdraw_funds`](#dotsappswithdraw_funds)
  * [`dots.checkout_sessions.create_session`](#dotscheckout_sessionscreate_session)
  * [`dots.checkout_sessions.get_by_id`](#dotscheckout_sessionsget_by_id)
  * [`dots.checkout_sessions.list_all`](#dotscheckout_sessionslist_all)
  * [`dots.disputes.add_evidence_file`](#dotsdisputesadd_evidence_file)
  * [`dots.disputes.get_all`](#dotsdisputesget_all)
  * [`dots.disputes.get_by_id`](#dotsdisputesget_by_id)
  * [`dots.disputes.submit_dispute`](#dotsdisputessubmit_dispute)
  * [`dots.flows.create_new_flow`](#dotsflowscreate_new_flow)
  * [`dots.flows.get_by_id`](#dotsflowsget_by_id)
  * [`dots.flows.list_all`](#dotsflowslist_all)
  * [`dots.payment_customers.create_customer`](#dotspayment_customerscreate_customer)
  * [`dots.payment_customers.get_by_id`](#dotspayment_customersget_by_id)
  * [`dots.payment_customers.list_all`](#dotspayment_customerslist_all)
  * [`dots.payment_intents.confirm_intent`](#dotspayment_intentsconfirm_intent)
  * [`dots.payment_intents.create_intent`](#dotspayment_intentscreate_intent)
  * [`dots.payment_intents.get_by_id`](#dotspayment_intentsget_by_id)
  * [`dots.payment_intents.list_all`](#dotspayment_intentslist_all)
  * [`dots.payment_methods.attach_payment_method`](#dotspayment_methodsattach_payment_method)
  * [`dots.payment_methods.detach_payment_method`](#dotspayment_methodsdetach_payment_method)
  * [`dots.payment_methods.get_by_id`](#dotspayment_methodsget_by_id)
  * [`dots.payment_methods.list_all_payment_customer`](#dotspayment_methodslist_all_payment_customer)
  * [`dots.payments.create_transaction`](#dotspaymentscreate_transaction)
  * [`dots.payout_links.cancel_link`](#dotspayout_linkscancel_link)
  * [`dots.payout_links.create_payout_link`](#dotspayout_linkscreate_payout_link)
  * [`dots.payout_links.get_payout_link`](#dotspayout_linksget_payout_link)
  * [`dots.payout_links.list_all`](#dotspayout_linkslist_all)
  * [`dots.payout_requests.get_all_payouts`](#dotspayout_requestsget_all_payouts)
  * [`dots.payout_requests.get_payout_by_id`](#dotspayout_requestsget_payout_by_id)
  * [`dots.payout_requests.submit_request`](#dotspayout_requestssubmit_request)
  * [`dots.payouts.create_payout`](#dotspayoutscreate_payout)
  * [`dots.payouts.send_payout`](#dotspayoutssend_payout)
  * [`dots.refunds.create_refund`](#dotsrefundscreate_refund)
  * [`dots.refunds.get_all`](#dotsrefundsget_all)
  * [`dots.refunds.get_by_id`](#dotsrefundsget_by_id)
  * [`dots.transactions.get_by_id`](#dotstransactionsget_by_id)
  * [`dots.transactions.list_all`](#dotstransactionslist_all)
  * [`dots.transfer_batches.create_batch`](#dotstransfer_batchescreate_batch)
  * [`dots.transfer_batches.get_by_id`](#dotstransfer_batchesget_by_id)
  * [`dots.transfer_batches.list_all`](#dotstransfer_batcheslist_all)
  * [`dots.transfers.create_organization_transfer`](#dotstransferscreate_organization_transfer)
  * [`dots.transfers.create_transfer`](#dotstransferscreate_transfer)
  * [`dots.transfers.get_all`](#dotstransfersget_all)
  * [`dots.transfers.get_by_id`](#dotstransfersget_by_id)
  * [`dots.transfers.get_by_id_0`](#dotstransfersget_by_id_0)
  * [`dots.transfers.list_all`](#dotstransferslist_all)
  * [`dots.users.add_payout_method`](#dotsusersadd_payout_method)
  * [`dots.users.create_new_user`](#dotsuserscreate_new_user)
  * [`dots.users.get_user_by_id`](#dotsusersget_user_by_id)
  * [`dots.users.list_all_users`](#dotsuserslist_all_users)
  * [`dots.users.list_payout_methods`](#dotsuserslist_payout_methods)
  * [`dots.users.remove_user`](#dotsusersremove_user)
  * [`dots.users.send_verification_token`](#dotsuserssend_verification_token)
  * [`dots.users.submit_compliance_info`](#dotsuserssubmit_compliance_info)
  * [`dots.users.update_user_object`](#dotsusersupdate_user_object)
  * [`dots.users.verify_user_token`](#dotsusersverify_user_token)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Dots&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from dots_python_sdk import Dots, ApiException

dots = Dots(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Add App ACH Account
    add_ach_account_response = dots.apps.add_ach_account(
        account_number="4807288800152",
        routing_number="048072888",
        account_type="checking",
        app_id="app_id_example",
    )
    print(add_ach_account_response)
except ApiException as e:
    print("Exception when calling AppsApi.add_ach_account: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from dots_python_sdk import Dots, ApiException

dots = Dots(username="YOUR_USERNAME", password="YOUR_PASSWORD")


async def main():
    try:
        # Add App ACH Account
        add_ach_account_response = await dots.apps.aadd_ach_account(
            account_number="4807288800152",
            routing_number="048072888",
            account_type="checking",
            app_id="app_id_example",
        )
        print(add_ach_account_response)
    except ApiException as e:
        print("Exception when calling AppsApi.add_ach_account: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from dots_python_sdk import Dots, ApiException

dots = Dots(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    # Add App ACH Account
    add_ach_account_response = dots.apps.raw.add_ach_account(
        account_number="4807288800152",
        routing_number="048072888",
        account_type="checking",
        app_id="app_id_example",
    )
    pprint(add_ach_account_response.body)
    pprint(add_ach_account_response.body["mask"])
    pprint(add_ach_account_response.body["name"])
    pprint(add_ach_account_response.headers)
    pprint(add_ach_account_response.status)
    pprint(add_ach_account_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AppsApi.add_ach_account: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `dots.apps.add_ach_account`<a id="dotsappsadd_ach_account"></a>

Add an ACH account to an app. The account's owner must match the compliance information submitted.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_ach_account_response = dots.apps.add_ach_account(
    account_number="4807288800152",
    routing_number="048072888",
    account_type="checking",
    app_id="app_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### account_number: `str`<a id="account_number-str"></a>

The bank account number.

##### routing_number: `str`<a id="routing_number-str"></a>

The bank's ABA routing number.

##### account_type: `str`<a id="account_type-str"></a>

The type of bank account.

##### app_id: `str`<a id="app_id-str"></a>

The ID of the app.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppsAddAchAccountRequest`](./dots_python_sdk/type/apps_add_ach_account_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AppsAddAchAccountResponse`](./dots_python_sdk/pydantic/apps_add_ach_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps/{app_id}/ach-account` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.create_new_app`<a id="dotsappscreate_new_app"></a>

Create an app in your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_app_response = dots.apps.create_new_app(
    name="aaa",
    metadata=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

The name of the application.

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppsCreateNewAppRequest`](./dots_python_sdk/type/apps_create_new_app_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`App`](./dots_python_sdk/pydantic/app.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.deposit_funds`<a id="dotsappsdeposit_funds"></a>

Deposit funds into App wallet by endpoint.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
deposit_funds_response = dots.apps.deposit_funds(
    amount=1,
    app_id="app_id_example",
    idempotency_key="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount to deposit in cents.

##### app_id: `str`<a id="app_id-str"></a>

The ID of the App.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency key in UUID format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppsDepositFundsRequest`](./dots_python_sdk/type/apps_deposit_funds_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps/{app_id}/deposit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.get_ach_account`<a id="dotsappsget_ach_account"></a>

Get the App's ach account information.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ach_account_response = dots.apps.get_ach_account(
    app_id="app_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

The ID of the app.

#### 🔄 Return<a id="🔄-return"></a>

[`AppsGetAchAccountResponse`](./dots_python_sdk/pydantic/apps_get_ach_account_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps/{app_id}/ach-account` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.get_by_id`<a id="dotsappsget_by_id"></a>

Retrieve an app in your organization by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.apps.get_by_id(
    app_id="app_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

ID of the app to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`App`](./dots_python_sdk/pydantic/app.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps/{app_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.get_compliance_info`<a id="dotsappsget_compliance_info"></a>

Retrieve the compliance information for an app in your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_compliance_info_response = dots.apps.get_compliance_info(
    app_id="app_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

ID of the app to query or modify

#### 🔄 Return<a id="🔄-return"></a>

[`BusinessComplianceInfo`](./dots_python_sdk/pydantic/business_compliance_info.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps/{app_id}/compliance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.list_all`<a id="dotsappslist_all"></a>

List all apps created by your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.apps.list_all(
    limit=0,
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

Maximum number of results to retrieve

##### starting_after: `str`<a id="starting_after-str"></a>

ID of first app to retrieve

##### ending_before: `str`<a id="ending_before-str"></a>

ID of last app to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`AppsListAllResponse`](./dots_python_sdk/pydantic/apps_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.update_compliance_info`<a id="dotsappsupdate_compliance_info"></a>

Add or update compliance information for an app in your organization

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_compliance_info_response = dots.apps.update_compliance_info(
    company_info={
        "ein": "048072888",
        "incorporation_date": "1970-01-01",
        "incorporation_state": "incorporation_state_example",
        "incorporation_type": "sole_proprietorship",
        "name": "name_example",
        "website": "website_example",
    },
    contact_info={
        "city": "city_example",
        "country": "country_example",
        "email": "email_example",
        "line1": "line1_example",
        "phone_number": "phone_number_example",
        "state": "state_example",
        "zip": "zip_example",
    },
    directors=[
        {
            "title": "title_example",
            "address": {
                "city": "city_example",
                "country": "country_example",
                "line1": "line1_example",
                "zip": "zip_example",
            },
            "dob": "1970-01-01",
            "email": "email_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "ownership_percentage": 3.14,
            "phone": "phone_example",
        }
    ],
    flow_of_funds={
        "reasons": "Payments are processed via credit card, deposited to Dots, and paid to sellers.",
        "usage": "We are a market place for teddy bears.",
    },
    app_id="app_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### company_info: [`BusinessComplianceInfoCompanyInfo`](./dots_python_sdk/type/business_compliance_info_company_info.py)<a id="company_info-businesscomplianceinfocompanyinfodots_python_sdktypebusiness_compliance_info_company_infopy"></a>


##### contact_info: [`BusinessComplianceInfoContactInfo`](./dots_python_sdk/type/business_compliance_info_contact_info.py)<a id="contact_info-businesscomplianceinfocontactinfodots_python_sdktypebusiness_compliance_info_contact_infopy"></a>


##### directors: [`BusinessComplianceInfoDirectors`](./dots_python_sdk/type/business_compliance_info_directors.py)<a id="directors-businesscomplianceinfodirectorsdots_python_sdktypebusiness_compliance_info_directorspy"></a>

##### flow_of_funds: [`BusinessComplianceInfoFlowOfFunds`](./dots_python_sdk/type/business_compliance_info_flow_of_funds.py)<a id="flow_of_funds-businesscomplianceinfoflowoffundsdots_python_sdktypebusiness_compliance_info_flow_of_fundspy"></a>


##### app_id: `str`<a id="app_id-str"></a>

ID of the app to query or modify

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BusinessComplianceInfo`](./dots_python_sdk/type/business_compliance_info.py)
#### 🔄 Return<a id="🔄-return"></a>

[`BusinessComplianceInfo`](./dots_python_sdk/pydantic/business_compliance_info.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps/{app_id}/compliance` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.apps.withdraw_funds`<a id="dotsappswithdraw_funds"></a>

Withdraw funds from app wallet into app bank account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
withdraw_funds_response = dots.apps.withdraw_funds(
    amount=1,
    app_id="app_id_example",
    idempotency_key="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount to deposit in cents.

##### app_id: `str`<a id="app_id-str"></a>

The ID of the App.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

Idempotency key in UUID format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AppsWithdrawFundsRequest`](./dots_python_sdk/type/apps_withdraw_funds_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/apps/{app_id}/withdraw` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.checkout_sessions.create_session`<a id="dotscheckout_sessionscreate_session"></a>

Create a checkout session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_response = dots.checkout_sessions.create_session(
    line_items=[
        {
            "price_data": {
                "currency": "usd",
                "amount": 1,
                "product_data": {
                    "name": "name_example",
                },
            },
            "quantity": 1,
        }
    ],
    success_url="string_example",
    mode="payment",
    customer_email="string_example",
    client_reference_id="string_example",
    cancel_url="string_example",
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    customer_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    expires_in=10800,
    metadata={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### line_items: [`CheckoutsessionsCreateSessionRequestLineItems`](./dots_python_sdk/type/checkoutsessions_create_session_request_line_items.py)<a id="line_items-checkoutsessionscreatesessionrequestlineitemsdots_python_sdktypecheckoutsessions_create_session_request_line_itemspy"></a>

##### success_url: `str`<a id="success_url-str"></a>

##### mode: `str`<a id="mode-str"></a>

##### customer_email: `str`<a id="customer_email-str"></a>

##### client_reference_id: `str`<a id="client_reference_id-str"></a>

##### cancel_url: `str`<a id="cancel_url-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

Supply a Dots user ID in place of a customer ID

##### customer_id: `str`<a id="customer_id-str"></a>

##### expires_in: `int`<a id="expires_in-int"></a>

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CheckoutsessionsCreateSessionRequest`](./dots_python_sdk/type/checkoutsessions_create_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CheckoutSession`](./dots_python_sdk/pydantic/checkout_session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout-sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.checkout_sessions.get_by_id`<a id="dotscheckout_sessionsget_by_id"></a>

Retrieve a checkout session by an ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.checkout_sessions.get_by_id(
    checkout_session_id="checkout_session_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### checkout_session_id: `str`<a id="checkout_session_id-str"></a>

ID of the checkout session to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`CheckoutSession`](./dots_python_sdk/pydantic/checkout_session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout-sessions/{checkout_session_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.checkout_sessions.list_all`<a id="dotscheckout_sessionslist_all"></a>

List all checkout sessions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.checkout_sessions.list_all(
    limit="string_example",
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`CheckoutsessionsListAllResponse`](./dots_python_sdk/pydantic/checkoutsessions_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/checkout-sessions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.disputes.add_evidence_file`<a id="dotsdisputesadd_evidence_file"></a>

Add an evidence file to the dispute

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dots.disputes.add_evidence_file(
    dispute_id="dispute_id_example",
    type="customer_communications",
    content="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dispute_id: `str`<a id="dispute_id-str"></a>

ID of the dispute to add evidence to

##### type: `str`<a id="type-str"></a>

##### content: `str`<a id="content-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DisputesAddEvidenceFileRequest`](./dots_python_sdk/type/disputes_add_evidence_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/disputes/{dispute_id}/evidence` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.disputes.get_all`<a id="dotsdisputesget_all"></a>

List all disputes

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = dots.disputes.get_all(
    limit="string_example",
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`DisputesGetAllResponse`](./dots_python_sdk/pydantic/disputes_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/disputes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.disputes.get_by_id`<a id="dotsdisputesget_by_id"></a>

Retreieve a dispute by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.disputes.get_by_id(
    dispute_id="dispute_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dispute_id: `str`<a id="dispute_id-str"></a>

ID of the dispute to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`Dispute`](./dots_python_sdk/pydantic/dispute.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/disputes/{dispute_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.disputes.submit_dispute`<a id="dotsdisputessubmit_dispute"></a>

Submit a dispute

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dots.disputes.submit_dispute(
    description="string_example",
    dispute_id="dispute_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

##### dispute_id: `str`<a id="dispute_id-str"></a>

ID of the dispute to submit

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DisputesSubmitDisputeRequest`](./dots_python_sdk/type/disputes_submit_dispute_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/disputes/{dispute_id}/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.flows.create_new_flow`<a id="dotsflowscreate_new_flow"></a>

Create a new Flow.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_flow_response = dots.flows.create_new_flow(
    steps=[None],
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    metadata=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### steps: [`FlowsCreateNewFlowRequestSteps`](./dots_python_sdk/type/flows_create_new_flow_request_steps.py)<a id="steps-flowscreatenewflowrequeststepsdots_python_sdktypeflows_create_new_flow_request_stepspy"></a>

##### user_id: `str`<a id="user_id-str"></a>

The user's id.

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`FlowsCreateNewFlowRequest`](./dots_python_sdk/type/flows_create_new_flow_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Flow`](./dots_python_sdk/pydantic/flow.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/flows` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.flows.get_by_id`<a id="dotsflowsget_by_id"></a>

Get a Flow by its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.flows.get_by_id(
    flow_id="flow_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### flow_id: `str`<a id="flow_id-str"></a>

Id of the flow to fetch

#### 🔄 Return<a id="🔄-return"></a>

[`Flow`](./dots_python_sdk/pydantic/flow.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/flows/{flow_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.flows.list_all`<a id="dotsflowslist_all"></a>

List all Flows.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.flows.list_all(
    limit=1,
    starting_after="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    ending_before="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`FlowsListAllResponse`](./dots_python_sdk/pydantic/flows_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/flows` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_customers.create_customer`<a id="dotspayment_customerscreate_customer"></a>

Create a Payment Customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_customer_response = dots.payment_customers.create_customer(
    id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    email="string_example",
    country_code="string_example",
    phone_number="string_example",
    first_name="string_example",
    middle_name="string_example",
    last_name="string_example",
    metadata={},
    created="1970-01-01T00:00:00.00Z",
    updated="1970-01-01T00:00:00.00Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

##### user_id: `str`<a id="user_id-str"></a>

##### email: `str`<a id="email-str"></a>

##### country_code: `str`<a id="country_code-str"></a>

##### phone_number: `str`<a id="phone_number-str"></a>

##### first_name: `str`<a id="first_name-str"></a>

##### middle_name: `str`<a id="middle_name-str"></a>

##### last_name: `str`<a id="last_name-str"></a>

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

##### created: `datetime`<a id="created-datetime"></a>

##### updated: `datetime`<a id="updated-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentCustomer`](./dots_python_sdk/type/payment_customer.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentcustomersCreateCustomerResponse`](./dots_python_sdk/pydantic/paymentcustomers_create_customer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-customers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_customers.get_by_id`<a id="dotspayment_customersget_by_id"></a>

Get a payment customer by ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.payment_customers.get_by_id(
    payment_customer_id="payment_customer_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_customer_id: `str`<a id="payment_customer_id-str"></a>

The ID of the payment customer

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentCustomer`](./dots_python_sdk/pydantic/payment_customer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-customers/{payment_customer_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_customers.list_all`<a id="dotspayment_customerslist_all"></a>

List all payment customers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.payment_customers.list_all(
    limit="string_example",
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentcustomersListAllResponse`](./dots_python_sdk/pydantic/paymentcustomers_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-customers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_intents.confirm_intent`<a id="dotspayment_intentsconfirm_intent"></a>

Confirm a payment intent that has not been confirmed yet.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
confirm_intent_response = dots.payment_intents.confirm_intent(
    payment_method_id="string_example",
    payment_intent_id="payment_intent_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_method_id: `str`<a id="payment_method_id-str"></a>

ID of the payment method to confirm the intent with.

##### payment_intent_id: `str`<a id="payment_intent_id-str"></a>

The ID if the Payment Intent to confirm.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentintentsConfirmIntentRequest`](./dots_python_sdk/type/paymentintents_confirm_intent_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentIntent`](./dots_python_sdk/pydantic/payment_intent.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-intents/{payment_intent_id}/confirm` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_intents.create_intent`<a id="dotspayment_intentscreate_intent"></a>

Create a Payment Intent

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_intent_response = dots.payment_intents.create_intent(
    amount=1,
    currency="usd",
    description="string_example",
    confirm=False,
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    customer_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    payment_method_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    payment_method_types=["string_example"],
    setup_future_usage="on_session",
    metadata=True,
    transfer_data={},
    application_fee_amount=0,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Amount in cents

##### currency: `str`<a id="currency-str"></a>

Currency of the payment. Currently only `usd` is supported.

##### description: `str`<a id="description-str"></a>

An arbitrary string attached to the object. Often useful for displaying to users.

##### confirm: `bool`<a id="confirm-bool"></a>

Set to `true` to attempt to confirm this payment intent immediately. Defaults to `false`.

##### user_id: `str`<a id="user_id-str"></a>

ID of a Dots `user` making this payment.

##### customer_id: `str`<a id="customer_id-str"></a>

ID of a Dots `payment_customer` making this payment.

##### payment_method_id: `str`<a id="payment_method_id-str"></a>

ID of the payment method to attach to this payment intent.

##### payment_method_types: [`PaymentintentsCreateIntentRequestPaymentMethodTypes`](./dots_python_sdk/type/paymentintents_create_intent_request_payment_method_types.py)<a id="payment_method_types-paymentintentscreateintentrequestpaymentmethodtypesdots_python_sdktypepaymentintents_create_intent_request_payment_method_typespy"></a>

##### setup_future_usage: `str`<a id="setup_future_usage-str"></a>

##### metadata: `bool`<a id="metadata-bool"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

##### transfer_data: [`PaymentintentsCreateIntentRequestTransferData`](./dots_python_sdk/type/paymentintents_create_intent_request_transfer_data.py)<a id="transfer_data-paymentintentscreateintentrequesttransferdatadots_python_sdktypepaymentintents_create_intent_request_transfer_datapy"></a>


##### application_fee_amount: `int`<a id="application_fee_amount-int"></a>

Amount in cents to transfer to the application's wallet as a platform fee.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentintentsCreateIntentRequest`](./dots_python_sdk/type/paymentintents_create_intent_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentIntent`](./dots_python_sdk/pydantic/payment_intent.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-intents` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_intents.get_by_id`<a id="dotspayment_intentsget_by_id"></a>

Retrieve a payment intent by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.payment_intents.get_by_id(
    payment_intent_id="payment_intent_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_intent_id: `str`<a id="payment_intent_id-str"></a>

Payment Intent ID

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentIntent`](./dots_python_sdk/pydantic/payment_intent.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-intents/{payment_intent_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_intents.list_all`<a id="dotspayment_intentslist_all"></a>

Get all payment intents

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.payment_intents.list_all()
```

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentintentsListAllResponse`](./dots_python_sdk/pydantic/paymentintents_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-intents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_methods.attach_payment_method`<a id="dotspayment_methodsattach_payment_method"></a>

Attach a payment method to a payment customer for future usage.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
attach_payment_method_response = dots.payment_methods.attach_payment_method(
    customer_id="string_example",
    payment_method_id="payment_method_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

ID of the payment customer

##### payment_method_id: `str`<a id="payment_method_id-str"></a>

The ID of the payment method.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentmethodsAttachPaymentMethodRequest`](./dots_python_sdk/type/paymentmethods_attach_payment_method_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentMethod`](./dots_python_sdk/pydantic/payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-methods/{payment_method_id}/attach` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_methods.detach_payment_method`<a id="dotspayment_methodsdetach_payment_method"></a>

Detach a payment method from a payment customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
detach_payment_method_response = dots.payment_methods.detach_payment_method(
    payment_method_id="payment_method_id_example",
    customer_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_method_id: `str`<a id="payment_method_id-str"></a>

ID of the payment method.

##### customer_id: `str`<a id="customer_id-str"></a>

ID of the payment customer to detach the payment method from.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentmethodsDetachPaymentMethodRequest`](./dots_python_sdk/type/paymentmethods_detach_payment_method_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentMethod`](./dots_python_sdk/pydantic/payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-methods/{payment_method_id}/detach` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_methods.get_by_id`<a id="dotspayment_methodsget_by_id"></a>

Get a payment method by its ID.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.payment_methods.get_by_id(
    payment_method_id="payment_method_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payment_method_id: `str`<a id="payment_method_id-str"></a>

ID of the payment method to get

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentMethod`](./dots_python_sdk/pydantic/payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-methods/{payment_method_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payment_methods.list_all_payment_customer`<a id="dotspayment_methodslist_all_payment_customer"></a>

Get the payment methods for a payment customer

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_payment_customer_response = dots.payment_methods.list_all_payment_customer(
    customer_id="string_example",
    limit=3.14,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### customer_id: `str`<a id="customer_id-str"></a>

Payment Customer ID

##### limit: `Union[int, float]`<a id="limit-unionint-float"></a>

Number or payment methods to return

#### 🔄 Return<a id="🔄-return"></a>

[`PaymentmethodsListAllPaymentCustomerResponse`](./dots_python_sdk/pydantic/paymentmethods_list_all_payment_customer_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payment-methods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payments.create_transaction`<a id="dotspaymentscreate_transaction"></a>

Creates a transaction from a user or a payment customer to the app. User the `/users/{user_id}/payout-methods` route to get a user's stored payment methods.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_transaction_response = dots.payments.create_transaction()
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PaymentsCreateTransactionRequest`](./dots_python_sdk/type/payments_create_transaction_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payout_links.cancel_link`<a id="dotspayout_linkscancel_link"></a>

Cancel a payout link

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cancel_link_response = dots.payout_links.cancel_link(
    payout_link_id="payout_link_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payout_link_id: `str`<a id="payout_link_id-str"></a>

Id of the payout link

#### 🔄 Return<a id="🔄-return"></a>

[`PayoutLink`](./dots_python_sdk/pydantic/payout_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payout-links/{payout_link_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payout_links.create_payout_link`<a id="dotspayout_linkscreate_payout_link"></a>

Create a Payout Link.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payout_link_response = dots.payout_links.create_payout_link(
    amount=1,
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    payee={},
    delivery={
        "method": "sms",
    },
    force_collect_compliance_information=False,
    tax_exempt=True,
    metadata=None,
    memo="string_example",
    idempotency_key=None,
    payout_fee_party="user",
    additional_steps=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Amount to be paid in cents.

##### user_id: `str`<a id="user_id-str"></a>

The user's id.

##### payee: [`PayoutlinksCreatePayoutLinkRequestPayee`](./dots_python_sdk/type/payoutlinks_create_payout_link_request_payee.py)<a id="payee-payoutlinkscreatepayoutlinkrequestpayeedots_python_sdktypepayoutlinks_create_payout_link_request_payeepy"></a>


##### delivery: [`PayoutlinksCreatePayoutLinkRequestDelivery`](./dots_python_sdk/type/payoutlinks_create_payout_link_request_delivery.py)<a id="delivery-payoutlinkscreatepayoutlinkrequestdeliverydots_python_sdktypepayoutlinks_create_payout_link_request_deliverypy"></a>


##### force_collect_compliance_information: `bool`<a id="force_collect_compliance_information-bool"></a>

Force the collection of 1099 or W-8 information. Defaults to `false`.

##### tax_exempt: `bool`<a id="tax_exempt-bool"></a>

Payout links marked as `tax_exempt` will not be counted towards the 1099 threshold.

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

##### memo: `str`<a id="memo-str"></a>

Add a memo to the top of the Payout Link

##### idempotency_key: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="idempotency_key-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Unique UUID key that prevents duplicate requests from being processed. If a payout link with the idempotency key exists, a new link will not be created and the existing link will be returned instead.

##### payout_fee_party: `str`<a id="payout_fee_party-str"></a>

Overrides the setting for which party will pay fees on this payout. This takes precedence over the default for your application.

##### additional_steps: [`PayoutlinksCreatePayoutLinkRequestAdditionalSteps`](./dots_python_sdk/type/payoutlinks_create_payout_link_request_additional_steps.py)<a id="additional_steps-payoutlinkscreatepayoutlinkrequestadditionalstepsdots_python_sdktypepayoutlinks_create_payout_link_request_additional_stepspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayoutlinksCreatePayoutLinkRequest`](./dots_python_sdk/type/payoutlinks_create_payout_link_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayoutLink`](./dots_python_sdk/pydantic/payout_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payout-links` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payout_links.get_payout_link`<a id="dotspayout_linksget_payout_link"></a>

Get a payout link by its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_payout_link_response = dots.payout_links.get_payout_link(
    payout_link_id="payout_link_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payout_link_id: `str`<a id="payout_link_id-str"></a>

Id of the payout link

#### 🔄 Return<a id="🔄-return"></a>

[`PayoutLink`](./dots_python_sdk/pydantic/payout_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payout-links/{payout_link_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payout_links.list_all`<a id="dotspayout_linkslist_all"></a>

List all created Payout Links.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.payout_links.list_all(
    limit=1,
    starting_after="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    ending_before="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`PayoutlinksListAllResponse`](./dots_python_sdk/pydantic/payoutlinks_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payout-links` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payout_requests.get_all_payouts`<a id="dotspayout_requestsget_all_payouts"></a>

List all payout requests.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_payouts_response = dots.payout_requests.get_all_payouts(
    limit=1,
    starting_after="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    ending_before="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`PayoutrequestsGetAllPayoutsResponse`](./dots_python_sdk/pydantic/payoutrequests_get_all_payouts_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payout-requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payout_requests.get_payout_by_id`<a id="dotspayout_requestsget_payout_by_id"></a>

Get a payout request by its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_payout_by_id_response = dots.payout_requests.get_payout_by_id(
    payout_request_id="payout_request_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### payout_request_id: `str`<a id="payout_request_id-str"></a>

Id of the payout request

#### 🔄 Return<a id="🔄-return"></a>

[`PayoutRequest`](./dots_python_sdk/pydantic/payout_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payout-requests/{payout_request_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payout_requests.submit_request`<a id="dotspayout_requestssubmit_request"></a>

Submit a payout request from a person when you know their phone number or user id. Once the payout request is approved, they will be sent a Payout Link to onboard and recieve funds.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_request_response = dots.payout_requests.submit_request(
    amount=1,
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    payee={
        "country_code": "country_code_example",
        "phone_number": "phone_number_example",
    },
    metadata=None,
    memo="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount in cents to pay the user.

##### user_id: `str`<a id="user_id-str"></a>

The user's id. `user_id` or `payee` is required.

##### payee: [`PayoutrequestsSubmitRequestRequestPayee`](./dots_python_sdk/type/payoutrequests_submit_request_request_payee.py)<a id="payee-payoutrequestssubmitrequestrequestpayeedots_python_sdktypepayoutrequests_submit_request_request_payeepy"></a>


##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

##### memo: `str`<a id="memo-str"></a>

Add a memo to payout request

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayoutrequestsSubmitRequestRequest`](./dots_python_sdk/type/payoutrequests_submit_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayoutRequest`](./dots_python_sdk/pydantic/payout_request.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payout-requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payouts.create_payout`<a id="dotspayoutscreate_payout"></a>

Create a payout for an existing user that has a payout method saved to their account.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_payout_response = dots.payouts.create_payout(
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    amount=1,
    platform="paypal",
    account_id="string_example",
    fund=True,
    idempotency_key="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    metadata=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

ID of the `user` who you are creating the payout for.

##### amount: `int`<a id="amount-int"></a>

Amount in cents to payout the user.

##### platform: `str`<a id="platform-str"></a>

Platform that you are paying out the `user` through,

##### account_id: `str`<a id="account_id-str"></a>

The bank account ID you are paying to. Required for `ach` and `intl_bank`.

##### fund: `bool`<a id="fund-bool"></a>

Creates a transfer for the amount to the user before creating the payout. The funds are returned if the payout does not succeed.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

UUID that will be used to idempotently handle requests. Transfers with existing idempotency keys will be rejected.

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayoutsCreatePayoutRequest`](./dots_python_sdk/type/payouts_create_payout_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payouts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.payouts.send_payout`<a id="dotspayoutssend_payout"></a>

Send a payout to a person when you know their phone number or user id. If the user has a Dots acconut, the funds will delivered according to their saved prefernces. Otherwise, they will be sent a Payout Link to onboard and recieve funds.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
send_payout_response = dots.payouts.send_payout(
    amount=1,
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    payee={
        "country_code": "country_code_example",
        "phone_number": "phone_number_example",
    },
    delivery={},
    force_collect_compliance_information=False,
    additional_steps=["string_example"],
    tax_exempt=True,
    metadata=None,
    memo="string_example",
    idempotency_key=None,
    payout_fee_party="user",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount in cents to pay the user.

##### user_id: `str`<a id="user_id-str"></a>

The user's id. `user_id` or `payee` is required.

##### payee: [`PayoutsSendPayoutRequestPayee`](./dots_python_sdk/type/payouts_send_payout_request_payee.py)<a id="payee-payoutssendpayoutrequestpayeedots_python_sdktypepayouts_send_payout_request_payeepy"></a>


##### delivery: [`PayoutsSendPayoutRequestDelivery`](./dots_python_sdk/type/payouts_send_payout_request_delivery.py)<a id="delivery-payoutssendpayoutrequestdeliverydots_python_sdktypepayouts_send_payout_request_deliverypy"></a>


##### force_collect_compliance_information: `bool`<a id="force_collect_compliance_information-bool"></a>

Collect 1099 or w8-ben information.

##### additional_steps: [`PayoutsSendPayoutRequestAdditionalSteps`](./dots_python_sdk/type/payouts_send_payout_request_additional_steps.py)<a id="additional_steps-payoutssendpayoutrequestadditionalstepsdots_python_sdktypepayouts_send_payout_request_additional_stepspy"></a>

##### tax_exempt: `bool`<a id="tax_exempt-bool"></a>

Payouts marked as `tax_exempt` will not be counted towards the 1099 threshold.

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

##### memo: `str`<a id="memo-str"></a>

Add a memo to the top of the Payout Link

##### idempotency_key: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="idempotency_key-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Unique UUID key that prevents duplicate requests from being processed. If a payout link with the idempotency key exists, a new link will not be created and the existing link will be returned instead.

##### payout_fee_party: `str`<a id="payout_fee_party-str"></a>

Overrides the setting for which party will pay fees on this payout. This takes precedence over the default for your application.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PayoutsSendPayoutRequest`](./dots_python_sdk/type/payouts_send_payout_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PayoutLink`](./dots_python_sdk/pydantic/payout_link.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/payouts/send-payout` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.refunds.create_refund`<a id="dotsrefundscreate_refund"></a>

Create a Refund

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_refund_response = dots.refunds.create_refund(
    amount=1,
    payment_intent_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    reason="duplicate",
    metadata=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

Amount in cents

##### payment_intent_id: `str`<a id="payment_intent_id-str"></a>

ID of the `payment_intent` you are refunding.

##### reason: `str`<a id="reason-str"></a>

##### metadata: `bool`<a id="metadata-bool"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`RefundsCreateRefundRequest`](./dots_python_sdk/type/refunds_create_refund_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Refund`](./dots_python_sdk/pydantic/refund.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/refunds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.refunds.get_all`<a id="dotsrefundsget_all"></a>

List all refunds

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = dots.refunds.get_all(
    limit="string_example",
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`RefundsGetAllResponse`](./dots_python_sdk/pydantic/refunds_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/refunds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.refunds.get_by_id`<a id="dotsrefundsget_by_id"></a>

Retreieve a refund by its ID

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.refunds.get_by_id(
    refund_id="refund_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### refund_id: `str`<a id="refund_id-str"></a>

ID of the refund to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`Refund`](./dots_python_sdk/pydantic/refund.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/refunds/{refund_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transactions.get_by_id`<a id="dotstransactionsget_by_id"></a>

Get a transaction by its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.transactions.get_by_id(
    transaction_id="transaction_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

Id of the transaction

#### 🔄 Return<a id="🔄-return"></a>

[`Transaction`](./dots_python_sdk/pydantic/transaction.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transactions/{transaction_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transactions.list_all`<a id="dotstransactionslist_all"></a>

List all transactions.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.transactions.list_all(
    limit=1,
    starting_after="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    ending_before="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`TransactionsListAllResponse`](./dots_python_sdk/pydantic/transactions_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transactions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfer_batches.create_batch`<a id="dotstransfer_batchescreate_batch"></a>

Create a transfer batch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_batch_response = dots.transfer_batches.create_batch(
    items=[{}],
    idempotency_key="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    metadata={},
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### items: [`TransferbatchesCreateBatchRequestItems`](./dots_python_sdk/type/transferbatches_create_batch_request_items.py)<a id="items-transferbatchescreatebatchrequestitemsdots_python_sdktypetransferbatches_create_batch_request_itemspy"></a>

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

##### metadata: `Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`<a id="metadata-dictstr-unionbool-date-datetime-dict-float-int-list-str-none"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransferbatchesCreateBatchRequest`](./dots_python_sdk/type/transferbatches_create_batch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`TransferbatchesCreateBatchResponse`](./dots_python_sdk/pydantic/transferbatches_create_batch_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transfer-batches` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfer_batches.get_by_id`<a id="dotstransfer_batchesget_by_id"></a>

Get a transfer batch by id

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.transfer_batches.get_by_id(
    transfer_batch_id="transfer_batch_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transfer_batch_id: `str`<a id="transfer_batch_id-str"></a>

Id of the transfer batch to fetch

#### 🔄 Return<a id="🔄-return"></a>

[`TransferbatchesGetByIdResponse`](./dots_python_sdk/pydantic/transferbatches_get_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transfer-batches/{transfer_batch_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfer_batches.list_all`<a id="dotstransfer_batcheslist_all"></a>

Get a transfer batch

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.transfer_batches.list_all(
    limit="string_example",
    starting_after="string_example",
    ending_before="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `str`<a id="limit-str"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`TransferbatchesListAllResponse`](./dots_python_sdk/pydantic/transferbatches_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transfer-batches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfers.create_organization_transfer`<a id="dotstransferscreate_organization_transfer"></a>

Create a transfer for the organization's wallet to an api app.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_organization_transfer_response = dots.transfers.create_organization_transfer(
    amount=1,
    api_app_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    idempotency_key="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    metadata=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount in cents to transfer. Negative amount transfers money from the `app` to the `user`.

##### api_app_id: `str`<a id="api_app_id-str"></a>

API App ID to transact with.

##### idempotency_key: `str`<a id="idempotency_key-str"></a>

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransfersCreateOrganizationTransferRequest`](./dots_python_sdk/type/transfers_create_organization_transfer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/organization-transfers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfers.create_transfer`<a id="dotstransferscreate_transfer"></a>

Create a transfer.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_transfer_response = dots.transfers.create_transfer(
    amount=1,
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    tax_exempt=None,
    idempotency_key=None,
    metadata=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### amount: `int`<a id="amount-int"></a>

The amount in cents to transfer. Negative amount transfers money from the `app` to the `user`.

##### user_id: `str`<a id="user_id-str"></a>

The user's id.

##### tax_exempt: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="tax_exempt-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Transfers marked as `tax_exempt` will not be counted towards the 1099 threshold.

##### idempotency_key: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="idempotency_key-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

UUID that will be used to idempotently handle requests. Transfers with existing idempotency keys will be rejected.

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransfersCreateTransferRequest`](./dots_python_sdk/type/transfers_create_transfer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transfers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfers.get_all`<a id="dotstransfersget_all"></a>

List all transfers to and from an Organization's wallet.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_all_response = dots.transfers.get_all(
    limit=1,
    starting_after="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    ending_before="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

##### user_id: `str`<a id="user_id-str"></a>

Include only results with this user ID attached.

#### 🔄 Return<a id="🔄-return"></a>

[`TransfersGetAllResponse`](./dots_python_sdk/pydantic/transfers_get_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/organization-transfers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfers.get_by_id`<a id="dotstransfersget_by_id"></a>

Get a transfer by its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = dots.transfers.get_by_id(
    transfer_id="transfer_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transfer_id: `str`<a id="transfer_id-str"></a>

Id of the transfer to fetch

#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transfers/{transfer_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfers.get_by_id_0`<a id="dotstransfersget_by_id_0"></a>

Get a transfer by its id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_0_response = dots.transfers.get_by_id_0(
    transfer_id="transfer_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transfer_id: `str`<a id="transfer_id-str"></a>

ID of the transfer to retrieve

#### 🔄 Return<a id="🔄-return"></a>

[`Transfer`](./dots_python_sdk/pydantic/transfer.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/organization-transfers/{transfer_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.transfers.list_all`<a id="dotstransferslist_all"></a>

List all transfers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_response = dots.transfers.list_all(
    limit=1,
    starting_after="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    ending_before="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    user_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

##### user_id: `str`<a id="user_id-str"></a>

Include only results with this user ID attached.

#### 🔄 Return<a id="🔄-return"></a>

[`TransfersListAllResponse`](./dots_python_sdk/pydantic/transfers_list_all_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/transfers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.add_payout_method`<a id="dotsusersadd_payout_method"></a>

Add a payout method to the user. Payout method can be one of `paypal`, `venmo`, `ach`, or `cash_app`. Each method has different required parameters.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_payout_method_response = dots.users.add_payout_method(
    platform="paypal",
    user_id="user_id_example",
    routing_number="string_example",
    account_number="string_example",
    account_type="checking",
    email="string_example",
    phone_number="string_example",
    handle="string_example",
    cash_tag="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### platform: `str`<a id="platform-str"></a>

Payout platform to add.

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

##### routing_number: `str`<a id="routing_number-str"></a>

Bank account or Cash App routing number. Required if `platform` = `ach` or `cash_app`.

##### account_number: `str`<a id="account_number-str"></a>

Bank account or Cash App account number. Required if `platform` = `ach` or `cash_app`.

##### account_type: `str`<a id="account_type-str"></a>

Bank account type. Required if `platform` = `ach`.

##### email: `str`<a id="email-str"></a>

PayPal email address. Required if `platform` = `paypal`.

##### phone_number: `str`<a id="phone_number-str"></a>

Venmo phone number. One of `phone_number` or `handle` is required if `platform` = `venmo`.

##### handle: `str`<a id="handle-str"></a>

Venmo handle. One of `phone_number` or `handle` is required if `platform` = `venmo`.

##### cash_tag: `str`<a id="cash_tag-str"></a>

Cash App Cash Tag. Required if `platform` = `cash_app`.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersAddPayoutMethodRequest`](./dots_python_sdk/type/users_add_payout_method_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PaymentMethod`](./dots_python_sdk/pydantic/payment_method.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}/payout-methods` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.create_new_user`<a id="dotsuserscreate_new_user"></a>

Create a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_user_response = dots.users.create_new_user(
    first_name="string_example",
    last_name="string_example",
    email="string_example",
    country_code="string_example",
    phone_number="string_example",
    username="a",
    metadata=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### first_name: `str`<a id="first_name-str"></a>

The user's first name.

##### last_name: `str`<a id="last_name-str"></a>

The user's last name.

##### email: `str`<a id="email-str"></a>

The user's email address.

##### country_code: `str`<a id="country_code-str"></a>

The user's phone number country code. e.g. \\\"1\\\"

##### phone_number: `str`<a id="phone_number-str"></a>

The user's phone number. e.g. \\\"4157223331\\\".

##### username: `str`<a id="username-str"></a>

Username to assign the user.

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersCreateNewUserRequest`](./dots_python_sdk/type/users_create_new_user_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./dots_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.get_user_by_id`<a id="dotsusersget_user_by_id"></a>

Get a user by their id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_user_by_id_response = dots.users.get_user_by_id(
    user_id="user_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./dots_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.list_all_users`<a id="dotsuserslist_all_users"></a>

List all users connected to your application.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_users_response = dots.users.list_all_users(
    starting_after="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    limit=1,
    ending_before="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### starting_after: `str`<a id="starting_after-str"></a>

A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `starting_after`=`aaa` in order to fetch the next page of the list.

##### limit: `int`<a id="limit-int"></a>

A limit on the number of objects to be returned, between 1 and 100.

##### ending_before: `str`<a id="ending_before-str"></a>

A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `aaa`, your subsequent call can include `ending_before`=`aaa` in order to fetch the previous page of the list.

#### 🔄 Return<a id="🔄-return"></a>

[`UsersListAllUsersResponse`](./dots_python_sdk/pydantic/users_list_all_users_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.list_payout_methods`<a id="dotsuserslist_payout_methods"></a>

Get a user's connected payout methods.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_payout_methods_response = dots.users.list_payout_methods(
    user_id="user_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

#### 🔄 Return<a id="🔄-return"></a>

[`UsersListPayoutMethodsResponse`](./dots_python_sdk/pydantic/users_list_payout_methods_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}/payout-methods` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.remove_user`<a id="dotsusersremove_user"></a>

Delete a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
remove_user_response = dots.users.remove_user(
    user_id="user_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

#### 🔄 Return<a id="🔄-return"></a>

[`User`](./dots_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.send_verification_token`<a id="dotsuserssend_verification_token"></a>

Send a user a verification token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dots.users.send_verification_token(
    user_id="user_id_example",
    use_voice=False,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

##### use_voice: `bool`<a id="use_voice-bool"></a>

Defaults to `false` which sends token via SMS. Set `true` to receive via call instead.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersSendVerificationTokenRequest`](./dots_python_sdk/type/users_send_verification_token_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}/send-verification-token` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.submit_compliance_info`<a id="dotsuserssubmit_compliance_info"></a>

Add Compliance information to a user.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dots.users.submit_compliance_info(
    user_id="user_id_example",
    w9={
        "entity_type": "individual",
        "date_of_birth": "1970-01-01",
        "tin": "tin_example",
        "address": {
            "line_1": "line_1_example",
            "city": "city_example",
            "state": "state_example",
            "country": "country_example",
            "postcode": "postcode_example",
        },
    },
    w8ben={
        "name": "name_example",
        "citizenship_country": "citizenship_country_example",
        "date_of_birth": "1970-01-01",
        "tin": "tin_example",
        "tax_treaty_income_type": "interest1",
        "address": {
            "line_1": "line_1_example",
            "city": "city_example",
            "state": "state_example",
            "country": "country_example",
            "postcode": "postcode_example",
        },
        "signature": {
            "consent": True,
            "name": "name_example",
            "email": "email_example",
        },
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

##### w9: [`UsersSubmitComplianceInfoRequestW9`](./dots_python_sdk/type/users_submit_compliance_info_request_w9.py)<a id="w9-userssubmitcomplianceinforequestw9dots_python_sdktypeusers_submit_compliance_info_request_w9py"></a>


##### w8ben: [`UsersSubmitComplianceInfoRequestW8Ben`](./dots_python_sdk/type/users_submit_compliance_info_request_w8_ben.py)<a id="w8ben-userssubmitcomplianceinforequestw8bendots_python_sdktypeusers_submit_compliance_info_request_w8_benpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersSubmitComplianceInfoRequest`](./dots_python_sdk/type/users_submit_compliance_info_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}/compliance` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.update_user_object`<a id="dotsusersupdate_user_object"></a>

Update mutable fields of a user object.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_user_object_response = dots.users.update_user_object(
    user_id="user_id_example",
    default_payout_method="paypal",
    auto_payout_enabled=True,
    metadata=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

##### default_payout_method: `str`<a id="default_payout_method-str"></a>

Configures the user's default payout method. Must be a payout method already configured by the user.

##### auto_payout_enabled: `bool`<a id="auto_payout_enabled-bool"></a>

Enables auto payout for the user whenever a default payout method is defined

##### metadata: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./dots_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="metadata-unionbool-date-datetime-dict-float-int-list-str-nonedots_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

Arbitrary metadata

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersUpdateUserObjectRequest`](./dots_python_sdk/type/users_update_user_object_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`User`](./dots_python_sdk/pydantic/user.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `dots.users.verify_user_token`<a id="dotsusersverify_user_token"></a>

Verify a user with a token.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
dots.users.verify_user_token(
    token="aaaaaa",
    user_id="user_id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### token: `str`<a id="token-str"></a>

The token sent to the user.

##### user_id: `str`<a id="user_id-str"></a>

Id of the user to fetch

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`UsersVerifyUserTokenRequest`](./dots_python_sdk/type/users_verify_user_token_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v2/users/{user_id}/verify` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
