# UnibeeApiBeanMerchantMemberSimplify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_time** | **int** | create utc time | [optional] 
**email** | **str** | email | [optional] 
**first_name** | **str** | first name | [optional] 
**id** | **int** | userId | [optional] 
**last_name** | **str** | last name | [optional] 
**merchant_id** | **int** | merchant id | [optional] 
**mobile** | **str** | mobile | [optional] 

## Example

```python
from openapi_client.models.unibee_api_bean_merchant_member_simplify import UnibeeApiBeanMerchantMemberSimplify

# TODO update the JSON string below
json = "{}"
# create an instance of UnibeeApiBeanMerchantMemberSimplify from a JSON string
unibee_api_bean_merchant_member_simplify_instance = UnibeeApiBeanMerchantMemberSimplify.from_json(json)
# print the JSON string representation of the object
print UnibeeApiBeanMerchantMemberSimplify.to_json()

# convert the object into a dict
unibee_api_bean_merchant_member_simplify_dict = unibee_api_bean_merchant_member_simplify_instance.to_dict()
# create an instance of UnibeeApiBeanMerchantMemberSimplify from a dict
unibee_api_bean_merchant_member_simplify_form_dict = unibee_api_bean_merchant_member_simplify.from_dict(unibee_api_bean_merchant_member_simplify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


