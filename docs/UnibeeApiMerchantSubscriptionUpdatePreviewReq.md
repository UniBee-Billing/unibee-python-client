# UnibeeApiMerchantSubscriptionUpdatePreviewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeApiBeanPlanAddonParam]**](UnibeeApiBeanPlanAddonParam.md) | addonParams | [optional] 
**effect_immediate** | **int** | Effect Immediate，1-Immediate，2-Next Period | [optional] 
**gateway_id** | **int** | Id | [optional] 
**new_plan_id** | **int** | New PlanId | 
**quantity** | **int** | Quantity，Default 1 | [optional] 
**subscription_id** | **str** | SubscriptionId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_update_preview_req import UnibeeApiMerchantSubscriptionUpdatePreviewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionUpdatePreviewReq from a JSON string
unibee_api_merchant_subscription_update_preview_req_instance = UnibeeApiMerchantSubscriptionUpdatePreviewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionUpdatePreviewReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_update_preview_req_dict = unibee_api_merchant_subscription_update_preview_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionUpdatePreviewReq from a dict
unibee_api_merchant_subscription_update_preview_req_form_dict = unibee_api_merchant_subscription_update_preview_req.from_dict(unibee_api_merchant_subscription_update_preview_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


