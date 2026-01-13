# openapi_client.Plan

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**plan_activate_post**](Plan.md#plan_activate_post) | **POST** /merchant/plan/activate | Plan Sync To Gateway And Activate
[**plan_addons_binding_post**](Plan.md#plan_addons_binding_post) | **POST** /merchant/plan/addons_binding | Plan Binding Addons
[**plan_delete_post**](Plan.md#plan_delete_post) | **POST** /merchant/plan/delete | Delete A Plan Before Activate
[**plan_detail_get**](Plan.md#plan_detail_get) | **GET** /merchant/plan/detail | Plan Detail
[**plan_detail_post**](Plan.md#plan_detail_post) | **POST** /merchant/plan/detail | Plan Detail
[**plan_edit_post**](Plan.md#plan_edit_post) | **POST** /merchant/plan/edit | Edit Plan
[**plan_expire_post**](Plan.md#plan_expire_post) | **POST** /merchant/plan/expire | Expire A Plan
[**plan_list_get**](Plan.md#plan_list_get) | **GET** /merchant/plan/list | Plan List
[**plan_list_post**](Plan.md#plan_list_post) | **POST** /merchant/plan/list | Plan List
[**plan_new_post**](Plan.md#plan_new_post) | **POST** /merchant/plan/new | Create Plan
[**plan_publish_post**](Plan.md#plan_publish_post) | **POST** /merchant/plan/publish | Publish Plan，Will Be Visible To UserPortal
[**plan_unpublished_post**](Plan.md#plan_unpublished_post) | **POST** /merchant/plan/unpublished | UnPublish Plan


# **plan_activate_post**
> MerchantAuthSsoLoginOTPPost200Response plan_activate_post(unibee_api_merchant_plan_activate_req)

Plan Sync To Gateway And Activate

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_plan_activate_req import UnibeeApiMerchantPlanActivateReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_activate_req = openapi_client.UnibeeApiMerchantPlanActivateReq() # UnibeeApiMerchantPlanActivateReq | 

    try:
        # Plan Sync To Gateway And Activate
        api_response = api_instance.plan_activate_post(unibee_api_merchant_plan_activate_req)
        print("The response of Plan->plan_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_activate_req** | [**UnibeeApiMerchantPlanActivateReq**](UnibeeApiMerchantPlanActivateReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_addons_binding_post**
> MerchantPlanAddonsBindingPost200Response plan_addons_binding_post(unibee_api_merchant_plan_addons_binding_req)

Plan Binding Addons

### Example


```python
import openapi_client
from openapi_client.models.merchant_plan_addons_binding_post200_response import MerchantPlanAddonsBindingPost200Response
from openapi_client.models.unibee_api_merchant_plan_addons_binding_req import UnibeeApiMerchantPlanAddonsBindingReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_addons_binding_req = openapi_client.UnibeeApiMerchantPlanAddonsBindingReq() # UnibeeApiMerchantPlanAddonsBindingReq | 

    try:
        # Plan Binding Addons
        api_response = api_instance.plan_addons_binding_post(unibee_api_merchant_plan_addons_binding_req)
        print("The response of Plan->plan_addons_binding_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_addons_binding_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_addons_binding_req** | [**UnibeeApiMerchantPlanAddonsBindingReq**](UnibeeApiMerchantPlanAddonsBindingReq.md)|  | 

### Return type

[**MerchantPlanAddonsBindingPost200Response**](MerchantPlanAddonsBindingPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_delete_post**
> MerchantAuthSsoLoginOTPPost200Response plan_delete_post(unibee_api_merchant_plan_delete_req)

Delete A Plan Before Activate

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_plan_delete_req import UnibeeApiMerchantPlanDeleteReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_delete_req = openapi_client.UnibeeApiMerchantPlanDeleteReq() # UnibeeApiMerchantPlanDeleteReq | 

    try:
        # Delete A Plan Before Activate
        api_response = api_instance.plan_delete_post(unibee_api_merchant_plan_delete_req)
        print("The response of Plan->plan_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_delete_req** | [**UnibeeApiMerchantPlanDeleteReq**](UnibeeApiMerchantPlanDeleteReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_detail_get**
> MerchantPlanDetailGet200Response plan_detail_get(plan_id)

Plan Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_plan_detail_get200_response import MerchantPlanDetailGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    plan_id = 56 # int | PlanId

    try:
        # Plan Detail
        api_response = api_instance.plan_detail_get(plan_id)
        print("The response of Plan->plan_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**| PlanId | 

### Return type

[**MerchantPlanDetailGet200Response**](MerchantPlanDetailGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_detail_post**
> MerchantPlanDetailGet200Response plan_detail_post(unibee_api_merchant_plan_detail_req)

Plan Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_plan_detail_get200_response import MerchantPlanDetailGet200Response
from openapi_client.models.unibee_api_merchant_plan_detail_req import UnibeeApiMerchantPlanDetailReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_detail_req = openapi_client.UnibeeApiMerchantPlanDetailReq() # UnibeeApiMerchantPlanDetailReq | 

    try:
        # Plan Detail
        api_response = api_instance.plan_detail_post(unibee_api_merchant_plan_detail_req)
        print("The response of Plan->plan_detail_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_detail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_detail_req** | [**UnibeeApiMerchantPlanDetailReq**](UnibeeApiMerchantPlanDetailReq.md)|  | 

### Return type

[**MerchantPlanDetailGet200Response**](MerchantPlanDetailGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_edit_post**
> MerchantPlanAddonsBindingPost200Response plan_edit_post(unibee_api_merchant_plan_edit_req)

Edit Plan

### Example


```python
import openapi_client
from openapi_client.models.merchant_plan_addons_binding_post200_response import MerchantPlanAddonsBindingPost200Response
from openapi_client.models.unibee_api_merchant_plan_edit_req import UnibeeApiMerchantPlanEditReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_edit_req = openapi_client.UnibeeApiMerchantPlanEditReq() # UnibeeApiMerchantPlanEditReq | 

    try:
        # Edit Plan
        api_response = api_instance.plan_edit_post(unibee_api_merchant_plan_edit_req)
        print("The response of Plan->plan_edit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_edit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_edit_req** | [**UnibeeApiMerchantPlanEditReq**](UnibeeApiMerchantPlanEditReq.md)|  | 

### Return type

[**MerchantPlanAddonsBindingPost200Response**](MerchantPlanAddonsBindingPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_expire_post**
> MerchantAuthSsoLoginOTPPost200Response plan_expire_post(unibee_api_merchant_plan_expire_req)

Expire A Plan

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_plan_expire_req import UnibeeApiMerchantPlanExpireReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_expire_req = openapi_client.UnibeeApiMerchantPlanExpireReq() # UnibeeApiMerchantPlanExpireReq | 

    try:
        # Expire A Plan
        api_response = api_instance.plan_expire_post(unibee_api_merchant_plan_expire_req)
        print("The response of Plan->plan_expire_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_expire_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_expire_req** | [**UnibeeApiMerchantPlanExpireReq**](UnibeeApiMerchantPlanExpireReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_list_get**
> MerchantPlanListGet200Response plan_list_get(type=type, status=status, publish_status=publish_status, currency=currency, sort_field=sort_field, sort_type=sort_type, page=page, count=count)

Plan List

### Example


```python
import openapi_client
from openapi_client.models.merchant_plan_list_get200_response import MerchantPlanListGet200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    type = [56] # List[int] | 1-main plan，2-addon plan (optional)
    status = [56] # List[int] | Filter, Default All，,Status，1-Editing，2-Active，3-InActive，4-Expired (optional)
    publish_status = 56 # int | Filter, Default All，PublishStatus，1-UnPublished，2-Published (optional)
    currency = 'currency_example' # str | Filter Currency (optional)
    sort_field = 'sort_field_example' # str | Sort Field，gmt_create|gmt_modify，Default gmt_modify (optional)
    sort_type = 'sort_type_example' # str | Sort Type，asc|desc，Default desc (optional)
    page = 56 # int | Page, Start 0 (optional)
    count = 56 # int | Count Of Per Page (optional)

    try:
        # Plan List
        api_response = api_instance.plan_list_get(type=type, status=status, publish_status=publish_status, currency=currency, sort_field=sort_field, sort_type=sort_type, page=page, count=count)
        print("The response of Plan->plan_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**List[int]**](int.md)| 1-main plan，2-addon plan | [optional] 
 **status** | [**List[int]**](int.md)| Filter, Default All，,Status，1-Editing，2-Active，3-InActive，4-Expired | [optional] 
 **publish_status** | **int**| Filter, Default All，PublishStatus，1-UnPublished，2-Published | [optional] 
 **currency** | **str**| Filter Currency | [optional] 
 **sort_field** | **str**| Sort Field，gmt_create|gmt_modify，Default gmt_modify | [optional] 
 **sort_type** | **str**| Sort Type，asc|desc，Default desc | [optional] 
 **page** | **int**| Page, Start 0 | [optional] 
 **count** | **int**| Count Of Per Page | [optional] 

### Return type

[**MerchantPlanListGet200Response**](MerchantPlanListGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_list_post**
> MerchantPlanListGet200Response plan_list_post(unibee_api_merchant_plan_list_req)

Plan List

### Example


```python
import openapi_client
from openapi_client.models.merchant_plan_list_get200_response import MerchantPlanListGet200Response
from openapi_client.models.unibee_api_merchant_plan_list_req import UnibeeApiMerchantPlanListReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_list_req = openapi_client.UnibeeApiMerchantPlanListReq() # UnibeeApiMerchantPlanListReq | 

    try:
        # Plan List
        api_response = api_instance.plan_list_post(unibee_api_merchant_plan_list_req)
        print("The response of Plan->plan_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_list_req** | [**UnibeeApiMerchantPlanListReq**](UnibeeApiMerchantPlanListReq.md)|  | 

### Return type

[**MerchantPlanListGet200Response**](MerchantPlanListGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_new_post**
> MerchantPlanAddonsBindingPost200Response plan_new_post(unibee_api_merchant_plan_new_req)

Create Plan

### Example


```python
import openapi_client
from openapi_client.models.merchant_plan_addons_binding_post200_response import MerchantPlanAddonsBindingPost200Response
from openapi_client.models.unibee_api_merchant_plan_new_req import UnibeeApiMerchantPlanNewReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_new_req = openapi_client.UnibeeApiMerchantPlanNewReq() # UnibeeApiMerchantPlanNewReq | 

    try:
        # Create Plan
        api_response = api_instance.plan_new_post(unibee_api_merchant_plan_new_req)
        print("The response of Plan->plan_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_new_req** | [**UnibeeApiMerchantPlanNewReq**](UnibeeApiMerchantPlanNewReq.md)|  | 

### Return type

[**MerchantPlanAddonsBindingPost200Response**](MerchantPlanAddonsBindingPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_publish_post**
> MerchantAuthSsoLoginOTPPost200Response plan_publish_post(unibee_api_merchant_plan_publish_req)

Publish Plan，Will Be Visible To UserPortal

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_plan_publish_req import UnibeeApiMerchantPlanPublishReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_publish_req = openapi_client.UnibeeApiMerchantPlanPublishReq() # UnibeeApiMerchantPlanPublishReq | 

    try:
        # Publish Plan，Will Be Visible To UserPortal
        api_response = api_instance.plan_publish_post(unibee_api_merchant_plan_publish_req)
        print("The response of Plan->plan_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_publish_req** | [**UnibeeApiMerchantPlanPublishReq**](UnibeeApiMerchantPlanPublishReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plan_unpublished_post**
> MerchantAuthSsoLoginOTPPost200Response plan_unpublished_post(unibee_api_merchant_plan_un_publish_req)

UnPublish Plan

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_plan_un_publish_req import UnibeeApiMerchantPlanUnPublishReq
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.Plan(api_client)
    unibee_api_merchant_plan_un_publish_req = openapi_client.UnibeeApiMerchantPlanUnPublishReq() # UnibeeApiMerchantPlanUnPublishReq | 

    try:
        # UnPublish Plan
        api_response = api_instance.plan_unpublished_post(unibee_api_merchant_plan_un_publish_req)
        print("The response of Plan->plan_unpublished_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Plan->plan_unpublished_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_plan_un_publish_req** | [**UnibeeApiMerchantPlanUnPublishReq**](UnibeeApiMerchantPlanUnPublishReq.md)|  | 

### Return type

[**MerchantAuthSsoLoginOTPPost200Response**](MerchantAuthSsoLoginOTPPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

