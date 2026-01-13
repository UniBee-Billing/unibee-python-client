# MerchantAuthSsoLoginPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_member** | [**UnibeeApiBeanMerchantMemberSimplify**](UnibeeApiBeanMerchantMemberSimplify.md) |  | [optional] 
**token** | **str** | Token | [optional] 

## Example

```python
from openapi_client.models.merchant_auth_sso_login_post200_response_data import MerchantAuthSsoLoginPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantAuthSsoLoginPost200ResponseData from a JSON string
merchant_auth_sso_login_post200_response_data_instance = MerchantAuthSsoLoginPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantAuthSsoLoginPost200ResponseData.to_json()

# convert the object into a dict
merchant_auth_sso_login_post200_response_data_dict = merchant_auth_sso_login_post200_response_data_instance.to_dict()
# create an instance of MerchantAuthSsoLoginPost200ResponseData from a dict
merchant_auth_sso_login_post200_response_data_form_dict = merchant_auth_sso_login_post200_response_data.from_dict(merchant_auth_sso_login_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


