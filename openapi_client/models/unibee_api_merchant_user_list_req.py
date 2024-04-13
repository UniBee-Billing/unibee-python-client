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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantUserListReq(BaseModel):
    """
    UnibeeApiMerchantUserListReq
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="Count OF Page")
    delete_include: Optional[StrictBool] = Field(default=None, description="Deleted Involved，Need Admin", alias="deleteInclude")
    email: Optional[StrictStr] = Field(default=None, description="Search Filter Email")
    first_name: Optional[StrictStr] = Field(default=None, description="Search FirstName", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="Search LastName", alias="lastName")
    page: Optional[StrictInt] = Field(default=None, description="Page,Start 0")
    sort_field: Optional[StrictStr] = Field(default=None, description="Sort，user_id|gmt_create|email|user_name|subscription_name|subscription_status|payment_method|recurring_amount|billing_type，Default gmt_create", alias="sortField")
    sort_type: Optional[StrictStr] = Field(default=None, description="Sort Type，asc|desc，Default desc", alias="sortType")
    status: Optional[List[StrictInt]] = Field(default=None, description="Status, 0-Active｜2-Frozen")
    user_id: Optional[StrictInt] = Field(default=None, description="Filter UserId", alias="userId")
    __properties: ClassVar[List[str]] = ["count", "deleteInclude", "email", "firstName", "lastName", "page", "sortField", "sortType", "status", "userId"]

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
        """Create an instance of UnibeeApiMerchantUserListReq from a JSON string"""
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
        """Create an instance of UnibeeApiMerchantUserListReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "deleteInclude": obj.get("deleteInclude"),
            "email": obj.get("email"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "page": obj.get("page"),
            "sortField": obj.get("sortField"),
            "sortType": obj.get("sortType"),
            "status": obj.get("status"),
            "userId": obj.get("userId")
        })
        return _obj


