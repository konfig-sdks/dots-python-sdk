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


class UserCompliance(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            tax_id_collected = schemas.BoolSchema
            address_collected = schemas.BoolSchema
            date_of_birth_collected = schemas.BoolSchema
            must_collect_1099 = schemas.BoolSchema
            _1099_collected = schemas.BoolSchema
            w8_ben_collected = schemas.BoolSchema
            flagged = schemas.BoolSchema
            id_verified = schemas.BoolSchema
            __annotations__ = {
                "tax_id_collected": tax_id_collected,
                "address_collected": address_collected,
                "date_of_birth_collected": date_of_birth_collected,
                "must_collect_1099": must_collect_1099,
                "1099_collected": _1099_collected,
                "w8_ben_collected": w8_ben_collected,
                "flagged": flagged,
                "id_verified": id_verified,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_id_collected"]) -> MetaOapg.properties.tax_id_collected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address_collected"]) -> MetaOapg.properties.address_collected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["date_of_birth_collected"]) -> MetaOapg.properties.date_of_birth_collected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["must_collect_1099"]) -> MetaOapg.properties.must_collect_1099: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["1099_collected"]) -> MetaOapg.properties._1099_collected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["w8_ben_collected"]) -> MetaOapg.properties.w8_ben_collected: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["flagged"]) -> MetaOapg.properties.flagged: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id_verified"]) -> MetaOapg.properties.id_verified: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tax_id_collected", "address_collected", "date_of_birth_collected", "must_collect_1099", "1099_collected", "w8_ben_collected", "flagged", "id_verified", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_id_collected"]) -> typing.Union[MetaOapg.properties.tax_id_collected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address_collected"]) -> typing.Union[MetaOapg.properties.address_collected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["date_of_birth_collected"]) -> typing.Union[MetaOapg.properties.date_of_birth_collected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["must_collect_1099"]) -> typing.Union[MetaOapg.properties.must_collect_1099, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["1099_collected"]) -> typing.Union[MetaOapg.properties._1099_collected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["w8_ben_collected"]) -> typing.Union[MetaOapg.properties.w8_ben_collected, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["flagged"]) -> typing.Union[MetaOapg.properties.flagged, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id_verified"]) -> typing.Union[MetaOapg.properties.id_verified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tax_id_collected", "address_collected", "date_of_birth_collected", "must_collect_1099", "1099_collected", "w8_ben_collected", "flagged", "id_verified", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tax_id_collected: typing.Union[MetaOapg.properties.tax_id_collected, bool, schemas.Unset] = schemas.unset,
        address_collected: typing.Union[MetaOapg.properties.address_collected, bool, schemas.Unset] = schemas.unset,
        date_of_birth_collected: typing.Union[MetaOapg.properties.date_of_birth_collected, bool, schemas.Unset] = schemas.unset,
        must_collect_1099: typing.Union[MetaOapg.properties.must_collect_1099, bool, schemas.Unset] = schemas.unset,
        w8_ben_collected: typing.Union[MetaOapg.properties.w8_ben_collected, bool, schemas.Unset] = schemas.unset,
        flagged: typing.Union[MetaOapg.properties.flagged, bool, schemas.Unset] = schemas.unset,
        id_verified: typing.Union[MetaOapg.properties.id_verified, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserCompliance':
        return super().__new__(
            cls,
            *args,
            tax_id_collected=tax_id_collected,
            address_collected=address_collected,
            date_of_birth_collected=date_of_birth_collected,
            must_collect_1099=must_collect_1099,
            w8_ben_collected=w8_ben_collected,
            flagged=flagged,
            id_verified=id_verified,
            _configuration=_configuration,
            **kwargs,
        )
