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

class UnibeeInternalLogicGatewayRoPlanSimplify(BaseModel):
    """
    UnibeeInternalLogicGatewayRoPlanSimplify
    """ # noqa: E501
    amount: Optional[StrictInt] = Field(default=None, description="amount, cent, without tax")
    binding_addon_ids: Optional[StrictStr] = Field(default=None, description="binded addon planIds，split with ,", alias="bindingAddonIds")
    create_time: Optional[StrictInt] = Field(default=None, description="create utc time", alias="createTime")
    currency: Optional[StrictStr] = Field(default=None, description="currency")
    description: Optional[StrictStr] = Field(default=None, description="description")
    extra_metric_data: Optional[StrictStr] = Field(default=None, alias="extraMetricData")
    home_url: Optional[StrictStr] = Field(default=None, description="home_url", alias="homeUrl")
    id: Optional[StrictInt] = None
    image_url: Optional[StrictStr] = Field(default=None, description="image_url", alias="imageUrl")
    interval_count: Optional[StrictInt] = Field(default=None, description="period unit count", alias="intervalCount")
    interval_unit: Optional[StrictStr] = Field(default=None, description="period unit,day|month|year|week", alias="intervalUnit")
    merchant_id: Optional[StrictInt] = Field(default=None, description="merchant id", alias="merchantId")
    metadata: Optional[Dict[str, StrictStr]] = None
    plan_name: Optional[StrictStr] = Field(default=None, description="PlanName", alias="planName")
    product_description: Optional[StrictStr] = Field(default=None, description="product description", alias="productDescription")
    product_name: Optional[StrictStr] = Field(default=None, description="product name", alias="productName")
    publish_status: Optional[StrictInt] = Field(default=None, description="1-UnPublish,2-Publish, Use For Display Plan At UserPortal", alias="publishStatus")
    status: Optional[StrictInt] = Field(default=None, description="status，1-editing，2-active，3-inactive，4-expired")
    tax_scale: Optional[StrictInt] = Field(default=None, description="tax scale 1000 = 10%", alias="taxScale")
    type: Optional[StrictInt] = Field(default=None, description="type，1-main plan，2-addon plan")
    __properties: ClassVar[List[str]] = ["amount", "bindingAddonIds", "createTime", "currency", "description", "extraMetricData", "homeUrl", "id", "imageUrl", "intervalCount", "intervalUnit", "merchantId", "metadata", "planName", "productDescription", "productName", "publishStatus", "status", "taxScale", "type"]

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
        """Create an instance of UnibeeInternalLogicGatewayRoPlanSimplify from a JSON string"""
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
        """Create an instance of UnibeeInternalLogicGatewayRoPlanSimplify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amount": obj.get("amount"),
            "bindingAddonIds": obj.get("bindingAddonIds"),
            "createTime": obj.get("createTime"),
            "currency": obj.get("currency"),
            "description": obj.get("description"),
            "extraMetricData": obj.get("extraMetricData"),
            "homeUrl": obj.get("homeUrl"),
            "id": obj.get("id"),
            "imageUrl": obj.get("imageUrl"),
            "intervalCount": obj.get("intervalCount"),
            "intervalUnit": obj.get("intervalUnit"),
            "merchantId": obj.get("merchantId"),
            "metadata": obj.get("metadata"),
            "planName": obj.get("planName"),
            "productDescription": obj.get("productDescription"),
            "productName": obj.get("productName"),
            "publishStatus": obj.get("publishStatus"),
            "status": obj.get("status"),
            "taxScale": obj.get("taxScale"),
            "type": obj.get("type")
        })
        return _obj


