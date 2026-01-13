# UnibeeApiBeanInvoiceSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**biz_type** | **int** | biz type from payment 1-single payment, 3-subscription | [optional] 
**crypto_amount** | **int** | crypto_amount, cent | [optional] 
**crypto_currency** | **str** | crypto_currency | [optional] 
**currency** | **str** |  | [optional] 
**day_util_due** | **int** | day util due after finish | [optional] 
**finish_time** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**invoice_name** | **str** |  | [optional] 
**lines** | [**List[UnibeeApiBeanInvoiceItemSimplify]**](UnibeeApiBeanInvoiceItemSimplify.md) |  | [optional] 
**link** | **str** | invoice link | [optional] 
**payment_id** | **str** | paymentId | [optional] 
**payment_link** | **str** | invoice payment link | [optional] 
**period_end** | **int** |  | [optional] 
**period_start** | **int** |  | [optional] 
**proration_date** | **int** |  | [optional] 
**proration_scale** | **int** |  | [optional] 
**refund_id** | **str** | refundId | [optional] 
**send_status** | **int** | email send status，0-No | 1- YES| 2-Unnecessary | [optional] 
**status** | **int** | status，0-Init | 1-pending｜2-processing｜3-paid | 4-failed | 5-cancelled | [optional] 
**subscription_amount** | **int** |  | [optional] 
**subscription_amount_excluding_tax** | **int** |  | [optional] 
**tax_amount** | **int** |  | [optional] 
**tax_scale** | **int** | Tax Scale，1000 &#x3D; 10% | [optional] 
**total_amount** | **int** |  | [optional] 
**total_amount_excluding_tax** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_invoice_simplify import UnibeeApiBeanInvoiceSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanInvoiceSimplify from a JSON string
unibee_api_bean_invoice_simplify_instance = UnibeeApiBeanInvoiceSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanInvoiceSimplify.to_json()

# convert the object into a dict
unibee_api_bean_invoice_simplify_dict = unibee_api_bean_invoice_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanInvoiceSimplify from a dict
unibee_api_bean_invoice_simplify_form_dict = unibee_api_bean_invoice_simplify.from_dict(unibee_api_bean_invoice_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


