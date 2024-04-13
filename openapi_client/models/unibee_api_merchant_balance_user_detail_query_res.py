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

from pydantic import BaseModel, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.unibee_internal_logic_gateway_gateway_bean_gateway_balance import UnibeeInternalLogicGatewayGatewayBeanGatewayBalance
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantBalanceUserDetailQueryRes(BaseModel):
    """
    UnibeeApiMerchantBalanceUserDetailQueryRes
    """ # noqa: E501
    balance: Optional[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance] = None
    cash_balance: Optional[List[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance]] = Field(default=None, alias="cashBalance")
    invoice_credit_balance: Optional[List[UnibeeInternalLogicGatewayGatewayBeanGatewayBalance]] = Field(default=None, alias="invoiceCreditBalance")
    __properties: ClassVar[List[str]] = ["balance", "cashBalance", "invoiceCreditBalance"]

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
        """Create an instance of UnibeeApiMerchantBalanceUserDetailQueryRes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of balance
        if self.balance:
            _dict['balance'] = self.balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in cash_balance (list)
        _items = []
        if self.cash_balance:
            for _item in self.cash_balance:
                if _item:
                    _items.append(_item.to_dict())
            _dict['cashBalance'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in invoice_credit_balance (list)
        _items = []
        if self.invoice_credit_balance:
            for _item in self.invoice_credit_balance:
                if _item:
                    _items.append(_item.to_dict())
            _dict['invoiceCreditBalance'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantBalanceUserDetailQueryRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "balance": UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.from_dict(obj["balance"]) if obj.get("balance") is not None else None,
            "cashBalance": [UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.from_dict(_item) for _item in obj["cashBalance"]] if obj.get("cashBalance") is not None else None,
            "invoiceCreditBalance": [UnibeeInternalLogicGatewayGatewayBeanGatewayBalance.from_dict(_item) for _item in obj["invoiceCreditBalance"]] if obj.get("invoiceCreditBalance") is not None else None
        })
        return _obj


