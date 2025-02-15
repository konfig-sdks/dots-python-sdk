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


class PayoutrequestsSubmitRequestRequestPayee(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The payee's phone number. `user_id` or `payee` is required.
    """


    class MetaOapg:
        required = {
            "country_code",
            "phone_number",
        }
        
        class properties:
            country_code = schemas.StrSchema
            phone_number = schemas.StrSchema
            __annotations__ = {
                "country_code": country_code,
                "phone_number": phone_number,
            }
    
    country_code: MetaOapg.properties.country_code
    phone_number: MetaOapg.properties.phone_number
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["country_code", "phone_number", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["country_code", "phone_number", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country_code: typing.Union[MetaOapg.properties.country_code, str, ],
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayoutrequestsSubmitRequestRequestPayee':
        return super().__new__(
            cls,
            *args,
            country_code=country_code,
            phone_number=phone_number,
            _configuration=_configuration,
            **kwargs,
        )
