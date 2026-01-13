# UnibeeApiMerchantPaymentDetailRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_detail** | [**UnibeeApiMerchantPaymentPaymentDetail**](UnibeeApiMerchantPaymentPaymentDetail.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_detail_res import UnibeeApiMerchantPaymentDetailRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentDetailRes from a JSON string
unibee_api_merchant_payment_detail_res_instance = UnibeeApiMerchantPaymentDetailRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentDetailRes.to_json()

# convert the object into a dict
unibee_api_merchant_payment_detail_res_dict = unibee_api_merchant_payment_detail_res_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentDetailRes from a dict
unibee_api_merchant_payment_detail_res_form_dict = unibee_api_merchant_payment_detail_res.from_dict(unibee_api_merchant_payment_detail_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


