# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from dots_python_sdk.paths.v2_organization_transfers.post import CreateOrganizationTransfer
from dots_python_sdk.paths.v2_transfers.post import CreateTransfer
from dots_python_sdk.paths.v2_organization_transfers.get import GetAll
from dots_python_sdk.paths.v2_transfers_transfer_id.get import GetById
from dots_python_sdk.paths.v2_organization_transfers_transfer_id.get import GetById0
from dots_python_sdk.paths.v2_transfers.get import ListAll
from dots_python_sdk.apis.tags.transfers_api_raw import TransfersApiRaw


class TransfersApi(
    CreateOrganizationTransfer,
    CreateTransfer,
    GetAll,
    GetById,
    GetById0,
    ListAll,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TransfersApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TransfersApiRaw(api_client)
