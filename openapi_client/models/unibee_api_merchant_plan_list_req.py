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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantPlanListReq(BaseModel):
    """
    UnibeeApiMerchantPlanListReq
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="Count Of Per Page")
    currency: Optional[StrictStr] = Field(default=None, description="Filter Currency")
    page: Optional[StrictInt] = Field(default=None, description="Page, Start 0")
    publish_status: Optional[StrictInt] = Field(default=None, description="Filter, Default All，PublishStatus，1-UnPublished，2-Published", alias="publishStatus")
    sort_field: Optional[StrictStr] = Field(default=None, description="Sort Field，gmt_create|gmt_modify，Default gmt_modify", alias="sortField")
    sort_type: Optional[StrictStr] = Field(default=None, description="Sort Type，asc|desc，Default desc", alias="sortType")
    status: Optional[List[StrictInt]] = Field(default=None, description="Filter, Default All，,Status，1-Editing，2-Active，3-InActive，4-Expired")
    type: Optional[List[StrictInt]] = Field(default=None, description="1-main plan，2-addon plan")
    __properties: ClassVar[List[str]] = ["count", "currency", "page", "publishStatus", "sortField", "sortType", "status", "type"]

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
        """Create an instance of UnibeeApiMerchantPlanListReq from a JSON string"""
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
        """Create an instance of UnibeeApiMerchantPlanListReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "currency": obj.get("currency"),
            "page": obj.get("page"),
            "publishStatus": obj.get("publishStatus"),
            "sortField": obj.get("sortField"),
            "sortType": obj.get("sortType"),
            "status": obj.get("status"),
            "type": obj.get("type")
        })
        return _obj


