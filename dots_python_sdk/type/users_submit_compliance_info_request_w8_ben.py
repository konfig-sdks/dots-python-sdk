# coding: utf-8

"""
    dots api

    Scalable and Flexible Payouts Infrastructure

    The version of the OpenAPI document: 1.0
    Contact: info@dots.dev
    Created by: https://dots.dev
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from dots_python_sdk.type.users_submit_compliance_info_request_w8_ben_address import UsersSubmitComplianceInfoRequestW8BenAddress
from dots_python_sdk.type.users_submit_compliance_info_request_w8_ben_signature import UsersSubmitComplianceInfoRequestW8BenSignature

class RequiredUsersSubmitComplianceInfoRequestW8Ben(TypedDict):
    # Full name of the person.
    name: str

    # The two-letter ISO country code associated with the beneficial owner's citizenship.
    citizenship_country: str

    # Date of birth of the user.
    date_of_birth: date

    # SSN
    tin: str

    address: UsersSubmitComplianceInfoRequestW8BenAddress

    signature: UsersSubmitComplianceInfoRequestW8BenSignature

class OptionalUsersSubmitComplianceInfoRequestW8Ben(TypedDict, total=False):
    # The tax identification number associated with the beneficial owner's country of residence.
    foreign_tax_id: str

    # The two-letter ISO country code of the country for tax treaty purposes.
    tax_treaty_country: str

    # The article and paragraph of the citation claimed for tax treaty purposes.
    tax_treaty_citation: str

    # The withholding rate claimed for tax treaty purposes. For example, a 15% rate would be represented as 0.15.
    tax_treaty_rate: typing.Union[int, float]

    # The type of income for tax treaty purposes. Valid values are - interest1 (Interest Paid by U.S. Obligors) - dividend6 (Dividends Paid by U.S. Corporations) - dividend7 (Dividends Qualifying for Direct Dividend Rate) - pension15 (Pensions and Annuities) - socialSecurity (Social Security) - equipment10 (Industrial Equipment) - knowhow10 (Know-How/Other Industrial Royalties) - patent10 (Patents) - film11 (Film & TV) - copyright12 (Copyrights)
    tax_treaty_income_type: str

    # An optional explanation for the tax treaty claimed.
    tax_treaty_explanation: str

class UsersSubmitComplianceInfoRequestW8Ben(RequiredUsersSubmitComplianceInfoRequestW8Ben, OptionalUsersSubmitComplianceInfoRequestW8Ben):
    pass
