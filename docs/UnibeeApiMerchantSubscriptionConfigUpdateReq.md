# UnibeeApiMerchantSubscriptionConfigUpdateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downgrade_effect_immediately** | **bool** | DowngradeEffectImmediately, whether subscription downgrade should effect immediately or at period end, default at period end | [optional] 
**incomplete_expire_time** | **int** | IncompleteExpireTime, em.. default 1day for plan of month type | [optional] 
**invoice_email** | **bool** | InvoiceEmail, whether to send invoice email to user, default yes | [optional] 
**upgrade_proration** | **bool** | UpgradeProration, whether subscription update generation proration invoice or not, default yes | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_config_update_req import UnibeeApiMerchantSubscriptionConfigUpdateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionConfigUpdateReq from a JSON string
unibee_api_merchant_subscription_config_update_req_instance = UnibeeApiMerchantSubscriptionConfigUpdateReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionConfigUpdateReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_config_update_req_dict = unibee_api_merchant_subscription_config_update_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionConfigUpdateReq from a dict
unibee_api_merchant_subscription_config_update_req_form_dict = unibee_api_merchant_subscription_config_update_req.from_dict(unibee_api_merchant_subscription_config_update_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


