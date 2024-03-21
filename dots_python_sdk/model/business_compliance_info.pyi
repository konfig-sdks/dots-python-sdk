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


class BusinessComplianceInfo(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "flow_of_funds",
            "directors",
            "company_info",
            "contact_info",
        }
        
        class properties:
        
            @staticmethod
            def company_info() -> typing.Type['BusinessComplianceInfoCompanyInfo']:
                return BusinessComplianceInfoCompanyInfo
        
            @staticmethod
            def contact_info() -> typing.Type['BusinessComplianceInfoContactInfo']:
                return BusinessComplianceInfoContactInfo
        
            @staticmethod
            def directors() -> typing.Type['BusinessComplianceInfoDirectors']:
                return BusinessComplianceInfoDirectors
        
            @staticmethod
            def flow_of_funds() -> typing.Type['BusinessComplianceInfoFlowOfFunds']:
                return BusinessComplianceInfoFlowOfFunds
            __annotations__ = {
                "company_info": company_info,
                "contact_info": contact_info,
                "directors": directors,
                "flow_of_funds": flow_of_funds,
            }
    
    flow_of_funds: 'BusinessComplianceInfoFlowOfFunds'
    directors: 'BusinessComplianceInfoDirectors'
    company_info: 'BusinessComplianceInfoCompanyInfo'
    contact_info: 'BusinessComplianceInfoContactInfo'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["company_info"]) -> 'BusinessComplianceInfoCompanyInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact_info"]) -> 'BusinessComplianceInfoContactInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["directors"]) -> 'BusinessComplianceInfoDirectors': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flow_of_funds"]) -> 'BusinessComplianceInfoFlowOfFunds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["company_info", "contact_info", "directors", "flow_of_funds", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["company_info"]) -> 'BusinessComplianceInfoCompanyInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact_info"]) -> 'BusinessComplianceInfoContactInfo': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["directors"]) -> 'BusinessComplianceInfoDirectors': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flow_of_funds"]) -> 'BusinessComplianceInfoFlowOfFunds': ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["company_info", "contact_info", "directors", "flow_of_funds", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        flow_of_funds: 'BusinessComplianceInfoFlowOfFunds',
        directors: 'BusinessComplianceInfoDirectors',
        company_info: 'BusinessComplianceInfoCompanyInfo',
        contact_info: 'BusinessComplianceInfoContactInfo',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BusinessComplianceInfo':
        return super().__new__(
            cls,
            *args,
            flow_of_funds=flow_of_funds,
            directors=directors,
            company_info=company_info,
            contact_info=contact_info,
            _configuration=_configuration,
            **kwargs,
        )

from dots_python_sdk.model.business_compliance_info_company_info import BusinessComplianceInfoCompanyInfo
from dots_python_sdk.model.business_compliance_info_contact_info import BusinessComplianceInfoContactInfo
from dots_python_sdk.model.business_compliance_info_directors import BusinessComplianceInfoDirectors
from dots_python_sdk.model.business_compliance_info_flow_of_funds import BusinessComplianceInfoFlowOfFunds
