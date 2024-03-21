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

from dots_python_sdk.model.payouts_send_payout_request_payee import PayoutsSendPayoutRequestPayee as PayoutsSendPayoutRequestPayeeSchema
from dots_python_sdk.model.payouts_send_payout_request import PayoutsSendPayoutRequest as PayoutsSendPayoutRequestSchema
from dots_python_sdk.model.payouts_send_payout_request_additional_steps import PayoutsSendPayoutRequestAdditionalSteps as PayoutsSendPayoutRequestAdditionalStepsSchema
from dots_python_sdk.model.payout_link import PayoutLink as PayoutLinkSchema
from dots_python_sdk.model.payouts_send_payout_request_delivery import PayoutsSendPayoutRequestDelivery as PayoutsSendPayoutRequestDeliverySchema

from dots_python_sdk.type.payouts_send_payout_request import PayoutsSendPayoutRequest
from dots_python_sdk.type.payout_link import PayoutLink
from dots_python_sdk.type.payouts_send_payout_request_additional_steps import PayoutsSendPayoutRequestAdditionalSteps
from dots_python_sdk.type.payouts_send_payout_request_delivery import PayoutsSendPayoutRequestDelivery
from dots_python_sdk.type.payouts_send_payout_request_payee import PayoutsSendPayoutRequestPayee

from ...api_client import Dictionary
from dots_python_sdk.pydantic.payouts_send_payout_request_delivery import PayoutsSendPayoutRequestDelivery as PayoutsSendPayoutRequestDeliveryPydantic
from dots_python_sdk.pydantic.payouts_send_payout_request_payee import PayoutsSendPayoutRequestPayee as PayoutsSendPayoutRequestPayeePydantic
from dots_python_sdk.pydantic.payout_link import PayoutLink as PayoutLinkPydantic
from dots_python_sdk.pydantic.payouts_send_payout_request_additional_steps import PayoutsSendPayoutRequestAdditionalSteps as PayoutsSendPayoutRequestAdditionalStepsPydantic
from dots_python_sdk.pydantic.payouts_send_payout_request import PayoutsSendPayoutRequest as PayoutsSendPayoutRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = PayoutsSendPayoutRequestSchema


