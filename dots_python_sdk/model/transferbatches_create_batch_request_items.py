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


class TransferbatchesCreateBatchRequestItems(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['TransferbatchesCreateBatchRequestItemsItem']:
            return TransferbatchesCreateBatchRequestItemsItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['TransferbatchesCreateBatchRequestItemsItem'], typing.List['TransferbatchesCreateBatchRequestItemsItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'TransferbatchesCreateBatchRequestItems':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'TransferbatchesCreateBatchRequestItemsItem':
        return super().__getitem__(i)

from dots_python_sdk.model.transferbatches_create_batch_request_items_item import TransferbatchesCreateBatchRequestItemsItem
