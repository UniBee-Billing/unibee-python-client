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

class UnibeeApiMerchantMetricNewReq(BaseModel):
    """
    UnibeeApiMerchantMetricNewReq
    """ # noqa: E501
    aggregation_property: Optional[StrictStr] = Field(default=None, description="AggregationProperty, Will Needed When AggregationType != count", alias="aggregationProperty")
    aggregation_type: Optional[StrictInt] = Field(default=None, description="AggregationType,1-count，2-count unique, 3-latest, 4-max, 5-sum", alias="aggregationType")
    code: StrictStr = Field(description="Code")
    metric_description: Optional[StrictStr] = Field(default=None, description="MetricDescription", alias="metricDescription")
    metric_name: StrictStr = Field(description="MetricName", alias="metricName")
    __properties: ClassVar[List[str]] = ["aggregationProperty", "aggregationType", "code", "metricDescription", "metricName"]

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
        """Create an instance of UnibeeApiMerchantMetricNewReq from a JSON string"""
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
        """Create an instance of UnibeeApiMerchantMetricNewReq from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationProperty": obj.get("aggregationProperty"),
            "aggregationType": obj.get("aggregationType"),
            "code": obj.get("code"),
            "metricDescription": obj.get("metricDescription"),
            "metricName": obj.get("metricName")
        })
        return _obj


