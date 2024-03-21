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


class UsersAddPayoutMethodRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "platform",
        }
        
        class properties:
            
            
            class platform(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "paypal": "PAYPAL",
                        "venmo": "VENMO",
                        "cash_app": "CASH_APP",
                        "ach": "ACH",
                    }
                
                @schemas.classproperty
                def PAYPAL(cls):
                    return cls("paypal")
                
                @schemas.classproperty
                def VENMO(cls):
                    return cls("venmo")
                
                @schemas.classproperty
                def CASH_APP(cls):
                    return cls("cash_app")
                
                @schemas.classproperty
                def ACH(cls):
                    return cls("ach")
            routing_number = schemas.StrSchema
            account_number = schemas.StrSchema
            
            
            class account_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "checking": "CHECKING",
                        "savings": "SAVINGS",
                    }
                
                @schemas.classproperty
                def CHECKING(cls):
                    return cls("checking")
                
                @schemas.classproperty
                def SAVINGS(cls):
                    return cls("savings")
            email = schemas.StrSchema
            phone_number = schemas.StrSchema
            handle = schemas.StrSchema
            cash_tag = schemas.StrSchema
            __annotations__ = {
                "platform": platform,
                "routing_number": routing_number,
                "account_number": account_number,
                "account_type": account_type,
                "email": email,
                "phone_number": phone_number,
                "handle": handle,
                "cash_tag": cash_tag,
            }
    
    platform: MetaOapg.properties.platform
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routing_number"]) -> MetaOapg.properties.routing_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_number"]) -> MetaOapg.properties.account_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_type"]) -> MetaOapg.properties.account_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handle"]) -> MetaOapg.properties.handle: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cash_tag"]) -> MetaOapg.properties.cash_tag: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["platform", "routing_number", "account_number", "account_type", "email", "phone_number", "handle", "cash_tag", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routing_number"]) -> typing.Union[MetaOapg.properties.routing_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_number"]) -> typing.Union[MetaOapg.properties.account_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_type"]) -> typing.Union[MetaOapg.properties.account_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> typing.Union[MetaOapg.properties.phone_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handle"]) -> typing.Union[MetaOapg.properties.handle, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cash_tag"]) -> typing.Union[MetaOapg.properties.cash_tag, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["platform", "routing_number", "account_number", "account_type", "email", "phone_number", "handle", "cash_tag", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        platform: typing.Union[MetaOapg.properties.platform, str, ],
        routing_number: typing.Union[MetaOapg.properties.routing_number, str, schemas.Unset] = schemas.unset,
        account_number: typing.Union[MetaOapg.properties.account_number, str, schemas.Unset] = schemas.unset,
        account_type: typing.Union[MetaOapg.properties.account_type, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, str, schemas.Unset] = schemas.unset,
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, schemas.Unset] = schemas.unset,
        handle: typing.Union[MetaOapg.properties.handle, str, schemas.Unset] = schemas.unset,
        cash_tag: typing.Union[MetaOapg.properties.cash_tag, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersAddPayoutMethodRequest':
        return super().__new__(
            cls,
            *args,
            platform=platform,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            email=email,
            phone_number=phone_number,
            handle=handle,
            cash_tag=cash_tag,
            _configuration=_configuration,
            **kwargs,
        )
