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
from openapi_client.models.unibee_api_bean_invoice_simplify import UnibeeApiBeanInvoiceSimplify
from openapi_client.models.unibee_api_bean_user_account_simplify import UnibeeApiBeanUserAccountSimplify
from openapi_client.models.unibee_api_merchant_search_precision_match_object import UnibeeApiMerchantSearchPrecisionMatchObject
from typing import Optional, Set
from typing_extensions import Self

class UnibeeApiMerchantSearchSearchRes(BaseModel):
    """
    UnibeeApiMerchantSearchSearchRes
    """ # noqa: E501
    match_invoice: Optional[List[UnibeeApiBeanInvoiceSimplify]] = Field(default=None, description="MatchInvoice", alias="matchInvoice")
    match_user_accounts: Optional[List[UnibeeApiBeanUserAccountSimplify]] = Field(default=None, description="MatchUserAccounts", alias="matchUserAccounts")
    precision_match_object: Optional[UnibeeApiMerchantSearchPrecisionMatchObject] = Field(default=None, alias="precisionMatchObject")
    __properties: ClassVar[List[str]] = ["matchInvoice", "matchUserAccounts", "precisionMatchObject"]

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
        """Create an instance of UnibeeApiMerchantSearchSearchRes from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in match_invoice (list)
        _items = []
        if self.match_invoice:
            for _item in self.match_invoice:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchInvoice'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in match_user_accounts (list)
        _items = []
        if self.match_user_accounts:
            for _item in self.match_user_accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchUserAccounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of precision_match_object
        if self.precision_match_object:
            _dict['precisionMatchObject'] = self.precision_match_object.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnibeeApiMerchantSearchSearchRes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "matchInvoice": [UnibeeApiBeanInvoiceSimplify.from_dict(_item) for _item in obj["matchInvoice"]] if obj.get("matchInvoice") is not None else None,
            "matchUserAccounts": [UnibeeApiBeanUserAccountSimplify.from_dict(_item) for _item in obj["matchUserAccounts"]] if obj.get("matchUserAccounts") is not None else None,
            "precisionMatchObject": UnibeeApiMerchantSearchPrecisionMatchObject.from_dict(obj["precisionMatchObject"]) if obj.get("precisionMatchObject") is not None else None
        })
        return _obj


