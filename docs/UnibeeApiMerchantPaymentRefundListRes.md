# UnibeeApiMerchantPaymentRefundListRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**refund_details** | [**List[UnibeeApiMerchantPaymentRefundDetail]**](UnibeeApiMerchantPaymentRefundDetail.md) | RefundDetails | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_payment_refund_list_res import UnibeeApiMerchantPaymentRefundListRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantPaymentRefundListRes from a JSON string
unibee_api_merchant_payment_refund_list_res_instance = UnibeeApiMerchantPaymentRefundListRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantPaymentRefundListRes.to_json()

# convert the object into a dict
unibee_api_merchant_payment_refund_list_res_dict = unibee_api_merchant_payment_refund_list_res_instance.to_dict()
# create an instance of UnibeeApiMerchantPaymentRefundListRes from a dict
unibee_api_merchant_payment_refund_list_res_form_dict = unibee_api_merchant_payment_refund_list_res.from_dict(unibee_api_merchant_payment_refund_list_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


