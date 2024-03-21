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


class UsersSubmitComplianceInfoRequestW8Ben(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    W8-BEN form for foreign payees.
    """


    class MetaOapg:
        required = {
            "address",
            "signature",
            "date_of_birth",
            "name",
            "tin",
            "citizenship_country",
        }
        
        class properties:
            name = schemas.StrSchema
            citizenship_country = schemas.StrSchema
            date_of_birth = schemas.DateSchema
            
            
            class tin(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 9
                    min_length = 9
        
            @staticmethod
            def address() -> typing.Type['UsersSubmitComplianceInfoRequestW8BenAddress']:
                return UsersSubmitComplianceInfoRequestW8BenAddress
        
            @staticmethod
            def signature() -> typing.Type['UsersSubmitComplianceInfoRequestW8BenSignature']:
                return UsersSubmitComplianceInfoRequestW8BenSignature
            foreign_tax_id = schemas.StrSchema
            tax_treaty_country = schemas.StrSchema
            tax_treaty_citation = schemas.StrSchema
            tax_treaty_rate = schemas.NumberSchema
            
            
            class tax_treaty_income_type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "interest1": "INTEREST1",
                        "dividend6": "DIVIDEND6",
                        "dividend7": "DIVIDEND7",
                        "pension15": "PENSION15",
                        "socialSecurity": "SOCIAL_SECURITY",
                        "equipment10": "EQUIPMENT10",
                        "knowhow10": "KNOWHOW10",
                        "patent10": "PATENT10",
                        "film11": "FILM11",
                        "copyright12": "COPYRIGHT12",
                    }
                
                @schemas.classproperty
                def INTEREST1(cls):
                    return cls("interest1")
                
                @schemas.classproperty
                def DIVIDEND6(cls):
                    return cls("dividend6")
                
                @schemas.classproperty
                def DIVIDEND7(cls):
                    return cls("dividend7")
                
                @schemas.classproperty
                def PENSION15(cls):
                    return cls("pension15")
                
                @schemas.classproperty
                def SOCIAL_SECURITY(cls):
                    return cls("socialSecurity")
                
                @schemas.classproperty
                def EQUIPMENT10(cls):
                    return cls("equipment10")
                
                @schemas.classproperty
                def KNOWHOW10(cls):
                    return cls("knowhow10")
                
                @schemas.classproperty
                def PATENT10(cls):
                    return cls("patent10")
                
                @schemas.classproperty
                def FILM11(cls):
                    return cls("film11")
                
                @schemas.classproperty
                def COPYRIGHT12(cls):
                    return cls("copyright12")
            tax_treaty_explanation = schemas.StrSchema
            __annotations__ = {
                "name": name,
                "citizenship_country": citizenship_country,
                "date_of_birth": date_of_birth,
                "tin": tin,
                "address": address,
                "signature": signature,
                "foreign_tax_id": foreign_tax_id,
                "tax_treaty_country": tax_treaty_country,
                "tax_treaty_citation": tax_treaty_citation,
                "tax_treaty_rate": tax_treaty_rate,
                "tax_treaty_income_type": tax_treaty_income_type,
                "tax_treaty_explanation": tax_treaty_explanation,
            }
    
    address: 'UsersSubmitComplianceInfoRequestW8BenAddress'
    signature: 'UsersSubmitComplianceInfoRequestW8BenSignature'
    date_of_birth: MetaOapg.properties.date_of_birth
    name: MetaOapg.properties.name
    tin: MetaOapg.properties.tin
    citizenship_country: MetaOapg.properties.citizenship_country
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["citizenship_country"]) -> MetaOapg.properties.citizenship_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_of_birth"]) -> MetaOapg.properties.date_of_birth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tin"]) -> MetaOapg.properties.tin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> 'UsersSubmitComplianceInfoRequestW8BenAddress': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signature"]) -> 'UsersSubmitComplianceInfoRequestW8BenSignature': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["foreign_tax_id"]) -> MetaOapg.properties.foreign_tax_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_treaty_country"]) -> MetaOapg.properties.tax_treaty_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_treaty_citation"]) -> MetaOapg.properties.tax_treaty_citation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_treaty_rate"]) -> MetaOapg.properties.tax_treaty_rate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_treaty_income_type"]) -> MetaOapg.properties.tax_treaty_income_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_treaty_explanation"]) -> MetaOapg.properties.tax_treaty_explanation: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "citizenship_country", "date_of_birth", "tin", "address", "signature", "foreign_tax_id", "tax_treaty_country", "tax_treaty_citation", "tax_treaty_rate", "tax_treaty_income_type", "tax_treaty_explanation", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["citizenship_country"]) -> MetaOapg.properties.citizenship_country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_of_birth"]) -> MetaOapg.properties.date_of_birth: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tin"]) -> MetaOapg.properties.tin: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> 'UsersSubmitComplianceInfoRequestW8BenAddress': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signature"]) -> 'UsersSubmitComplianceInfoRequestW8BenSignature': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["foreign_tax_id"]) -> typing.Union[MetaOapg.properties.foreign_tax_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_treaty_country"]) -> typing.Union[MetaOapg.properties.tax_treaty_country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_treaty_citation"]) -> typing.Union[MetaOapg.properties.tax_treaty_citation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_treaty_rate"]) -> typing.Union[MetaOapg.properties.tax_treaty_rate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_treaty_income_type"]) -> typing.Union[MetaOapg.properties.tax_treaty_income_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_treaty_explanation"]) -> typing.Union[MetaOapg.properties.tax_treaty_explanation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "citizenship_country", "date_of_birth", "tin", "address", "signature", "foreign_tax_id", "tax_treaty_country", "tax_treaty_citation", "tax_treaty_rate", "tax_treaty_income_type", "tax_treaty_explanation", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        address: 'UsersSubmitComplianceInfoRequestW8BenAddress',
        signature: 'UsersSubmitComplianceInfoRequestW8BenSignature',
        date_of_birth: typing.Union[MetaOapg.properties.date_of_birth, str, date, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        tin: typing.Union[MetaOapg.properties.tin, str, ],
        citizenship_country: typing.Union[MetaOapg.properties.citizenship_country, str, ],
        foreign_tax_id: typing.Union[MetaOapg.properties.foreign_tax_id, str, schemas.Unset] = schemas.unset,
        tax_treaty_country: typing.Union[MetaOapg.properties.tax_treaty_country, str, schemas.Unset] = schemas.unset,
        tax_treaty_citation: typing.Union[MetaOapg.properties.tax_treaty_citation, str, schemas.Unset] = schemas.unset,
        tax_treaty_rate: typing.Union[MetaOapg.properties.tax_treaty_rate, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tax_treaty_income_type: typing.Union[MetaOapg.properties.tax_treaty_income_type, str, schemas.Unset] = schemas.unset,
        tax_treaty_explanation: typing.Union[MetaOapg.properties.tax_treaty_explanation, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UsersSubmitComplianceInfoRequestW8Ben':
        return super().__new__(
            cls,
            *args,
            address=address,
            signature=signature,
            date_of_birth=date_of_birth,
            name=name,
            tin=tin,
            citizenship_country=citizenship_country,
            foreign_tax_id=foreign_tax_id,
            tax_treaty_country=tax_treaty_country,
            tax_treaty_citation=tax_treaty_citation,
            tax_treaty_rate=tax_treaty_rate,
            tax_treaty_income_type=tax_treaty_income_type,
            tax_treaty_explanation=tax_treaty_explanation,
            _configuration=_configuration,
            **kwargs,
        )

from dots_python_sdk.model.users_submit_compliance_info_request_w8_ben_address import UsersSubmitComplianceInfoRequestW8BenAddress
from dots_python_sdk.model.users_submit_compliance_info_request_w8_ben_signature import UsersSubmitComplianceInfoRequestW8BenSignature
