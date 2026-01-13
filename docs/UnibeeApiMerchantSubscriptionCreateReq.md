# UnibeeApiMerchantSubscriptionCreateReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_params** | [**List[UnibeeApiBeanPlanAddonParam]**](UnibeeApiBeanPlanAddonParam.md) | addonParams | [optional] 
**confirm_currency** | **str** | Currency To Be Confirmed，Get From Preview | [optional] 
**confirm_total_amount** | **int** | TotalAmount To Be Confirmed，Get From Preview | [optional] 
**gateway_id** | **int** | Id | 
**metadata** | **Dict[str, str]** | Metadata，Map | [optional] 
**payment_method_id** | **str** | PaymentMethodId | [optional] 
**plan_id** | **int** | PlanId | 
**quantity** | **int** | Quantity，Default 1 | [optional] 
**return_url** | **str** | RedirectUrl | [optional] 
**user_id** | **int** | UserId | 
**vat_country_code** | **str** | VatCountryCode, CountryName | [optional] 
**vat_number** | **str** | VatNumber | [optional] 

## Example

```python
from openapi_client.models.unibee_api_merchant_subscription_create_req import UnibeeApiMerchantSubscriptionCreateReq

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiMerchantSubscriptionCreateReq from a JSON string
unibee_api_merchant_subscription_create_req_instance = UnibeeApiMerchantSubscriptionCreateReq.from_json(json)
# print the JSON string representation of the object
print UnibeeApiMerchantSubscriptionCreateReq.to_json()

# convert the object into a dict
unibee_api_merchant_subscription_create_req_dict = unibee_api_merchant_subscription_create_req_instance.to_dict()
# create an instance of UnibeeApiMerchantSubscriptionCreateReq from a dict
unibee_api_merchant_subscription_create_req_form_dict = unibee_api_merchant_subscription_create_req.from_dict(unibee_api_merchant_subscription_create_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


