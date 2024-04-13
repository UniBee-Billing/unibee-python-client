# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_api_bean_detail_merchant_member_detail import UnibeeApiBeanDetailMerchantMemberDetail
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantAuthLoginOtpVerifyRes(BaseModel):
    """
    UnibeeApiMerchantAuthLoginOtpVerifyRes
    """ # noqa: E501
    merchant_member: Optional[UnibeeApiBeanDetailMerchantMemberDetail] = Field(default=None, alias="merchantMember")
    token: Optional[StrictStr] = Field(default=None, description="Token")
    __properties: ClassVar[List[str]] = ["merchantMember", "token"]

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
        """Create an instance of UnibeeApiMerchantAuthLoginOtpVerifyRes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of merchant_member
        if self.merchant_member:
            _dict['merchantMember'] = self.merchant_member.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantAuthLoginOtpVerifyRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "merchantMember": UnibeeApiBeanDetailMerchantMemberDetail.from_dict(obj["merchantMember"]) if obj.get("merchantMember") is not None else None,
            "token": obj.get("token")
        })
        return _obj


