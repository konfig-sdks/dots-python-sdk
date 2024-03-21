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


class BusinessComplianceInfoDirectorsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "address",
            "phone",
            "dob",
            "last_name",
            "title",
            "first_name",
            "email",
            "ownership_percentage",
        }
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def address() -> typing.Type['BusinessComplianceInfoDirectorsItemAddress']:
                return BusinessComplianceInfoDirectorsItemAddress
            dob = schemas.DateSchema
            
            
            class email(
                schemas.StrSchema
            ):
                pass
            
            
            class first_name(
                schemas.StrSchema
            ):
                pass
            
            
            class last_name(
                schemas.StrSchema
            ):
                pass
            ownership_percentage = schemas.NumberSchema
            
            
            class phone(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "title": title,
                "address": address,
                "dob": dob,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
                "ownership_percentage": ownership_percentage,
                "phone": phone,
            }
    
    address: 'BusinessComplianceInfoDirectorsItemAddress'
    phone: MetaOapg.properties.phone
    dob: MetaOapg.properties.dob
    last_name: MetaOapg.properties.last_name
    title: MetaOapg.properties.title
    first_name: MetaOapg.properties.first_name
    email: MetaOapg.properties.email
    ownership_percentage: MetaOapg.properties.ownership_percentage
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'BusinessComplianceInfoDirectorsItemAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dob"]) -> MetaOapg.properties.dob: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ownership_percentage"]) -> MetaOapg.properties.ownership_percentage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "address", "dob", "email", "first_name", "last_name", "ownership_percentage", "phone", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> 'BusinessComplianceInfoDirectorsItemAddress': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dob"]) -> MetaOapg.properties.dob: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["first_name"]) -> MetaOapg.properties.first_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_name"]) -> MetaOapg.properties.last_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ownership_percentage"]) -> MetaOapg.properties.ownership_percentage: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "address", "dob", "email", "first_name", "last_name", "ownership_percentage", "phone", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: 'BusinessComplianceInfoDirectorsItemAddress',
        phone: typing.Union[MetaOapg.properties.phone, str, ],
        dob: typing.Union[MetaOapg.properties.dob, str, date, ],
        last_name: typing.Union[MetaOapg.properties.last_name, str, ],
        title: typing.Union[MetaOapg.properties.title, str, ],
        first_name: typing.Union[MetaOapg.properties.first_name, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        ownership_percentage: typing.Union[MetaOapg.properties.ownership_percentage, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BusinessComplianceInfoDirectorsItem':
        return super().__new__(
            cls,
            *args,
            address=address,
            phone=phone,
            dob=dob,
            last_name=last_name,
            title=title,
            first_name=first_name,
            email=email,
            ownership_percentage=ownership_percentage,
            _configuration=_configuration,
            **kwargs,
        )

from dots_python_sdk.model.business_compliance_info_directors_item_address import BusinessComplianceInfoDirectorsItemAddress
