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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_internal_logic_gateway_ro_gateway_simplify import UnibeeInternalLogicGatewayRoGatewaySimplify
from openapi_client.models.unibee_internal_logic_gateway_ro_plan_addon_vo import UnibeeInternalLogicGatewayRoPlanAddonVo
from openapi_client.models.unibee_internal_logic_gateway_ro_plan_simplify import UnibeeInternalLogicGatewayRoPlanSimplify
from openapi_client.models.unibee_internal_logic_gateway_ro_subscription_pending_update_detail_vo import UnibeeInternalLogicGatewayRoSubscriptionPendingUpdateDetailVo
from openapi_client.models.unibee_internal_logic_gateway_ro_subscription_plan_addon_param_ro import UnibeeInternalLogicGatewayRoSubscriptionPlanAddonParamRo
from openapi_client.models.unibee_internal_logic_gateway_ro_subscription_simplify import UnibeeInternalLogicGatewayRoSubscriptionSimplify
from openapi_client.models.unibee_internal_logic_gateway_ro_user_account_simplify import UnibeeInternalLogicGatewayRoUserAccountSimplify
from typing import Optional, Set
from typing_extensions import Self

class UnibeeInternalLogicGatewayRoSubscriptionDetailVo(BaseModel):
    """
    UnibeeInternalLogicGatewayRoSubscriptionDetailVo
    """ # noqa: E501
    addon_params: Optional[List[UnibeeInternalLogicGatewayRoSubscriptionPlanAddonParamRo]] = Field(default=None, description="AddonParams", alias="addonParams")
    addons: Optional[List[UnibeeInternalLogicGatewayRoPlanAddonVo]] = Field(default=None, description="Addon")
    gateway: Optional[UnibeeInternalLogicGatewayRoGatewaySimplify] = None
    plan: Optional[UnibeeInternalLogicGatewayRoPlanSimplify] = None
    subscription: Optional[UnibeeInternalLogicGatewayRoSubscriptionSimplify] = None
    unfinished_subscription_pending_update: Optional[UnibeeInternalLogicGatewayRoSubscriptionPendingUpdateDetailVo] = Field(default=None, alias="unfinishedSubscriptionPendingUpdate")
    user: Optional[UnibeeInternalLogicGatewayRoUserAccountSimplify] = None
    __properties: ClassVar[List[str]] = ["addonParams", "addons", "gateway", "plan", "subscription", "unfinishedSubscriptionPendingUpdate", "user"]

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
        """Create an instance of UnibeeInternalLogicGatewayRoSubscriptionDetailVo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in addon_params (list)
        _items = []
        if self.addon_params:
            for _item in self.addon_params:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addonParams'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in addons (list)
        _items = []
        if self.addons:
            for _item in self.addons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['addons'] = _items
        # override the default output from pydantic by calling `to_dict()` of gateway
        if self.gateway:
            _dict['gateway'] = self.gateway.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plan
        if self.plan:
            _dict['plan'] = self.plan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        # override the default output from pydantic by calling `to_dict()` of unfinished_subscription_pending_update
        if self.unfinished_subscription_pending_update:
            _dict['unfinishedSubscriptionPendingUpdate'] = self.unfinished_subscription_pending_update.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeInternalLogicGatewayRoSubscriptionDetailVo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addonParams": [UnibeeInternalLogicGatewayRoSubscriptionPlanAddonParamRo.from_dict(_item) for _item in obj["addonParams"]] if obj.get("addonParams") is not None else None,
            "addons": [UnibeeInternalLogicGatewayRoPlanAddonVo.from_dict(_item) for _item in obj["addons"]] if obj.get("addons") is not None else None,
            "gateway": UnibeeInternalLogicGatewayRoGatewaySimplify.from_dict(obj["gateway"]) if obj.get("gateway") is not None else None,
            "plan": UnibeeInternalLogicGatewayRoPlanSimplify.from_dict(obj["plan"]) if obj.get("plan") is not None else None,
            "subscription": UnibeeInternalLogicGatewayRoSubscriptionSimplify.from_dict(obj["subscription"]) if obj.get("subscription") is not None else None,
            "unfinishedSubscriptionPendingUpdate": UnibeeInternalLogicGatewayRoSubscriptionPendingUpdateDetailVo.from_dict(obj["unfinishedSubscriptionPendingUpdate"]) if obj.get("unfinishedSubscriptionPendingUpdate") is not None else None,
            "user": UnibeeInternalLogicGatewayRoUserAccountSimplify.from_dict(obj["user"]) if obj.get("user") is not None else None
        })
        return _obj


