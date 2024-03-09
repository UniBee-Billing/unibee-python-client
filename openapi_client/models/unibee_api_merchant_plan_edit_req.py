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
from openapi_client.models.unibee_internal_logic_gateway_ro_bulk_metric_limit_plan_binding_param import UnibeeInternalLogicGatewayRoBulkMetricLimitPlanBindingParam
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantPlanEditReq(BaseModel):
    """
    UnibeeApiMerchantPlanEditReq
    """ # noqa: E501
    addon_ids: Optional[List[StrictInt]] = Field(default=None, description="Plan Ids Of Addon Type", alias="addonIds")
    amount: StrictInt = Field(description="Plan CaptureAmount")
    currency: StrictStr = Field(description="Plan Currency")
    description: Optional[StrictStr] = Field(default=None, description="Description")
    home_url: Optional[StrictStr] = Field(default=None, description="HomeUrl,Start With: http", alias="homeUrl")
    image_url: Optional[StrictStr] = Field(default=None, description="ImageUrl,Start With: http", alias="imageUrl")
    interval_count: Optional[StrictInt] = Field(default=1, description="Default 1，Number Of IntervalUnit", alias="intervalCount")
    interval_unit: StrictStr = Field(description="Plan Interval Unit，em: day|month|year|week", alias="intervalUnit")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Metadata，Map")
    metric_limits: Optional[List[UnibeeInternalLogicGatewayRoBulkMetricLimitPlanBindingParam]] = Field(default=None, description="Plan's MetricLimit List", alias="metricLimits")
    plan_id: StrictInt = Field(description="PlanId", alias="planId")
    plan_name: StrictStr = Field(description="Plan Name", alias="planName")
    product_description: Optional[StrictStr] = Field(default=None, description="Default Copy Description", alias="productDescription")
    product_name: Optional[StrictStr] = Field(default=None, description="Default Copy PlanName", alias="productName")
    __properties: ClassVar[List[str]] = ["addonIds", "amount", "currency", "description", "homeUrl", "imageUrl", "intervalCount", "intervalUnit", "metadata", "metricLimits", "planId", "planName", "productDescription", "productName"]

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
        """Create an instance of UnibeeApiMerchantPlanEditReq from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in metric_limits (list)
        _items = []
        if self.metric_limits:
            for _item in self.metric_limits:
                if _item:
                    _items.append(_item.to_dict())
            _dict['metricLimits'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantPlanEditReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addonIds": obj.get("addonIds"),
            "amount": obj.get("amount"),
            "currency": obj.get("currency"),
            "description": obj.get("description"),
            "homeUrl": obj.get("homeUrl"),
            "imageUrl": obj.get("imageUrl"),
            "intervalCount": obj.get("intervalCount") if obj.get("intervalCount") is not None else 1,
            "intervalUnit": obj.get("intervalUnit"),
            "metadata": obj.get("metadata"),
            "metricLimits": [UnibeeInternalLogicGatewayRoBulkMetricLimitPlanBindingParam.from_dict(_item) for _item in obj["metricLimits"]] if obj.get("metricLimits") is not None else None,
            "planId": obj.get("planId"),
            "planName": obj.get("planName"),
            "productDescription": obj.get("productDescription"),
            "productName": obj.get("productName")
        })
        return _obj


