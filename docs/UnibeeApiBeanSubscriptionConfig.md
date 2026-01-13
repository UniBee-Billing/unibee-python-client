# UnibeeApiBeanSubscriptionConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downgrade_effect_immediately** | **bool** | DowngradeEffectImmediately, whether subscription update should effect immediately or at period end, default at period end | [optional] 
**incomplete_expire_time** | **int** | IncompleteExpireTime, em.. default 1day for plan of month type | [optional] 
**invoice_email** | **bool** | InvoiceEmail, whether to send invoice email to user, default yes | [optional] 
**upgrade_proration** | **bool** | UpgradeProration, whether subscription update generation proration invoice or not, default yes | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_subscription_config import UnibeeApiBeanSubscriptionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanSubscriptionConfig from a JSON string
unibee_api_bean_subscription_config_instance = UnibeeApiBeanSubscriptionConfig.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanSubscriptionConfig.to_json()

# convert the object into a dict
unibee_api_bean_subscription_config_dict = unibee_api_bean_subscription_config_instance.to_dict()
# create an instance of UnibeeApiBeanSubscriptionConfig from a dict
unibee_api_bean_subscription_config_form_dict = unibee_api_bean_subscription_config.from_dict(unibee_api_bean_subscription_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


