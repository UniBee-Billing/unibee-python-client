# UnibeeApiBeanInvoiceItemSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**amount_excluding_tax** | **int** |  | [optional] 
**currency** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**period_end** | **int** |  | [optional] 
**period_start** | **int** |  | [optional] 
**proration** | **bool** |  | [optional] 
**quantity** | **int** |  | [optional] 
**tax** | **int** |  | [optional] 
**tax_scale** | **int** | Tax Scale，1000 &#x3D; 10% | [optional] 
**unit_amount_excluding_tax** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_invoice_item_simplify import UnibeeApiBeanInvoiceItemSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanInvoiceItemSimplify from a JSON string
unibee_api_bean_invoice_item_simplify_instance = UnibeeApiBeanInvoiceItemSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanInvoiceItemSimplify.to_json()

# convert the object into a dict
unibee_api_bean_invoice_item_simplify_dict = unibee_api_bean_invoice_item_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanInvoiceItemSimplify from a dict
unibee_api_bean_invoice_item_simplify_form_dict = unibee_api_bean_invoice_item_simplify.from_dict(unibee_api_bean_invoice_item_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


