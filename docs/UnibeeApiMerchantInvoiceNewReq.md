# UnibeeApiMerchantInvoiceNewReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency | 
**finish** | **bool** |  | [optional] 
**gateway_id** | **int** | Gateway Id | 
**lines** | [**List[UnibeeApiMerchantInvoiceNewInvoiceItemParam]**](UnibeeApiMerchantInvoiceNewInvoiceItemParam.md) |  | [optional] 
**name** | **str** | Name | [optional] 
**tax_scale** | **int** | TaxScale，1000 represent 10% | 
**user_id** | **int** | UserId | 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_new_req import UnibeeApiMerchantInvoiceNewReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceNewReq from a JSON string
unibee_api_merchant_invoice_new_req_instance = UnibeeApiMerchantInvoiceNewReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceNewReq.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_new_req_dict = unibee_api_merchant_invoice_new_req_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceNewReq from a dict
unibee_api_merchant_invoice_new_req_form_dict = unibee_api_merchant_invoice_new_req.from_dict(unibee_api_merchant_invoice_new_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


