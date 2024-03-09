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

class UnibeeInternalModelEntityOverseaPayPayment(BaseModel):
    """
    UnibeeInternalModelEntityOverseaPayPayment
    """ # noqa: E501
    app_id: Optional[StrictStr] = Field(default=None, description="app id", alias="appId")
    authorize_reason: Optional[StrictStr] = Field(default=None, alias="authorizeReason")
    authorize_status: Optional[StrictInt] = Field(default=None, description="authorize status，0-waiting authorize，1-authorized，2-authorized_request", alias="authorizeStatus")
    automatic: Optional[StrictInt] = Field(default=None, description="0-no,1-yes")
    balance_amount: Optional[StrictInt] = Field(default=None, description="balance_amount", alias="balanceAmount")
    balance_end: Optional[StrictInt] = Field(default=None, description="balance_end, utc time", alias="balanceEnd")
    balance_start: Optional[StrictInt] = Field(default=None, description="balance_start, utc time", alias="balanceStart")
    billing_reason: Optional[StrictStr] = Field(default=None, alias="billingReason")
    biz_type: Optional[StrictInt] = Field(default=None, description="biz_type 1-single payment, 3-subscription", alias="bizType")
    cancel_time: Optional[StrictInt] = Field(default=None, description="cancel time, utc time", alias="cancelTime")
    capture_delay_hours: Optional[StrictInt] = Field(default=None, description="capture_delay_hours", alias="captureDelayHours")
    code: Optional[StrictStr] = None
    company_id: Optional[StrictInt] = Field(default=None, description="company id", alias="companyId")
    country_code: Optional[StrictStr] = Field(default=None, description="country code", alias="countryCode")
    create_time: Optional[StrictInt] = Field(default=None, description="create time, utc time", alias="createTime")
    currency: Optional[StrictStr] = Field(default=None, description="currency，“SGD” “MYR” “PHP” “IDR” “THB”")
    external_payment_id: Optional[StrictStr] = Field(default=None, description="external_payment_id", alias="externalPaymentId")
    failure_reason: Optional[StrictStr] = Field(default=None, alias="failureReason")
    gateway_edition: Optional[StrictStr] = Field(default=None, description="gateway edition", alias="gatewayEdition")
    gateway_id: Optional[StrictInt] = Field(default=None, description="gateway_id", alias="gatewayId")
    gateway_payment_id: Optional[StrictStr] = Field(default=None, description="gateway_payment_id", alias="gatewayPaymentId")
    gateway_payment_intent_id: Optional[StrictStr] = Field(default=None, description="gateway_payment_intent_id", alias="gatewayPaymentIntentId")
    gateway_payment_method: Optional[StrictStr] = Field(default=None, alias="gatewayPaymentMethod")
    gmt_create: Optional[StrictStr] = Field(default=None, description="create time", alias="gmtCreate")
    gmt_modify: Optional[StrictStr] = Field(default=None, description="update time", alias="gmtModify")
    hide_payment_methods: Optional[StrictStr] = Field(default=None, description="hide_payment_methods", alias="hidePaymentMethods")
    id: Optional[StrictInt] = Field(default=None, description="id")
    invoice_data: Optional[StrictStr] = Field(default=None, alias="invoiceData")
    invoice_id: Optional[StrictStr] = Field(default=None, description="invoice id", alias="invoiceId")
    link: Optional[StrictStr] = None
    merchant_id: Optional[StrictInt] = Field(default=None, description="merchant id", alias="merchantId")
    meta_data: Optional[StrictStr] = Field(default=None, description="meta_data (json)", alias="metaData")
    open_api_id: Optional[StrictInt] = Field(default=None, description="open api id", alias="openApiId")
    paid_time: Optional[StrictInt] = Field(default=None, description="paid time, utc time", alias="paidTime")
    payment_amount: Optional[StrictInt] = Field(default=None, description="payment_amount", alias="paymentAmount")
    payment_data: Optional[StrictStr] = Field(default=None, description="payment create data (json)", alias="paymentData")
    payment_id: Optional[StrictStr] = Field(default=None, description="payment id", alias="paymentId")
    refund_amount: Optional[StrictInt] = Field(default=None, description="total refund amount", alias="refundAmount")
    return_url: Optional[StrictStr] = Field(default=None, description="return url", alias="returnUrl")
    status: Optional[StrictInt] = Field(default=None, description="status  10-pending，20-success，30-failure, 40-cancel")
    subscription_id: Optional[StrictStr] = Field(default=None, description="subscription id", alias="subscriptionId")
    terminal_ip: Optional[StrictStr] = Field(default=None, description="client ip", alias="terminalIp")
    token: Optional[StrictStr] = None
    total_amount: Optional[StrictInt] = Field(default=None, description="total amount", alias="totalAmount")
    unique_id: Optional[StrictStr] = Field(default=None, description="unique id", alias="uniqueId")
    user_id: Optional[StrictInt] = Field(default=None, description="user_id", alias="userId")
    verify: Optional[StrictStr] = Field(default=None, description="codeVerify")
    __properties: ClassVar[List[str]] = ["appId", "authorizeReason", "authorizeStatus", "automatic", "balanceAmount", "balanceEnd", "balanceStart", "billingReason", "bizType", "cancelTime", "captureDelayHours", "code", "companyId", "countryCode", "createTime", "currency", "externalPaymentId", "failureReason", "gatewayEdition", "gatewayId", "gatewayPaymentId", "gatewayPaymentIntentId", "gatewayPaymentMethod", "gmtCreate", "gmtModify", "hidePaymentMethods", "id", "invoiceData", "invoiceId", "link", "merchantId", "metaData", "openApiId", "paidTime", "paymentAmount", "paymentData", "paymentId", "refundAmount", "returnUrl", "status", "subscriptionId", "terminalIp", "token", "totalAmount", "uniqueId", "userId", "verify"]

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
        """Create an instance of UnibeeInternalModelEntityOverseaPayPayment from a JSON string"""
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
        """Create an instance of UnibeeInternalModelEntityOverseaPayPayment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "appId": obj.get("appId"),
            "authorizeReason": obj.get("authorizeReason"),
            "authorizeStatus": obj.get("authorizeStatus"),
            "automatic": obj.get("automatic"),
            "balanceAmount": obj.get("balanceAmount"),
            "balanceEnd": obj.get("balanceEnd"),
            "balanceStart": obj.get("balanceStart"),
            "billingReason": obj.get("billingReason"),
            "bizType": obj.get("bizType"),
            "cancelTime": obj.get("cancelTime"),
            "captureDelayHours": obj.get("captureDelayHours"),
            "code": obj.get("code"),
            "companyId": obj.get("companyId"),
            "countryCode": obj.get("countryCode"),
            "createTime": obj.get("createTime"),
            "currency": obj.get("currency"),
            "externalPaymentId": obj.get("externalPaymentId"),
            "failureReason": obj.get("failureReason"),
            "gatewayEdition": obj.get("gatewayEdition"),
            "gatewayId": obj.get("gatewayId"),
            "gatewayPaymentId": obj.get("gatewayPaymentId"),
            "gatewayPaymentIntentId": obj.get("gatewayPaymentIntentId"),
            "gatewayPaymentMethod": obj.get("gatewayPaymentMethod"),
            "gmtCreate": obj.get("gmtCreate"),
            "gmtModify": obj.get("gmtModify"),
            "hidePaymentMethods": obj.get("hidePaymentMethods"),
            "id": obj.get("id"),
            "invoiceData": obj.get("invoiceData"),
            "invoiceId": obj.get("invoiceId"),
            "link": obj.get("link"),
            "merchantId": obj.get("merchantId"),
            "metaData": obj.get("metaData"),
            "openApiId": obj.get("openApiId"),
            "paidTime": obj.get("paidTime"),
            "paymentAmount": obj.get("paymentAmount"),
            "paymentData": obj.get("paymentData"),
            "paymentId": obj.get("paymentId"),
            "refundAmount": obj.get("refundAmount"),
            "returnUrl": obj.get("returnUrl"),
            "status": obj.get("status"),
            "subscriptionId": obj.get("subscriptionId"),
            "terminalIp": obj.get("terminalIp"),
            "token": obj.get("token"),
            "totalAmount": obj.get("totalAmount"),
            "uniqueId": obj.get("uniqueId"),
            "userId": obj.get("userId"),
            "verify": obj.get("verify")
        })
        return _obj


