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


class PayoutsCreatePayoutRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "amount",
            "user_id",
            "platform",
        }
        
        class properties:
            user_id = schemas.UUIDSchema
            amount = schemas.IntSchema
            
            
            class platform(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "paypal": "PAYPAL",
                        "venmo": "VENMO",
                        "ach": "ACH",
                        "bank_transfer": "BANK_TRANSFER",
                        "cash_app": "CASH_APP",
                        "payoneer": "PAYONEER",
                        "airtm": "AIRTM",
                        "default": "DEFAULT",
                    }
                
                @schemas.classproperty
                def PAYPAL(cls):
                    return cls("paypal")
                
                @schemas.classproperty
                def VENMO(cls):
                    return cls("venmo")
                
                @schemas.classproperty
                def ACH(cls):
                    return cls("ach")
                
                @schemas.classproperty
                def BANK_TRANSFER(cls):
                    return cls("bank_transfer")
                
                @schemas.classproperty
                def CASH_APP(cls):
                    return cls("cash_app")
                
                @schemas.classproperty
                def PAYONEER(cls):
                    return cls("payoneer")
                
                @schemas.classproperty
                def AIRTM(cls):
                    return cls("airtm")
                
                @schemas.classproperty
                def DEFAULT(cls):
                    return cls("default")
            account_id = schemas.StrSchema
            fund = schemas.BoolSchema
            idempotency_key = schemas.UUIDSchema
            metadata = schemas.AnyTypeSchema
            __annotations__ = {
                "user_id": user_id,
                "amount": amount,
                "platform": platform,
                "account_id": account_id,
                "fund": fund,
                "idempotency_key": idempotency_key,
                "metadata": metadata,
            }
    
    amount: MetaOapg.properties.amount
    user_id: MetaOapg.properties.user_id
    platform: MetaOapg.properties.platform
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fund"]) -> MetaOapg.properties.fund: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idempotency_key"]) -> MetaOapg.properties.idempotency_key: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user_id", "amount", "platform", "account_id", "fund", "idempotency_key", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fund"]) -> typing.Union[MetaOapg.properties.fund, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idempotency_key"]) -> typing.Union[MetaOapg.properties.idempotency_key, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user_id", "amount", "platform", "account_id", "fund", "idempotency_key", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, uuid.UUID, ],
        platform: typing.Union[MetaOapg.properties.platform, str, ],
        account_id: typing.Union[MetaOapg.properties.account_id, str, schemas.Unset] = schemas.unset,
        fund: typing.Union[MetaOapg.properties.fund, bool, schemas.Unset] = schemas.unset,
        idempotency_key: typing.Union[MetaOapg.properties.idempotency_key, str, uuid.UUID, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayoutsCreatePayoutRequest':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            user_id=user_id,
            platform=platform,
            account_id=account_id,
            fund=fund,
            idempotency_key=idempotency_key,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )
