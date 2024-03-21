# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from dots_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from dots_python_sdk.api_response import AsyncGeneratorResponse
from dots_python_sdk import api_client, exceptions
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

from dots_python_sdk.model.transferbatches_create_batch_request import TransferbatchesCreateBatchRequest as TransferbatchesCreateBatchRequestSchema
from dots_python_sdk.model.transferbatches_create_batch_request_items import TransferbatchesCreateBatchRequestItems as TransferbatchesCreateBatchRequestItemsSchema
from dots_python_sdk.model.transferbatches_create_batch_response import TransferbatchesCreateBatchResponse as TransferbatchesCreateBatchResponseSchema

from dots_python_sdk.type.transferbatches_create_batch_response import TransferbatchesCreateBatchResponse
from dots_python_sdk.type.transferbatches_create_batch_request import TransferbatchesCreateBatchRequest
from dots_python_sdk.type.transferbatches_create_batch_request_items import TransferbatchesCreateBatchRequestItems

from ...api_client import Dictionary
from dots_python_sdk.pydantic.transferbatches_create_batch_request import TransferbatchesCreateBatchRequest as TransferbatchesCreateBatchRequestPydantic
from dots_python_sdk.pydantic.transferbatches_create_batch_response import TransferbatchesCreateBatchResponse as TransferbatchesCreateBatchResponsePydantic
from dots_python_sdk.pydantic.transferbatches_create_batch_request_items import TransferbatchesCreateBatchRequestItems as TransferbatchesCreateBatchRequestItemsPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TransferbatchesCreateBatchRequestSchema
SchemaForRequestBodyApplicationXml = schemas.DictSchema


request_body_transferbatches_create_batch_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
    },
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = TransferbatchesCreateBatchResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: TransferbatchesCreateBatchResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: TransferbatchesCreateBatchResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_batch_mapped_args(
        self,
        items: typing.Optional[TransferbatchesCreateBatchRequestItems] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if items is not None:
            _body["items"] = items
        if idempotency_key is not None:
            _body["idempotency_key"] = idempotency_key
        if metadata is not None:
            _body["metadata"] = metadata
        args.body = _body
        return args

    async def _acreate_batch_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a Transfer Batch
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/transfer-batches',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_transferbatches_create_batch_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_batch_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a Transfer Batch
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/transfer-batches',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_transferbatches_create_batch_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateBatchRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_batch(
        self,
        items: typing.Optional[TransferbatchesCreateBatchRequestItems] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_batch_mapped_args(
            items=items,
            idempotency_key=idempotency_key,
            metadata=metadata,
        )
        return await self._acreate_batch_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_batch(
        self,
        items: typing.Optional[TransferbatchesCreateBatchRequestItems] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_batch_mapped_args(
            items=items,
            idempotency_key=idempotency_key,
            metadata=metadata,
        )
        return self._create_batch_oapg(
            body=args.body,
        )

class CreateBatch(BaseApi):

    async def acreate_batch(
        self,
        items: typing.Optional[TransferbatchesCreateBatchRequestItems] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
        **kwargs,
    ) -> TransferbatchesCreateBatchResponsePydantic:
        raw_response = await self.raw.acreate_batch(
            items=items,
            idempotency_key=idempotency_key,
            metadata=metadata,
            **kwargs,
        )
        if validate:
            return TransferbatchesCreateBatchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TransferbatchesCreateBatchResponsePydantic, raw_response.body)
    
    
    def create_batch(
        self,
        items: typing.Optional[TransferbatchesCreateBatchRequestItems] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        validate: bool = False,
    ) -> TransferbatchesCreateBatchResponsePydantic:
        raw_response = self.raw.create_batch(
            items=items,
            idempotency_key=idempotency_key,
            metadata=metadata,
        )
        if validate:
            return TransferbatchesCreateBatchResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(TransferbatchesCreateBatchResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        items: typing.Optional[TransferbatchesCreateBatchRequestItems] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_batch_mapped_args(
            items=items,
            idempotency_key=idempotency_key,
            metadata=metadata,
        )
        return await self._acreate_batch_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        items: typing.Optional[TransferbatchesCreateBatchRequestItems] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_batch_mapped_args(
            items=items,
            idempotency_key=idempotency_key,
            metadata=metadata,
        )
        return self._create_batch_oapg(
            body=args.body,
        )

