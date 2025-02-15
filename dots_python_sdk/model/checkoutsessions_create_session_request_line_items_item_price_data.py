# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from dots_python_sdk import schemas  # noqa: F401


class CheckoutsessionsCreateSessionRequestLineItemsItemPriceData(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "amount",
            "currency",
            "product_data",
        }
        
        class properties:
            
            
            class currency(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "usd": "USD",
                    }
                
                @schemas.classproperty
                def USD(cls):
                    return cls("usd")
            amount = schemas.IntSchema
        
            @staticmethod
            def product_data() -> typing.Type['CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData']:
                return CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData
            __annotations__ = {
                "currency": currency,
                "amount": amount,
                "product_data": product_data,
            }
    
    amount: MetaOapg.properties.amount
    currency: MetaOapg.properties.currency
    product_data: 'CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product_data"]) -> 'CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["currency", "amount", "product_data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product_data"]) -> 'CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["currency", "amount", "product_data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        product_data: 'CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CheckoutsessionsCreateSessionRequestLineItemsItemPriceData':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            currency=currency,
            product_data=product_data,
            _configuration=_configuration,
            **kwargs,
        )

from dots_python_sdk.model.checkoutsessions_create_session_request_line_items_item_price_data_product_data import CheckoutsessionsCreateSessionRequestLineItemsItemPriceDataProductData
