# UnibeeApiMerchantSubscriptionCreatePreviewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeApiBeanPlanAddonParam]**](UnibeeApiBeanPlanAddonParam.md) | addonParams | [optional] 
**gateway_id** | **int** | Id | 
**plan_id** | **int** | PlanId | 
**quantity** | **int** | Quantity | [optional] 
**user_id** | **int** | UserId | 
**vat_country_code** | **str** | VatCountryCode, CountryName | [optional] 
**vat_number** | **str** | VatNumber | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_create_preview_req import UnibeeApiMerchantSubscriptionCreatePreviewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionCreatePreviewReq from a JSON string
unibee_api_merchant_subscription_create_preview_req_instance = UnibeeApiMerchantSubscriptionCreatePreviewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionCreatePreviewReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_create_preview_req_dict = unibee_api_merchant_subscription_create_preview_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionCreatePreviewReq from a dict
unibee_api_merchant_subscription_create_preview_req_form_dict = unibee_api_merchant_subscription_create_preview_req.from_dict(unibee_api_merchant_subscription_create_preview_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


