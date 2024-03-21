# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from dots_python_sdk.paths.v2_disputes_dispute_id_evidence.post import AddEvidenceFile
from dots_python_sdk.paths.v2_disputes.get import GetAll
from dots_python_sdk.paths.v2_disputes_dispute_id.get import GetById
from dots_python_sdk.paths.v2_disputes_dispute_id_submit.post import SubmitDispute
from dots_python_sdk.apis.tags.disputes_api_raw import DisputesApiRaw


class DisputesApi(
    AddEvidenceFile,
    GetAll,
    GetById,
    SubmitDispute,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DisputesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DisputesApiRaw(api_client)
