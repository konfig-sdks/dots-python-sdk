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

from dots_python_sdk.model.refunds_create_refund_request import RefundsCreateRefundRequest as RefundsCreateRefundRequestSchema
from dots_python_sdk.model.refund import Refund as RefundSchema

from dots_python_sdk.type.refunds_create_refund_request import RefundsCreateRefundRequest
from dots_python_sdk.type.refund import Refund

from ...api_client import Dictionary
from dots_python_sdk.pydantic.refunds_create_refund_request import RefundsCreateRefundRequest as RefundsCreateRefundRequestPydantic
from dots_python_sdk.pydantic.refund import Refund as RefundPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = RefundsCreateRefundRequestSchema


request_body_refunds_create_refund_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = RefundSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Refund


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Refund


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

    def _create_refund_mapped_args(
        self,
        amount: int,
        payment_intent_id: str,
        reason: typing.Optional[str] = None,
        metadata: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if amount is not None:
            _body["amount"] = amount
        if payment_intent_id is not None:
            _body["payment_intent_id"] = payment_intent_id
        if reason is not None:
            _body["reason"] = reason
        if metadata is not None:
            _body["metadata"] = metadata
        args.body = _body
        return args

    async def _acreate_refund_oapg(
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
        Create a Refund
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
            path_template='/v2/refunds',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refunds_create_refund_request.serialize(body, content_type)
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


    def _create_refund_oapg(
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
        Create a Refund
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
            path_template='/v2/refunds',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refunds_create_refund_request.serialize(body, content_type)
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


class CreateRefundRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_refund(
        self,
        amount: int,
        payment_intent_id: str,
        reason: typing.Optional[str] = None,
        metadata: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_refund_mapped_args(
            amount=amount,
            payment_intent_id=payment_intent_id,
            reason=reason,
            metadata=metadata,
        )
        return await self._acreate_refund_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_refund(
        self,
        amount: int,
        payment_intent_id: str,
        reason: typing.Optional[str] = None,
        metadata: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_refund_mapped_args(
            amount=amount,
            payment_intent_id=payment_intent_id,
            reason=reason,
            metadata=metadata,
        )
        return self._create_refund_oapg(
            body=args.body,
        )

class CreateRefund(BaseApi):

    async def acreate_refund(
        self,
        amount: int,
        payment_intent_id: str,
        reason: typing.Optional[str] = None,
        metadata: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> RefundPydantic:
        raw_response = await self.raw.acreate_refund(
            amount=amount,
            payment_intent_id=payment_intent_id,
            reason=reason,
            metadata=metadata,
            **kwargs,
        )
        if validate:
            return RefundPydantic(**raw_response.body)
        return api_client.construct_model_instance(RefundPydantic, raw_response.body)
    
    
    def create_refund(
        self,
        amount: int,
        payment_intent_id: str,
        reason: typing.Optional[str] = None,
        metadata: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> RefundPydantic:
        raw_response = self.raw.create_refund(
            amount=amount,
            payment_intent_id=payment_intent_id,
            reason=reason,
            metadata=metadata,
        )
        if validate:
            return RefundPydantic(**raw_response.body)
        return api_client.construct_model_instance(RefundPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        amount: int,
        payment_intent_id: str,
        reason: typing.Optional[str] = None,
        metadata: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_refund_mapped_args(
            amount=amount,
            payment_intent_id=payment_intent_id,
            reason=reason,
            metadata=metadata,
        )
        return await self._acreate_refund_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        amount: int,
        payment_intent_id: str,
        reason: typing.Optional[str] = None,
        metadata: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_refund_mapped_args(
            amount=amount,
            payment_intent_id=payment_intent_id,
            reason=reason,
            metadata=metadata,
        )
        return self._create_refund_oapg(
            body=args.body,
        )

