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

class UnibeeApiBeanMerchantMetricEventSimplify(BaseModel):
    """
    UnibeeApiBeanMerchantMetricEventSimplify
    """ # noqa: E501
    aggregation_property_data: Optional[StrictStr] = Field(default=None, description="aggregation property data (Json)", alias="aggregationPropertyData")
    aggregation_property_int: Optional[StrictInt] = Field(default=None, description="aggregation property int, use for metric of max|sum type", alias="aggregationPropertyInt")
    aggregation_property_string: Optional[StrictStr] = Field(default=None, description="aggregation property string, use for metric of count|count_unique type", alias="aggregationPropertyString")
    create_time: Optional[StrictInt] = Field(default=None, description="create utc time", alias="createTime")
    external_event_id: Optional[StrictStr] = Field(default=None, description="external_event_id, should be unique", alias="externalEventId")
    id: Optional[StrictInt] = Field(default=None, description="Id")
    merchant_id: Optional[StrictInt] = Field(default=None, description="merchantId", alias="merchantId")
    metric_id: Optional[StrictInt] = Field(default=None, description="metric_id", alias="metricId")
    metric_limit: Optional[StrictInt] = Field(default=None, alias="metricLimit")
    subscription_ids: Optional[StrictStr] = Field(default=None, alias="subscriptionIds")
    subscription_period_end: Optional[StrictInt] = Field(default=None, description="matched subscription's current_period_end", alias="subscriptionPeriodEnd")
    subscription_period_start: Optional[StrictInt] = Field(default=None, description="matched subscription's current_period_start", alias="subscriptionPeriodStart")
    used: Optional[StrictInt] = None
    user_id: Optional[StrictInt] = Field(default=None, description="user_id", alias="userId")
    __properties: ClassVar[List[str]] = ["aggregationPropertyData", "aggregationPropertyInt", "aggregationPropertyString", "createTime", "externalEventId", "id", "merchantId", "metricId", "metricLimit", "subscriptionIds", "subscriptionPeriodEnd", "subscriptionPeriodStart", "used", "userId"]

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
        """Create an instance of UnibeeApiBeanMerchantMetricEventSimplify from a JSON string"""
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
        """Create an instance of UnibeeApiBeanMerchantMetricEventSimplify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationPropertyData": obj.get("aggregationPropertyData"),
            "aggregationPropertyInt": obj.get("aggregationPropertyInt"),
            "aggregationPropertyString": obj.get("aggregationPropertyString"),
            "createTime": obj.get("createTime"),
            "externalEventId": obj.get("externalEventId"),
            "id": obj.get("id"),
            "merchantId": obj.get("merchantId"),
            "metricId": obj.get("metricId"),
            "metricLimit": obj.get("metricLimit"),
            "subscriptionIds": obj.get("subscriptionIds"),
            "subscriptionPeriodEnd": obj.get("subscriptionPeriodEnd"),
            "subscriptionPeriodStart": obj.get("subscriptionPeriodStart"),
            "used": obj.get("used"),
            "userId": obj.get("userId")
        })
        return _obj


