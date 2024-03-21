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

from dots_python_sdk.model.payment_method import PaymentMethod as PaymentMethodSchema
from dots_python_sdk.model.users_add_payout_method_request import UsersAddPayoutMethodRequest as UsersAddPayoutMethodRequestSchema

from dots_python_sdk.type.payment_method import PaymentMethod
from dots_python_sdk.type.users_add_payout_method_request import UsersAddPayoutMethodRequest

from ...api_client import Dictionary
from dots_python_sdk.pydantic.payment_method import PaymentMethod as PaymentMethodPydantic
from dots_python_sdk.pydantic.users_add_payout_method_request import UsersAddPayoutMethodRequest as UsersAddPayoutMethodRequestPydantic

# Path params
UserIdSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'user_id': typing.Union[UserIdSchema, str, uuid.UUID, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_user_id = api_client.PathParameter(
    name="user_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=UserIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = UsersAddPayoutMethodRequestSchema


request_body_users_add_payout_method_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = PaymentMethodSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentMethod


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentMethod


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _add_payout_method_mapped_args(
        self,
        platform: str,
        user_id: str,
        routing_number: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        cash_tag: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if platform is not None:
            _body["platform"] = platform
        if routing_number is not None:
            _body["routing_number"] = routing_number
        if account_number is not None:
            _body["account_number"] = account_number
        if account_type is not None:
            _body["account_type"] = account_type
        if email is not None:
            _body["email"] = email
        if phone_number is not None:
            _body["phone_number"] = phone_number
        if handle is not None:
            _body["handle"] = handle
        if cash_tag is not None:
            _body["cash_tag"] = cash_tag
        args.body = _body
        if user_id is not None:
            _path_params["user_id"] = user_id
        args.path = _path_params
        return args

    async def _aadd_payout_method_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Add a Payout Method
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/users/{user_id}/payout-methods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_users_add_payout_method_request.serialize(body, content_type)
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


    def _add_payout_method_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Add a Payout Method
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_user_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/users/{user_id}/payout-methods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_users_add_payout_method_request.serialize(body, content_type)
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


class AddPayoutMethodRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aadd_payout_method(
        self,
        platform: str,
        user_id: str,
        routing_number: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        cash_tag: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_payout_method_mapped_args(
            platform=platform,
            user_id=user_id,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            email=email,
            phone_number=phone_number,
            handle=handle,
            cash_tag=cash_tag,
        )
        return await self._aadd_payout_method_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def add_payout_method(
        self,
        platform: str,
        user_id: str,
        routing_number: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        cash_tag: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_payout_method_mapped_args(
            platform=platform,
            user_id=user_id,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            email=email,
            phone_number=phone_number,
            handle=handle,
            cash_tag=cash_tag,
        )
        return self._add_payout_method_oapg(
            body=args.body,
            path_params=args.path,
        )

class AddPayoutMethod(BaseApi):

    async def aadd_payout_method(
        self,
        platform: str,
        user_id: str,
        routing_number: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        cash_tag: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaymentMethodPydantic:
        raw_response = await self.raw.aadd_payout_method(
            platform=platform,
            user_id=user_id,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            email=email,
            phone_number=phone_number,
            handle=handle,
            cash_tag=cash_tag,
            **kwargs,
        )
        if validate:
            return PaymentMethodPydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentMethodPydantic, raw_response.body)
    
    
    def add_payout_method(
        self,
        platform: str,
        user_id: str,
        routing_number: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        cash_tag: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PaymentMethodPydantic:
        raw_response = self.raw.add_payout_method(
            platform=platform,
            user_id=user_id,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            email=email,
            phone_number=phone_number,
            handle=handle,
            cash_tag=cash_tag,
        )
        if validate:
            return PaymentMethodPydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentMethodPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        platform: str,
        user_id: str,
        routing_number: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        cash_tag: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._add_payout_method_mapped_args(
            platform=platform,
            user_id=user_id,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            email=email,
            phone_number=phone_number,
            handle=handle,
            cash_tag=cash_tag,
        )
        return await self._aadd_payout_method_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def put(
        self,
        platform: str,
        user_id: str,
        routing_number: typing.Optional[str] = None,
        account_number: typing.Optional[str] = None,
        account_type: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        phone_number: typing.Optional[str] = None,
        handle: typing.Optional[str] = None,
        cash_tag: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._add_payout_method_mapped_args(
            platform=platform,
            user_id=user_id,
            routing_number=routing_number,
            account_number=account_number,
            account_type=account_type,
            email=email,
            phone_number=phone_number,
            handle=handle,
            cash_tag=cash_tag,
        )
        return self._add_payout_method_oapg(
            body=args.body,
            path_params=args.path,
        )

