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

class UnibeeInternalLogicGatewayRoMerchantMetricVo(BaseModel):
    """
    UnibeeInternalLogicGatewayRoMerchantMetricVo
    """ # noqa: E501
    aggregation_property: Optional[StrictStr] = Field(default=None, description="aggregation property", alias="aggregationProperty")
    aggregation_type: Optional[StrictInt] = Field(default=None, description="1-count，2-count unique, 3-latest, 4-max, 5-sum", alias="aggregationType")
    code: Optional[StrictStr] = Field(default=None, description="code")
    create_time: Optional[StrictInt] = Field(default=None, description="create utc time", alias="createTime")
    gmt_modify: Optional[StrictInt] = Field(default=None, description="update time", alias="gmtModify")
    id: Optional[StrictInt] = Field(default=None, description="id")
    merchant_id: Optional[StrictInt] = Field(default=None, description="merchantId", alias="merchantId")
    metric_description: Optional[StrictStr] = Field(default=None, description="metric description", alias="metricDescription")
    metric_name: Optional[StrictStr] = Field(default=None, description="metric name", alias="metricName")
    type: Optional[StrictInt] = Field(default=None, description="1-limit_metered，2-charge_metered(come later),3-charge_recurring(come later)")
    __properties: ClassVar[List[str]] = ["aggregationProperty", "aggregationType", "code", "createTime", "gmtModify", "id", "merchantId", "metricDescription", "metricName", "type"]

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
        """Create an instance of UnibeeInternalLogicGatewayRoMerchantMetricVo from a JSON string"""
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
        """Create an instance of UnibeeInternalLogicGatewayRoMerchantMetricVo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationProperty": obj.get("aggregationProperty"),
            "aggregationType": obj.get("aggregationType"),
            "code": obj.get("code"),
            "createTime": obj.get("createTime"),
            "gmtModify": obj.get("gmtModify"),
            "id": obj.get("id"),
            "merchantId": obj.get("merchantId"),
            "metricDescription": obj.get("metricDescription"),
            "metricName": obj.get("metricName"),
            "type": obj.get("type")
        })
        return _obj


