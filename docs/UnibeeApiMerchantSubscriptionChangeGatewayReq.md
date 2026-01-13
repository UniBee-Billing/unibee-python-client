# UnibeeApiMerchantSubscriptionChangeGatewayReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gateway_id** | **int** | GatewayId | 
**subscription_id** | **str** | SubscriptionId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_change_gateway_req import UnibeeApiMerchantSubscriptionChangeGatewayReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionChangeGatewayReq from a JSON string
unibee_api_merchant_subscription_change_gateway_req_instance = UnibeeApiMerchantSubscriptionChangeGatewayReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionChangeGatewayReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_change_gateway_req_dict = unibee_api_merchant_subscription_change_gateway_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionChangeGatewayReq from a dict
unibee_api_merchant_subscription_change_gateway_req_form_dict = unibee_api_merchant_subscription_change_gateway_req.from_dict(unibee_api_merchant_subscription_change_gateway_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