request_body_payouts_send_payout_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = PayoutLinkSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: PayoutLink


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: PayoutLink


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _send_payout_mapped_args(
        self,
        amount: int,
        user_id: typing.Optional[str] = None,
        payee: typing.Optional[PayoutsSendPayoutRequestPayee] = None,
        delivery: typing.Optional[PayoutsSendPayoutRequestDelivery] = None,
        force_collect_compliance_information: typing.Optional[bool] = None,
        additional_steps: typing.Optional[PayoutsSendPayoutRequestAdditionalSteps] = None,
        tax_exempt: typing.Optional[bool] = None,
        metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        memo: typing.Optional[str] = None,
        idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        payout_fee_party: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if amount is not None:
            _body["amount"] = amount
        if user_id is not None:
            _body["user_id"] = user_id
        if payee is not None:
            _body["payee"] = payee
        if delivery is not None:
            _body["delivery"] = delivery
        if force_collect_compliance_information is not None:
            _body["force_collect_compliance_information"] = force_collect_compliance_information
        if additional_steps is not None:
            _body["additional_steps"] = additional_steps
        if tax_exempt is not None:
            _body["tax_exempt"] = tax_exempt
        if metadata is not None:
            _body["metadata"] = metadata
        if memo is not None:
            _body["memo"] = memo
        if idempotency_key is not None:
            _body["idempotency_key"] = idempotency_key
        if payout_fee_party is not None:
            _body["payout_fee_party"] = payout_fee_party
        args.body = _body
        return args

    async def _asend_payout_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Send a Payout
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
            path_template='/v2/payouts/send-payout',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payouts_send_payout_request.serialize(body, content_type)
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


    def _send_payout_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Send a Payout
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
            path_template='/v2/payouts/send-payout',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_payouts_send_payout_request.serialize(body, content_type)
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


class SendPayoutRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asend_payout(
        self,
        amount: int,
        user_id: typing.Optional[str] = None,
        payee: typing.Optional[PayoutsSendPayoutRequestPayee] = None,
        delivery: typing.Optional[PayoutsSendPayoutRequestDelivery] = None,
        force_collect_compliance_information: typing.Optional[bool] = None,
        additional_steps: typing.Optional[PayoutsSendPayoutRequestAdditionalSteps] = None,
        tax_exempt: typing.Optional[bool] = None,
        metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        memo: typing.Optional[str] = None,
        idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        payout_fee_party: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_payout_mapped_args(
            amount=amount,
            user_id=user_id,
            payee=payee,
            delivery=delivery,
            force_collect_compliance_information=force_collect_compliance_information,
            additional_steps=additional_steps,
            tax_exempt=tax_exempt,
            metadata=metadata,
            memo=memo,
            idempotency_key=idempotency_key,
            payout_fee_party=payout_fee_party,
        )
        return await self._asend_payout_oapg(
            body=args.body,
            **kwargs,
        )
    
    def send_payout(
        self,
        amount: int,
        user_id: typing.Optional[str] = None,
        payee: typing.Optional[PayoutsSendPayoutRequestPayee] = None,
        delivery: typing.Optional[PayoutsSendPayoutRequestDelivery] = None,
        force_collect_compliance_information: typing.Optional[bool] = None,
        additional_steps: typing.Optional[PayoutsSendPayoutRequestAdditionalSteps] = None,
        tax_exempt: typing.Optional[bool] = None,
        metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        memo: typing.Optional[str] = None,
        idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        payout_fee_party: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_payout_mapped_args(
            amount=amount,
            user_id=user_id,
            payee=payee,
            delivery=delivery,
            force_collect_compliance_information=force_collect_compliance_information,
            additional_steps=additional_steps,
            tax_exempt=tax_exempt,
            metadata=metadata,
            memo=memo,
            idempotency_key=idempotency_key,
            payout_fee_party=payout_fee_party,
        )
        return self._send_payout_oapg(
            body=args.body,
        )

class SendPayout(BaseApi):

    async def asend_payout(
        self,
        amount: int,
        user_id: typing.Optional[str] = None,
        payee: typing.Optional[PayoutsSendPayoutRequestPayee] = None,
        delivery: typing.Optional[PayoutsSendPayoutRequestDelivery] = None,
        force_collect_compliance_information: typing.Optional[bool] = None,
        additional_steps: typing.Optional[PayoutsSendPayoutRequestAdditionalSteps] = None,
        tax_exempt: typing.Optional[bool] = None,
        metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        memo: typing.Optional[str] = None,
        idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        payout_fee_party: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> PayoutLinkPydantic:
        raw_response = await self.raw.asend_payout(
            amount=amount,
            user_id=user_id,
            payee=payee,
            delivery=delivery,
            force_collect_compliance_information=force_collect_compliance_information,
            additional_steps=additional_steps,
            tax_exempt=tax_exempt,
            metadata=metadata,
            memo=memo,
            idempotency_key=idempotency_key,
            payout_fee_party=payout_fee_party,
            **kwargs,
        )
        if validate:
            return PayoutLinkPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayoutLinkPydantic, raw_response.body)
    
    
    def send_payout(
        self,
        amount: int,
        user_id: typing.Optional[str] = None,
        payee: typing.Optional[PayoutsSendPayoutRequestPayee] = None,
        delivery: typing.Optional[PayoutsSendPayoutRequestDelivery] = None,
        force_collect_compliance_information: typing.Optional[bool] = None,
        additional_steps: typing.Optional[PayoutsSendPayoutRequestAdditionalSteps] = None,
        tax_exempt: typing.Optional[bool] = None,
        metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        memo: typing.Optional[str] = None,
        idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        payout_fee_party: typing.Optional[str] = None,
        validate: bool = False,
    ) -> PayoutLinkPydantic:
        raw_response = self.raw.send_payout(
            amount=amount,
            user_id=user_id,
            payee=payee,
            delivery=delivery,
            force_collect_compliance_information=force_collect_compliance_information,
            additional_steps=additional_steps,
            tax_exempt=tax_exempt,
            metadata=metadata,
            memo=memo,
            idempotency_key=idempotency_key,
            payout_fee_party=payout_fee_party,
        )
        if validate:
            return PayoutLinkPydantic(**raw_response.body)
        return api_client.construct_model_instance(PayoutLinkPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        amount: int,
        user_id: typing.Optional[str] = None,
        payee: typing.Optional[PayoutsSendPayoutRequestPayee] = None,
        delivery: typing.Optional[PayoutsSendPayoutRequestDelivery] = None,
        force_collect_compliance_information: typing.Optional[bool] = None,
        additional_steps: typing.Optional[PayoutsSendPayoutRequestAdditionalSteps] = None,
        tax_exempt: typing.Optional[bool] = None,
        metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        memo: typing.Optional[str] = None,
        idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        payout_fee_party: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._send_payout_mapped_args(
            amount=amount,
            user_id=user_id,
            payee=payee,
            delivery=delivery,
            force_collect_compliance_information=force_collect_compliance_information,
            additional_steps=additional_steps,
            tax_exempt=tax_exempt,
            metadata=metadata,
            memo=memo,
            idempotency_key=idempotency_key,
            payout_fee_party=payout_fee_party,
        )
        return await self._asend_payout_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        amount: int,
        user_id: typing.Optional[str] = None,
        payee: typing.Optional[PayoutsSendPayoutRequestPayee] = None,
        delivery: typing.Optional[PayoutsSendPayoutRequestDelivery] = None,
        force_collect_compliance_information: typing.Optional[bool] = None,
        additional_steps: typing.Optional[PayoutsSendPayoutRequestAdditionalSteps] = None,
        tax_exempt: typing.Optional[bool] = None,
        metadata: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        memo: typing.Optional[str] = None,
        idempotency_key: typing.Optional[typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = None,
        payout_fee_party: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._send_payout_mapped_args(
            amount=amount,
            user_id=user_id,
            payee=payee,
            delivery=delivery,
            force_collect_compliance_information=force_collect_compliance_information,
            additional_steps=additional_steps,
            tax_exempt=tax_exempt,
            metadata=metadata,
            memo=memo,
            idempotency_key=idempotency_key,
            payout_fee_party=payout_fee_party,
        )
        return self._send_payout_oapg(
            body=args.body,
        )

