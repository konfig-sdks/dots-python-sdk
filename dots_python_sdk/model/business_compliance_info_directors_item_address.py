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


class BusinessComplianceInfoDirectorsItemAddress(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "zip",
            "country",
            "city",
            "line1",
        }
        
        class properties:
            
            
            class city(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
                    min_length = 1
            
            
            class country(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 60
                    min_length = 2
            
            
            class line1(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
                    min_length = 1
            
            
            class zip(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
                    min_length = 3
            
            
            class line2(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
                    min_length = 1
            
            
            class state(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 60
                    min_length = 1
            __annotations__ = {
                "city": city,
                "country": country,
                "line1": line1,
                "zip": zip,
                "line2": line2,
                "state": state,
            }
    
    zip: MetaOapg.properties.zip
    country: MetaOapg.properties.country
    city: MetaOapg.properties.city
    line1: MetaOapg.properties.line1
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line1"]) -> MetaOapg.properties.line1: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line2"]) -> MetaOapg.properties.line2: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state"]) -> MetaOapg.properties.state: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["city", "country", "line1", "zip", "line2", "state", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line1"]) -> MetaOapg.properties.line1: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zip"]) -> MetaOapg.properties.zip: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line2"]) -> typing.Union[MetaOapg.properties.line2, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state"]) -> typing.Union[MetaOapg.properties.state, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["city", "country", "line1", "zip", "line2", "state", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        zip: typing.Union[MetaOapg.properties.zip, str, ],
        country: typing.Union[MetaOapg.properties.country, str, ],
        city: typing.Union[MetaOapg.properties.city, str, ],
        line1: typing.Union[MetaOapg.properties.line1, str, ],
        line2: typing.Union[MetaOapg.properties.line2, str, schemas.Unset] = schemas.unset,
        state: typing.Union[MetaOapg.properties.state, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BusinessComplianceInfoDirectorsItemAddress':
        return super().__new__(
            cls,
            *args,
            zip=zip,
            country=country,
            city=city,
            line1=line1,
            line2=line2,
            state=state,
            _configuration=_configuration,
            **kwargs,
        )
