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

class UnibeeApiBeanPaymentSimplify(BaseModel):
    """
    UnibeeApiBeanPaymentSimplify
    """ # noqa: E501
    authorize_reason: Optional[StrictStr] = Field(default=None, alias="authorizeReason")
    authorize_status: Optional[StrictInt] = Field(default=None, description="authorize status，0-waiting authorize，1-authorized，2-authorized_request", alias="authorizeStatus")
    automatic: Optional[StrictInt] = None
    balance_amount: Optional[StrictInt] = Field(default=None, description="balance_amount", alias="balanceAmount")
    billing_reason: Optional[StrictStr] = Field(default=None, alias="billingReason")
    cancel_time: Optional[StrictInt] = Field(default=None, description="cancel time, utc time", alias="cancelTime")
    country_code: Optional[StrictStr] = Field(default=None, description="country code", alias="countryCode")
    create_time: Optional[StrictInt] = Field(default=None, description="create time, utc time", alias="createTime")
    currency: Optional[StrictStr] = Field(default=None, description="currency，“SGD” “MYR” “PHP” “IDR” “THB”")
    external_payment_id: Optional[StrictStr] = Field(default=None, description="external_payment_id", alias="externalPaymentId")
    failure_reason: Optional[StrictStr] = Field(default=None, alias="failureReason")
    gas_payer: Optional[StrictStr] = Field(default=None, description="who pay the gas, merchant|user", alias="gasPayer")
    gateway_id: Optional[StrictInt] = Field(default=None, description="gateway_id", alias="gatewayId")
    gateway_payment_id: Optional[StrictStr] = Field(default=None, description="gateway_payment_id", alias="gatewayPaymentId")
    invoice_id: Optional[StrictStr] = Field(default=None, description="invoice id", alias="invoiceId")
    link: Optional[StrictStr] = None
    merchant_id: Optional[StrictInt] = Field(default=None, description="merchant id", alias="merchantId")
    metadata: Optional[Dict[str, StrictStr]] = None
    paid_time: Optional[StrictInt] = Field(default=None, description="paid time, utc time", alias="paidTime")
    payment_amount: Optional[StrictInt] = Field(default=None, description="payment_amount", alias="paymentAmount")
    payment_id: Optional[StrictStr] = Field(default=None, description="payment id", alias="paymentId")
    refund_amount: Optional[StrictInt] = Field(default=None, description="total refund amount", alias="refundAmount")
    return_url: Optional[StrictStr] = Field(default=None, description="return url", alias="returnUrl")
    status: Optional[StrictInt] = Field(default=None, description="status  10-pending，20-success，30-failure, 40-cancel")
    subscription_id: Optional[StrictStr] = Field(default=None, description="subscription id", alias="subscriptionId")
    total_amount: Optional[StrictInt] = Field(default=None, description="total amount", alias="totalAmount")
    user_id: Optional[StrictInt] = Field(default=None, description="user_id", alias="userId")
    __properties: ClassVar[List[str]] = ["authorizeReason", "authorizeStatus", "automatic", "balanceAmount", "billingReason", "cancelTime", "countryCode", "createTime", "currency", "externalPaymentId", "failureReason", "gasPayer", "gatewayId", "gatewayPaymentId", "invoiceId", "link", "merchantId", "metadata", "paidTime", "paymentAmount", "paymentId", "refundAmount", "returnUrl", "status", "subscriptionId", "totalAmount", "userId"]

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
        """Create an instance of UnibeeApiBeanPaymentSimplify from a JSON string"""
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
        """Create an instance of UnibeeApiBeanPaymentSimplify from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorizeReason": obj.get("authorizeReason"),
            "authorizeStatus": obj.get("authorizeStatus"),
            "automatic": obj.get("automatic"),
            "balanceAmount": obj.get("balanceAmount"),
            "billingReason": obj.get("billingReason"),
            "cancelTime": obj.get("cancelTime"),
            "countryCode": obj.get("countryCode"),
            "createTime": obj.get("createTime"),
            "currency": obj.get("currency"),
            "externalPaymentId": obj.get("externalPaymentId"),
            "failureReason": obj.get("failureReason"),
            "gasPayer": obj.get("gasPayer"),
            "gatewayId": obj.get("gatewayId"),
            "gatewayPaymentId": obj.get("gatewayPaymentId"),
            "invoiceId": obj.get("invoiceId"),
            "link": obj.get("link"),
            "merchantId": obj.get("merchantId"),
            "metadata": obj.get("metadata"),
            "paidTime": obj.get("paidTime"),
            "paymentAmount": obj.get("paymentAmount"),
            "paymentId": obj.get("paymentId"),
            "refundAmount": obj.get("refundAmount"),
            "returnUrl": obj.get("returnUrl"),
            "status": obj.get("status"),
            "subscriptionId": obj.get("subscriptionId"),
            "totalAmount": obj.get("totalAmount"),
            "userId": obj.get("userId")
        })
        return _obj


