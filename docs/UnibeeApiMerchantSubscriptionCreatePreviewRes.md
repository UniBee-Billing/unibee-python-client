# UnibeeApiMerchantSubscriptionCreatePreviewRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeApiBeanPlanAddonParam]**](UnibeeApiBeanPlanAddonParam.md) |  | [optional] 
**addons** | [**List[UnibeeApiBeanPlanAddonDetail]**](UnibeeApiBeanPlanAddonDetail.md) |  | [optional] 
**currency** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**gateway** | [**UnibeeApiBeanGatewaySimplify**](UnibeeApiBeanGatewaySimplify.md) |  | [optional] 
**invoice** | [**UnibeeApiBeanInvoiceSimplify**](UnibeeApiBeanInvoiceSimplify.md) |  | [optional] 
**plan** | [**UnibeeApiBeanPlanSimplify**](UnibeeApiBeanPlanSimplify.md) |  | [optional] 
**quantity** | **int** |  | [optional] 
**tax_scale** | **int** |  | [optional] 
**total_amount** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 
**vat_country_code** | **str** |  | [optional] 
**vat_country_name** | **str** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**vat_number_validate** | [**UnibeeApiBeanValidResult**](UnibeeApiBeanValidResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_create_preview_res import UnibeeApiMerchantSubscriptionCreatePreviewRes

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionCreatePreviewRes from a JSON string
unibee_api_merchant_subscription_create_preview_res_instance = UnibeeApiMerchantSubscriptionCreatePreviewRes.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionCreatePreviewRes.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_create_preview_res_dict = unibee_api_merchant_subscription_create_preview_res_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionCreatePreviewRes from a dict
unibee_api_merchant_subscription_create_preview_res_form_dict = unibee_api_merchant_subscription_create_preview_res.from_dict(unibee_api_merchant_subscription_create_preview_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


