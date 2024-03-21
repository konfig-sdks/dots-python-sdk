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


class UsersCreateNewUserRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "country_code",
            "last_name",
            "phone_number",
            "first_name",
            "email",
        }
        
        class properties:
            first_name = schemas.StrSchema
            last_name = schemas.StrSchema
            email = schemas.StrSchema
            country_code = schemas.StrSchema
            phone_number = schemas.StrSchema
            
            
            class username(
                schemas.StrSchema
            ):
                pass
            metadata = schemas.AnyTypeSchema
            __annotations__ = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "country_code": country_code,
                "phone_number": phone_number,
                "username": username,
                "metadata": metadata,
            }
    
    country_code: MetaOapg.properties.country_code
    last_name: MetaOapg.properties.last_name
    phone_number: MetaOapg.properties.phone_number
    first_name: MetaOapg.properties.first_name
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "email", "country_code", "phone_number", "username", "metadata", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_code"]) -> MetaOapg.properties.country_code: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone_number"]) -> MetaOapg.properties.phone_number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["first_name", "last_name", "email", "country_code", "phone_number", "username", "metadata", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        country_code: typing.Union[MetaOapg.properties.country_code, str, ],
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        phone_number: typing.Union[MetaOapg.properties.phone_number, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersCreateNewUserRequest':
        return super().__new__(
            cls,
            *args,
            country_code=country_code,
            last_name=last_name,
            phone_number=phone_number,
            first_name=first_name,
            email=email,
            username=username,
            metadata=metadata,
            _configuration=_configuration,
            **kwargs,
        )
