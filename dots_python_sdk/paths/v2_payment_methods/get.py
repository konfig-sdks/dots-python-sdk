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

from dots_python_sdk.model.paymentmethods_list_all_payment_customer_response import PaymentmethodsListAllPaymentCustomerResponse as PaymentmethodsListAllPaymentCustomerResponseSchema

from dots_python_sdk.type.paymentmethods_list_all_payment_customer_response import PaymentmethodsListAllPaymentCustomerResponse

from ...api_client import Dictionary
from dots_python_sdk.pydantic.paymentmethods_list_all_payment_customer_response import PaymentmethodsListAllPaymentCustomerResponse as PaymentmethodsListAllPaymentCustomerResponsePydantic

from . import path

# Query params
CustomerIdSchema = schemas.StrSchema
LimitSchema = schemas.NumberSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'customer_id': typing.Union[CustomerIdSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, float, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_customer_id = api_client.QueryParameter(
    name="customer_id",
    style=api_client.ParameterStyle.FORM,
    schema=CustomerIdSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
_auth = [
    'api_key',
]
SchemaFor200ResponseBodyApplicationJson = PaymentmethodsListAllPaymentCustomerResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaymentmethodsListAllPaymentCustomerResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaymentmethodsListAllPaymentCustomerResponse


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

    def _list_all_payment_customer_mapped_args(
        self,
        customer_id: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if customer_id is not None:
            _query_params["customer_id"] = customer_id
        if limit is not None:
            _query_params["limit"] = limit
        args.query = _query_params
        return args

    async def _alist_all_payment_customer_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List all Payment Methods for a Payment Customer
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_customer_id,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/payment-methods',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _list_all_payment_customer_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List all Payment Methods for a Payment Customer
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_customer_id,
            request_query_limit,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/payment-methods',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class ListAllPaymentCustomerRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_all_payment_customer(
        self,
        customer_id: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_payment_customer_mapped_args(
            customer_id=customer_id,
            limit=limit,
        )
        return await self._alist_all_payment_customer_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def list_all_payment_customer(
        self,
        customer_id: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_payment_customer_mapped_args(
            customer_id=customer_id,
            limit=limit,
        )
        return self._list_all_payment_customer_oapg(
            query_params=args.query,
        )

class ListAllPaymentCustomer(BaseApi):

    async def alist_all_payment_customer(
        self,
        customer_id: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaymentmethodsListAllPaymentCustomerResponsePydantic:
        raw_response = await self.raw.alist_all_payment_customer(
            customer_id=customer_id,
            limit=limit,
            **kwargs,
        )
        if validate:
            return PaymentmethodsListAllPaymentCustomerResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentmethodsListAllPaymentCustomerResponsePydantic, raw_response.body)
    
    
    def list_all_payment_customer(
        self,
        customer_id: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        validate: bool = False,
    ) -> PaymentmethodsListAllPaymentCustomerResponsePydantic:
        raw_response = self.raw.list_all_payment_customer(
            customer_id=customer_id,
            limit=limit,
        )
        if validate:
            return PaymentmethodsListAllPaymentCustomerResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaymentmethodsListAllPaymentCustomerResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        customer_id: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_all_payment_customer_mapped_args(
            customer_id=customer_id,
            limit=limit,
        )
        return await self._alist_all_payment_customer_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        customer_id: typing.Optional[str] = None,
        limit: typing.Optional[typing.Union[int, float]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_all_payment_customer_mapped_args(
            customer_id=customer_id,
            limit=limit,
        )
        return self._list_all_payment_customer_oapg(
            query_params=args.query,
        )

