# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantUserUpdateReq(BaseModel):
    """
    UnibeeApiMerchantUserUpdateReq
    """ # noqa: E501
    linked_in: Optional[StrictStr] = Field(default=None, description="LinkedIn", alias="LinkedIn")
    address: StrictStr = Field(description="Billing Address")
    company_name: Optional[StrictStr] = Field(default=None, description="Company Name", alias="companyName")
    country_code: StrictStr = Field(description="Country Code", alias="countryCode")
    country_name: StrictStr = Field(description="Country Name", alias="countryName")
    email: StrictStr = Field(description="Email")
    facebook: Optional[StrictStr] = Field(default=None, description="Facebook")
    first_name: StrictStr = Field(description="First name", alias="firstName")
    last_name: StrictStr = Field(description="Last Name", alias="lastName")
    other_social_info: Optional[StrictStr] = Field(default=None, description="Other Social Info", alias="otherSocialInfo")
    payment_method: Optional[StrictStr] = Field(default=None, description="Payment Method", alias="paymentMethod")
    phone: Optional[StrictStr] = Field(default=None, description="Phone")
    telegram: Optional[StrictStr] = Field(default=None, description="Telegram")
    tiktok: Optional[StrictStr] = Field(default=None, description="Tiktok")
    user_id: StrictInt = Field(description="User Id", alias="userId")
    v_at_number: Optional[StrictStr] = Field(default=None, description="VAT Number", alias="vATNumber")
    we_chat: Optional[StrictStr] = Field(default=None, description="WeChat", alias="weChat")
    whats_app: Optional[StrictStr] = Field(default=None, description="WhatsApp", alias="whatsApp")
    __properties: ClassVar[List[str]] = ["LinkedIn", "address", "companyName", "countryCode", "countryName", "email", "facebook", "firstName", "lastName", "otherSocialInfo", "paymentMethod", "phone", "telegram", "tiktok", "userId", "vATNumber", "weChat", "whatsApp"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantUserUpdateReq from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantUserUpdateReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LinkedIn": obj.get("LinkedIn"),
            "address": obj.get("address"),
            "companyName": obj.get("companyName"),
            "countryCode": obj.get("countryCode"),
            "countryName": obj.get("countryName"),
            "email": obj.get("email"),
            "facebook": obj.get("facebook"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "otherSocialInfo": obj.get("otherSocialInfo"),
            "paymentMethod": obj.get("paymentMethod"),
            "phone": obj.get("phone"),
            "telegram": obj.get("telegram"),
            "tiktok": obj.get("tiktok"),
            "userId": obj.get("userId"),
            "vATNumber": obj.get("vATNumber"),
            "weChat": obj.get("weChat"),
            "whatsApp": obj.get("whatsApp")
        })
        return _obj


