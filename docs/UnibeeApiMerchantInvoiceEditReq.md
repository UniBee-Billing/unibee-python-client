# UnibeeApiMerchantInvoiceEditReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency | [optional] 
**finish** | **bool** |  | [optional] 
**gateway_id** | **int** | Gateway Id | [optional] 
**invoice_id** | **str** | InvoiceId | 
**lines** | [**List[UnibeeApiMerchantInvoiceNewInvoiceItemParam]**](UnibeeApiMerchantInvoiceNewInvoiceItemParam.md) |  | [optional] 
**name** | **str** | Name | [optional] 
**tax_scale** | **int** | TaxScale，1000 represent 10% | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_invoice_edit_req import UnibeeApiMerchantInvoiceEditReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantInvoiceEditReq from a JSON string
unibee_api_merchant_invoice_edit_req_instance = UnibeeApiMerchantInvoiceEditReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantInvoiceEditReq.to_json()

# convert the object into a dict
unibee_api_merchant_invoice_edit_req_dict = unibee_api_merchant_invoice_edit_req_instance.to_dict()
# create an instance of UnibeeApiMerchantInvoiceEditReq from a dict
unibee_api_merchant_invoice_edit_req_form_dict = unibee_api_merchant_invoice_edit_req.from_dict(unibee_api_merchant_invoice_edit_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


