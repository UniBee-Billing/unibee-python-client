# UnibeeApiMerchantPaymentNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | CountryCode | [optional] 
**currency** | **str** | Currency, either Currency&amp;Currency or PlanId needed | [optional] 
**email** | **str** | Email, either ExternalUserId&amp;Email or UserId needed | [optional] 
**external_payment_id** | **str** | ExternalPaymentId should unique for payment | [optional] 
**external_user_id** | **str** | ExternalUserId, unique, either ExternalUserId&amp;Email or UserId needed | [optional] 
**gas_payer** | **str** | who pay the gas, merchant|user | [optional] 
**gateway_id** | **int** | GatewayId | 
**items** | [**List[UnibeeApiMerchantPaymentItem]**](UnibeeApiMerchantPaymentItem.md) | Items | [optional] 
**metadata** | **Dict[str, str]** | Metadata，Map | [optional] 
**plan_id** | **int** | PlanId, either TotalAmount&amp;Currency or PlanId needed | [optional] 
**redirect_url** | **str** | Redirect Url | [optional] 
**total_amount** | **int** | Total PaymentAmount, Cent, either TotalAmount&amp;Currency or PlanId needed | [optional] 
**user_id** | **int** | UserId, either ExternalUserId&amp;Email or UserId needed | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_new_req import UnibeeApiMerchantPaymentNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentNewReq from a JSON string
unibee_api_merchant_payment_new_req_instance = UnibeeApiMerchantPaymentNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_payment_new_req_dict = unibee_api_merchant_payment_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentNewReq from a dict
unibee_api_merchant_payment_new_req_form_dict = unibee_api_merchant_payment_new_req.from_dict(unibee_api_merchant_payment_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


