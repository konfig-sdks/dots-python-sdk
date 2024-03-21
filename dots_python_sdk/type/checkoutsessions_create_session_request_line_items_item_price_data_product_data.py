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

from dots_python_sdk.type.checkoutsessions_create_session_request_line_items_item_price_data_product_data_images import CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductDataImages

class RequiredCheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData(TypedDict):
    name: str

class OptionalCheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData(TypedDict, total=False):
    description: str

    images: CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductDataImages

    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData(RequiredCheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData, OptionalCheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData):
    pass
