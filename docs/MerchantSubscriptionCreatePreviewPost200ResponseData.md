# MerchantSubscriptionCreatePreviewPost200ResponseData


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
from openapi_client.models.merchant_subscription_create_preview_post200_response_data import MerchantSubscriptionCreatePreviewPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of MerchantSubscriptionCreatePreviewPost200ResponseData from a JSON string
merchant_subscription_create_preview_post200_response_data_instance = MerchantSubscriptionCreatePreviewPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print MerchantSubscriptionCreatePreviewPost200ResponseData.to_json()

# convert the object into a dict
merchant_subscription_create_preview_post200_response_data_dict = merchant_subscription_create_preview_post200_response_data_instance.to_dict()
# create an instance of MerchantSubscriptionCreatePreviewPost200ResponseData from a dict
merchant_subscription_create_preview_post200_response_data_form_dict = merchant_subscription_create_preview_post200_response_data.from_dict(merchant_subscription_create_preview_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


