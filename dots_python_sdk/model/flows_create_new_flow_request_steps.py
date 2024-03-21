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


class FlowsCreateNewFlowRequestSteps(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)

    A list of steps. Can either be a string or an object with additional properties. Example: A `redirect` step looks like {"name": "redirect", "redirect_url": "https://example.com"}
    """


    class MetaOapg:
        unique_items = True
        
        
        class items(
            schemas.ComposedSchema,
        ):
        
        
            class MetaOapg:
                
                
                class one_of_0(
                    schemas.EnumBase,
                    schemas.StrSchema
                ):
                
                
                    class MetaOapg:
                        enum_value_to_name = {
                            "compliance": "COMPLIANCE",
                            "id-verification": "IDVERIFICATION",
                            "manage-payouts": "MANAGEPAYOUTS",
                            "manage-payments": "MANAGEPAYMENTS",
                            "payout": "PAYOUT",
                            "background-check": "BACKGROUNDCHECK",
                            "redirect": "REDIRECT",
                        }
                    
                    @schemas.classproperty
                    def COMPLIANCE(cls):
                        return cls("compliance")
                    
                    @schemas.classproperty
                    def IDVERIFICATION(cls):
                        return cls("id-verification")
                    
                    @schemas.classproperty
                    def MANAGEPAYOUTS(cls):
                        return cls("manage-payouts")
                    
                    @schemas.classproperty
                    def MANAGEPAYMENTS(cls):
                        return cls("manage-payments")
                    
                    @schemas.classproperty
                    def PAYOUT(cls):
                        return cls("payout")
                    
                    @schemas.classproperty
                    def BACKGROUNDCHECK(cls):
                        return cls("background-check")
                    
                    @schemas.classproperty
                    def REDIRECT(cls):
                        return cls("redirect")
                
                
                class one_of_1(
                    schemas.DictSchema
                ):
                
                
                    class MetaOapg:
                        required = {
                            "name",
                        }
                        
                        class properties:
                            
                            
                            class name(
                                schemas.EnumBase,
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    enum_value_to_name = {
                                        "compliance": "COMPLIANCE",
                                        "id-verification": "IDVERIFICATION",
                                        "manage-payouts": "MANAGEPAYOUTS",
                                        "manage-payments": "MANAGEPAYMENTS",
                                        "payout": "PAYOUT",
                                        "background-check": "BACKGROUNDCHECK",
                                        "redirect": "REDIRECT",
                                    }
                                
                                @schemas.classproperty
                                def COMPLIANCE(cls):
                                    return cls("compliance")
                                
                                @schemas.classproperty
                                def IDVERIFICATION(cls):
                                    return cls("id-verification")
                                
                                @schemas.classproperty
                                def MANAGEPAYOUTS(cls):
                                    return cls("manage-payouts")
                                
                                @schemas.classproperty
                                def MANAGEPAYMENTS(cls):
                                    return cls("manage-payments")
                                
                                @schemas.classproperty
                                def PAYOUT(cls):
                                    return cls("payout")
                                
                                @schemas.classproperty
                                def BACKGROUNDCHECK(cls):
                                    return cls("background-check")
                                
                                @schemas.classproperty
                                def REDIRECT(cls):
                                    return cls("redirect")
                            auto_payout_enabled = schemas.BoolSchema
                            
                            
                            class redirect_url(
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                                    format = 'uri'
                                    regex=[{
                                        'pattern': r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)',
                                    }]
                            hide_continue_button = schemas.BoolSchema
                            __annotations__ = {
                                "name": name,
                                "auto_payout_enabled": auto_payout_enabled,
                                "redirect_url": redirect_url,
                                "hide_continue_button": hide_continue_button,
                            }
                    
                    name: MetaOapg.properties.name
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["auto_payout_enabled"]) -> MetaOapg.properties.auto_payout_enabled: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["redirect_url"]) -> MetaOapg.properties.redirect_url: ...
                    
                    @typing.overload
                    def __getitem__(self, name: typing_extensions.Literal["hide_continue_button"]) -> MetaOapg.properties.hide_continue_button: ...
                    
                    @typing.overload
                    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                    
                    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "auto_payout_enabled", "redirect_url", "hide_continue_button", ], str]):
                        # dict_instance[name] accessor
                        return super().__getitem__(name)
                    
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["auto_payout_enabled"]) -> typing.Union[MetaOapg.properties.auto_payout_enabled, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["redirect_url"]) -> typing.Union[MetaOapg.properties.redirect_url, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: typing_extensions.Literal["hide_continue_button"]) -> typing.Union[MetaOapg.properties.hide_continue_button, schemas.Unset]: ...
                    
                    @typing.overload
                    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                    
                    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "auto_payout_enabled", "redirect_url", "hide_continue_button", ], str]):
                        return super().get_item_oapg(name)
                    
                
                    def __new__(
                        cls,
                        *args: typing.Union[dict, frozendict.frozendict, ],
                        name: typing.Union[MetaOapg.properties.name, str, ],
                        auto_payout_enabled: typing.Union[MetaOapg.properties.auto_payout_enabled, bool, schemas.Unset] = schemas.unset,
                        redirect_url: typing.Union[MetaOapg.properties.redirect_url, str, schemas.Unset] = schemas.unset,
                        hide_continue_button: typing.Union[MetaOapg.properties.hide_continue_button, bool, schemas.Unset] = schemas.unset,
                        _configuration: typing.Optional[schemas.Configuration] = None,
                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                    ) -> 'one_of_1':
                        return super().__new__(
                            cls,
                            *args,
                            name=name,
                            auto_payout_enabled=auto_payout_enabled,
                            redirect_url=redirect_url,
                            hide_continue_button=hide_continue_button,
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
        
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'items':
                return super().__new__(
                    cls,
                    *args,
                    _configuration=_configuration,
                    **kwargs,
                )

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'FlowsCreateNewFlowRequestSteps':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
