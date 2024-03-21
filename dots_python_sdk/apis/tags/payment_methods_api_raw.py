# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from dots_python_sdk.paths.v2_payment_methods_payment_method_id_attach.post import AttachPaymentMethodRaw
from dots_python_sdk.paths.v2_payment_methods_payment_method_id_detach.post import DetachPaymentMethodRaw
from dots_python_sdk.paths.v2_payment_methods_payment_method_id.get import GetByIdRaw
from dots_python_sdk.paths.v2_payment_methods.get import ListAllPaymentCustomerRaw


class PaymentMethodsApiRaw(
    AttachPaymentMethodRaw,
    DetachPaymentMethodRaw,
    GetByIdRaw,
    ListAllPaymentCustomerRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
