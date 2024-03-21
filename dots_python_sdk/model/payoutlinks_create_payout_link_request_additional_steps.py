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


class PayoutlinksCreatePayoutLinkRequestAdditionalSteps(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    Array of steps in the flow.
    """


    class MetaOapg:
        
        
        class items(
            schemas.EnumBase,
            schemas.StrSchema
        ):
        
        
            class MetaOapg:
                enum_value_to_name = {
                    "compliance": "COMPLIANCE",
                    "id-verification": "IDVERIFICATION",
                    "background-check": "BACKGROUNDCHECK",
                    "manage-payments": "MANAGEPAYMENTS",
                    "manage-payouts": "MANAGEPAYOUTS",
                    "payout": "PAYOUT",
                    "redirect": "REDIRECT",
                }
            
            @schemas.classproperty
            def COMPLIANCE(cls):
                return cls("compliance")
            
            @schemas.classproperty
            def IDVERIFICATION(cls):
                return cls("id-verification")
            
            @schemas.classproperty
            def BACKGROUNDCHECK(cls):
                return cls("background-check")
            
            @schemas.classproperty
            def MANAGEPAYMENTS(cls):
                return cls("manage-payments")
            
            @schemas.classproperty
            def MANAGEPAYOUTS(cls):
                return cls("manage-payouts")
            
            @schemas.classproperty
            def PAYOUT(cls):
                return cls("payout")
            
            @schemas.classproperty
            def REDIRECT(cls):
                return cls("redirect")

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'PayoutlinksCreatePayoutLinkRequestAdditionalSteps':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
