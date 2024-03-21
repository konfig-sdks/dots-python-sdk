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


class PaymentsCreateTransactionRequest(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "amount",
            "platform",
        }
        
        class properties:
            amount = schemas.IntSchema
            
            
            class platform(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ACH(cls):
                    return cls("ach")
            user_id = schemas.UUIDSchema
            customer_id = schemas.UUIDSchema
        
            @staticmethod
            def ach_info() -> typing.Type['PaymentsCreateTransactionRequestAchInfo']:
                return PaymentsCreateTransactionRequestAchInfo
            account_id = schemas.AnyTypeSchema
            metadata = schemas.AnyTypeSchema
            __annotations__ = {
                "amount": amount,
                "platform": platform,
                "user_id": user_id,
                "customer_id": customer_id,
                "ach_info": ach_info,
                "account_id": account_id,
                "metadata": metadata,
            }
        
        
        class one_of_0(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "user_id",
                }
        
            
            user_id: schemas.AnyTypeSchema
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_0':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        
        class one_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                required = {
                    "customer_id",
                }
        
            
            customer_id: schemas.AnyTypeSchema
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'one_of_1':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def one_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                cls.one_of_0,
                cls.one_of_1,
            ]

    
    amount: MetaOapg.properties.amount
    platform: MetaOapg.properties.platform
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user_id"]) -> MetaOapg.properties.user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customer_id"]) -> MetaOapg.properties.customer_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ach_info"]) -> 'PaymentsCreateTransactionRequestAchInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_id"]) -> MetaOapg.properties.account_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "platform", "user_id", "customer_id", "ach_info", "account_id", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform"]) -> MetaOapg.properties.platform: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user_id"]) -> typing.Union[MetaOapg.properties.user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customer_id"]) -> typing.Union[MetaOapg.properties.customer_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ach_info"]) -> typing.Union['PaymentsCreateTransactionRequestAchInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_id"]) -> typing.Union[MetaOapg.properties.account_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "platform", "user_id", "customer_id", "ach_info", "account_id", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, ],
        platform: typing.Union[MetaOapg.properties.platform, str, ],
        user_id: typing.Union[MetaOapg.properties.user_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        customer_id: typing.Union[MetaOapg.properties.customer_id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        ach_info: typing.Union['PaymentsCreateTransactionRequestAchInfo', schemas.Unset] = schemas.unset,
        account_id: typing.Union[MetaOapg.properties.account_id, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentsCreateTransactionRequest':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            platform=platform,
            user_id=user_id,
            customer_id=customer_id,
            ach_info=ach_info,
            account_id=account_id,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )

from dots_python_sdk.model.payments_create_transaction_request_ach_info import PaymentsCreateTransactionRequestAchInfo
