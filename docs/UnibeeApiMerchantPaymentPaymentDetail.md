# UnibeeApiMerchantPaymentPaymentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment** | [**UnibeeApiBeanPaymentSimplify**](UnibeeApiBeanPaymentSimplify.md) |  | [optional] 
**user** | [**UnibeeApiBeanUserAccountSimplify**](UnibeeApiBeanUserAccountSimplify.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_payment_detail import UnibeeApiMerchantPaymentPaymentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentPaymentDetail from a JSON string
unibee_api_merchant_payment_payment_detail_instance = UnibeeApiMerchantPaymentPaymentDetail.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentPaymentDetail.to_json()

# convert the object into a dict
unibee_api_merchant_payment_payment_detail_dict = unibee_api_merchant_payment_payment_detail_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentPaymentDetail from a dict
unibee_api_merchant_payment_payment_detail_form_dict = unibee_api_merchant_payment_payment_detail.from_dict(unibee_api_merchant_payment_payment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


