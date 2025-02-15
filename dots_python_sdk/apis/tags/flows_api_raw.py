# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from dots_python_sdk.paths.v2_flows.post import CreateNewFlowRaw
from dots_python_sdk.paths.v2_flows_flow_id.get import GetByIdRaw
from dots_python_sdk.paths.v2_flows.get import ListAllRaw


class FlowsApiRaw(
    CreateNewFlowRaw,
    GetByIdRaw,
    ListAllRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
