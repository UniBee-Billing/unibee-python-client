# UnibeeApiBeanSubscriptionSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_data** | **str** | plan addon json data | [optional] 
**amount** | **int** | amount, cent | [optional] 
**billing_cycle_anchor** | **int** | billing_cycle_anchor | [optional] 
**cancel_at_period_end** | **int** | whether cancel at period end，0-false | 1-true | [optional] 
**cancel_reason** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**create_time** | **int** | create utc time | [optional] 
**currency** | **str** | currency | [optional] 
**current_period_end** | **int** | current_period_end, utc time | [optional] 
**current_period_start** | **int** | current_period_start, utc time | [optional] 
**dunning_time** | **int** | dunning_time, utc time | [optional] 
**first_paid_time** | **int** | first success payment time | [optional] 
**gas_payer** | **str** | who pay the gas, merchant|user | [optional] 
**gateway_id** | **int** | gateway_id | [optional] 
**gateway_item_data** | **str** | gateway_item_data | [optional] 
**gateway_status** | **str** | gateway status，Stripe：https://stripe.com/docs/billing/subscriptions/webhooks  Paypal：https://developer.paypal.com/docs/api/subscriptions/v1/#subscriptions_get | [optional] 
**id** | **int** |  | [optional] 
**last_update_time** | **int** |  | [optional] 
**latest_invoice_id** | **str** | latest_invoice_id | [optional] 
**link** | **str** |  | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 
**pending_update_id** | **str** |  | [optional] 
**plan_id** | **int** | plan id | [optional] 
**quantity** | **int** | quantity | [optional] 
**return_url** | **str** |  | [optional] 
**status** | **int** | status，0-Init | 1-Create｜2-Active｜3-PendingInActive | 4-Cancel | 5-Expire | 6- Suspend| 7-Incomplete | [optional] 
**subscription_id** | **str** | subscription id | [optional] 
**task_time** | **str** | task_time | [optional] 
**tax_scale** | **int** | Tax Scale，1000 &#x3D; 10% | [optional] 
**test_clock** | **int** | test_clock, simulator clock for subscription, if set , sub will out of cronjob controll | [optional] 
**trial_end** | **int** | trial_end, utc time | [optional] 
**type** | **int** | sub type, 0-gateway sub, 1-unibee sub | [optional] 
**user_id** | **int** | userId | [optional] 
**vat_number** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_subscription_simplify import UnibeeApiBeanSubscriptionSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanSubscriptionSimplify from a JSON string
unibee_api_bean_subscription_simplify_instance = UnibeeApiBeanSubscriptionSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanSubscriptionSimplify.to_json()

# convert the object into a dict
unibee_api_bean_subscription_simplify_dict = unibee_api_bean_subscription_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanSubscriptionSimplify from a dict
unibee_api_bean_subscription_simplify_form_dict = unibee_api_bean_subscription_simplify.from_dict(unibee_api_bean_subscription_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


