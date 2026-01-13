# UnibeeApiMerchantProfileGetRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**List[UnibeeApiBeanCurrency]**](UnibeeApiBeanCurrency.md) | Currency List | [optional] 
**time_zone** | **List[str]** | TimeZone List | [optional] 
**env** | **str** | System Env, em: daily|stage|local|prod | [optional] 
**gateway** | [**List[UnibeeApiBeanGatewaySimplify]**](UnibeeApiBeanGatewaySimplify.md) | Gateway List | [optional] 
**is_prod** | **bool** | Check System Env Is Prod, true|false | [optional] 
**merchant** | [**UnibeeApiBeanMerchantSimplify**](UnibeeApiBeanMerchantSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_profile_get_res import UnibeeApiMerchantProfileGetRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantProfileGetRes from a JSON string
unibee_api_merchant_profile_get_res_instance = UnibeeApiMerchantProfileGetRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantProfileGetRes.to_json()

# convert the object into a dict
unibee_api_merchant_profile_get_res_dict = unibee_api_merchant_profile_get_res_instance.to_dict()
# create an instance of UnibeeApiMerchantProfileGetRes from a dict
unibee_api_merchant_profile_get_res_form_dict = unibee_api_merchant_profile_get_res.from_dict(unibee_api_merchant_profile_get_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


