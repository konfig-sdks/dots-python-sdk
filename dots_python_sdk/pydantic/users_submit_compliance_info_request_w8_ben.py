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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from dots_python_sdk.pydantic.users_submit_compliance_info_request_w8_ben_address import UsersSubmitComplianceInfoRequestW8BenAddress
from dots_python_sdk.pydantic.users_submit_compliance_info_request_w8_ben_signature import UsersSubmitComplianceInfoRequestW8BenSignature

class UsersSubmitComplianceInfoRequestW8Ben(BaseModel):
    # Full name of the person.
    name: str = Field(alias='name')

    # The two-letter ISO country code associated with the beneficial owner's citizenship.
    citizenship_country: str = Field(alias='citizenship_country')

    # Date of birth of the user.
    date_of_birth: date = Field(alias='date_of_birth')

    # SSN
    tin: str = Field(alias='tin')

    address: UsersSubmitComplianceInfoRequestW8BenAddress = Field(alias='address')

    signature: UsersSubmitComplianceInfoRequestW8BenSignature = Field(alias='signature')

    # The tax identification number associated with the beneficial owner's country of residence.
    foreign_tax_id: typing.Optional[str] = Field(None, alias='foreign_tax_id')

    # The two-letter ISO country code of the country for tax treaty purposes.
    tax_treaty_country: typing.Optional[str] = Field(None, alias='tax_treaty_country')

    # The article and paragraph of the citation claimed for tax treaty purposes.
    tax_treaty_citation: typing.Optional[str] = Field(None, alias='tax_treaty_citation')

    # The withholding rate claimed for tax treaty purposes. For example, a 15% rate would be represented as 0.15.
    tax_treaty_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='tax_treaty_rate')

    # The type of income for tax treaty purposes. Valid values are - interest1 (Interest Paid by U.S. Obligors) - dividend6 (Dividends Paid by U.S. Corporations) - dividend7 (Dividends Qualifying for Direct Dividend Rate) - pension15 (Pensions and Annuities) - socialSecurity (Social Security) - equipment10 (Industrial Equipment) - knowhow10 (Know-How/Other Industrial Royalties) - patent10 (Patents) - film11 (Film & TV) - copyright12 (Copyrights)
    tax_treaty_income_type: typing.Optional[Literal["interest1", "dividend6", "dividend7", "pension15", "socialSecurity", "equipment10", "knowhow10", "patent10", "film11", "copyright12"]] = Field(None, alias='tax_treaty_income_type')

    # An optional explanation for the tax treaty claimed.
    tax_treaty_explanation: typing.Optional[str] = Field(None, alias='tax_treaty_explanation')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
