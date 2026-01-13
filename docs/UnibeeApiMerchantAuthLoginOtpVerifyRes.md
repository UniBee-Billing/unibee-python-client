# UnibeeApiMerchantAuthLoginOtpVerifyRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**merchant_member** | [**UnibeeApiBeanMerchantMemberSimplify**](UnibeeApiBeanMerchantMemberSimplify.md) |  | [optional] 
**token** | **str** | Token | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_auth_login_otp_verify_res import UnibeeApiMerchantAuthLoginOtpVerifyRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantAuthLoginOtpVerifyRes from a JSON string
unibee_api_merchant_auth_login_otp_verify_res_instance = UnibeeApiMerchantAuthLoginOtpVerifyRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantAuthLoginOtpVerifyRes.to_json()

# convert the object into a dict
unibee_api_merchant_auth_login_otp_verify_res_dict = unibee_api_merchant_auth_login_otp_verify_res_instance.to_dict()
# create an instance of UnibeeApiMerchantAuthLoginOtpVerifyRes from a dict
unibee_api_merchant_auth_login_otp_verify_res_form_dict = unibee_api_merchant_auth_login_otp_verify_res.from_dict(unibee_api_merchant_auth_login_otp_verify_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


