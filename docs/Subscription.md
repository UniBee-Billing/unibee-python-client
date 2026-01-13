# openapi_client.Subscription

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**subscription_add_new_trial_start_post**](Subscription.md#subscription_add_new_trial_start_post) | **POST** /merchant/subscription/add_new_trial_start | Merchant Edit Subscription-add appendTrialEndHour For Free
[**subscription_cancel_at_period_end_post**](Subscription.md#subscription_cancel_at_period_end_post) | **POST** /merchant/subscription/cancel_at_period_end | Merchant Edit Subscription-Set Cancel Ad Period End
[**subscription_cancel_last_cancel_at_period_end_post**](Subscription.md#subscription_cancel_last_cancel_at_period_end_post) | **POST** /merchant/subscription/cancel_last_cancel_at_period_end | Merchant Edit Subscription-Cancel Last CancelAtPeriod
[**subscription_cancel_post**](Subscription.md#subscription_cancel_post) | **POST** /merchant/subscription/cancel | Merchant Cancel Subscription Immediately (Will Not Generate Proration Invoice)
[**subscription_change_gateway_post**](Subscription.md#subscription_change_gateway_post) | **POST** /merchant/subscription/change_gateway | Change Subscription Gateway
[**subscription_config_get**](Subscription.md#subscription_config_get) | **GET** /merchant/subscription/config | Get Merchant Subscription Config
[**subscription_config_update_get**](Subscription.md#subscription_config_update_get) | **GET** /merchant/subscription/config/update | Update Merchant Subscription Config
[**subscription_create_preview_post**](Subscription.md#subscription_create_preview_post) | **POST** /merchant/subscription/create_preview | Create Subscription Preview
[**subscription_create_submit_post**](Subscription.md#subscription_create_submit_post) | **POST** /merchant/subscription/create_submit | Create Subscription
[**subscription_detail_get**](Subscription.md#subscription_detail_get) | **GET** /merchant/subscription/detail | Subscription Detail
[**subscription_detail_post**](Subscription.md#subscription_detail_post) | **POST** /merchant/subscription/detail | Subscription Detail
[**subscription_list_get**](Subscription.md#subscription_list_get) | **GET** /merchant/subscription/list | Subscription List
[**subscription_list_post**](Subscription.md#subscription_list_post) | **POST** /merchant/subscription/list | Subscription List
[**subscription_renew_post**](Subscription.md#subscription_renew_post) | **POST** /merchant/subscription/renew | Renew Subscription, will create new subscription based on one provided 
[**subscription_resume_post**](Subscription.md#subscription_resume_post) | **POST** /merchant/subscription/resume | Merchant Edit Subscription-Resume
[**subscription_suspend_post**](Subscription.md#subscription_suspend_post) | **POST** /merchant/subscription/suspend | Merchant Edit Subscription-Stop
[**subscription_update_preview_post**](Subscription.md#subscription_update_preview_post) | **POST** /merchant/subscription/update_preview | Merchant Update Subscription Preview
[**subscription_update_submit_post**](Subscription.md#subscription_update_submit_post) | **POST** /merchant/subscription/update_submit | Merchant Update Subscription Submit
[**subscription_user_subscription_detail_get**](Subscription.md#subscription_user_subscription_detail_get) | **GET** /merchant/subscription/user_subscription_detail | Subscription Detail
[**subscription_user_subscription_detail_post**](Subscription.md#subscription_user_subscription_detail_post) | **POST** /merchant/subscription/user_subscription_detail | Subscription Detail


# **subscription_add_new_trial_start_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_add_new_trial_start_post(unibee_api_merchant_subscription_add_new_trial_start_req)

Merchant Edit Subscription-add appendTrialEndHour For Free

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_add_new_trial_start_req import UnibeeApiMerchantSubscriptionAddNewTrialStartReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_add_new_trial_start_req = openapi_client.UnibeeApiMerchantSubscriptionAddNewTrialStartReq() # UnibeeApiMerchantSubscriptionAddNewTrialStartReq | 

    try:
        # Merchant Edit Subscription-add appendTrialEndHour For Free
        api_response = api_instance.subscription_add_new_trial_start_post(unibee_api_merchant_subscription_add_new_trial_start_req)
        print("The response of Subscription->subscription_add_new_trial_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_add_new_trial_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_add_new_trial_start_req** | [**UnibeeApiMerchantSubscriptionAddNewTrialStartReq**](UnibeeApiMerchantSubscriptionAddNewTrialStartReq.md)|  | 

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

# **subscription_cancel_at_period_end_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_cancel_at_period_end_post(unibee_api_merchant_subscription_cancel_at_period_end_req)

Merchant Edit Subscription-Set Cancel Ad Period End

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_cancel_at_period_end_req import UnibeeApiMerchantSubscriptionCancelAtPeriodEndReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_cancel_at_period_end_req = openapi_client.UnibeeApiMerchantSubscriptionCancelAtPeriodEndReq() # UnibeeApiMerchantSubscriptionCancelAtPeriodEndReq | 

    try:
        # Merchant Edit Subscription-Set Cancel Ad Period End
        api_response = api_instance.subscription_cancel_at_period_end_post(unibee_api_merchant_subscription_cancel_at_period_end_req)
        print("The response of Subscription->subscription_cancel_at_period_end_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_cancel_at_period_end_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_cancel_at_period_end_req** | [**UnibeeApiMerchantSubscriptionCancelAtPeriodEndReq**](UnibeeApiMerchantSubscriptionCancelAtPeriodEndReq.md)|  | 

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

# **subscription_cancel_last_cancel_at_period_end_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_cancel_last_cancel_at_period_end_post(unibee_api_merchant_subscription_cancel_last_cancel_at_period_end_req)

Merchant Edit Subscription-Cancel Last CancelAtPeriod

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_cancel_last_cancel_at_period_end_req import UnibeeApiMerchantSubscriptionCancelLastCancelAtPeriodEndReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_cancel_last_cancel_at_period_end_req = openapi_client.UnibeeApiMerchantSubscriptionCancelLastCancelAtPeriodEndReq() # UnibeeApiMerchantSubscriptionCancelLastCancelAtPeriodEndReq | 

    try:
        # Merchant Edit Subscription-Cancel Last CancelAtPeriod
        api_response = api_instance.subscription_cancel_last_cancel_at_period_end_post(unibee_api_merchant_subscription_cancel_last_cancel_at_period_end_req)
        print("The response of Subscription->subscription_cancel_last_cancel_at_period_end_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_cancel_last_cancel_at_period_end_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_cancel_last_cancel_at_period_end_req** | [**UnibeeApiMerchantSubscriptionCancelLastCancelAtPeriodEndReq**](UnibeeApiMerchantSubscriptionCancelLastCancelAtPeriodEndReq.md)|  | 

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

# **subscription_cancel_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_cancel_post(unibee_api_merchant_subscription_cancel_req)

Merchant Cancel Subscription Immediately (Will Not Generate Proration Invoice)

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_cancel_req import UnibeeApiMerchantSubscriptionCancelReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_cancel_req = openapi_client.UnibeeApiMerchantSubscriptionCancelReq() # UnibeeApiMerchantSubscriptionCancelReq | 

    try:
        # Merchant Cancel Subscription Immediately (Will Not Generate Proration Invoice)
        api_response = api_instance.subscription_cancel_post(unibee_api_merchant_subscription_cancel_req)
        print("The response of Subscription->subscription_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_cancel_req** | [**UnibeeApiMerchantSubscriptionCancelReq**](UnibeeApiMerchantSubscriptionCancelReq.md)|  | 

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

# **subscription_change_gateway_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_change_gateway_post(unibee_api_merchant_subscription_change_gateway_req)

Change Subscription Gateway

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_change_gateway_req import UnibeeApiMerchantSubscriptionChangeGatewayReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_change_gateway_req = openapi_client.UnibeeApiMerchantSubscriptionChangeGatewayReq() # UnibeeApiMerchantSubscriptionChangeGatewayReq | 

    try:
        # Change Subscription Gateway
        api_response = api_instance.subscription_change_gateway_post(unibee_api_merchant_subscription_change_gateway_req)
        print("The response of Subscription->subscription_change_gateway_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_change_gateway_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_change_gateway_req** | [**UnibeeApiMerchantSubscriptionChangeGatewayReq**](UnibeeApiMerchantSubscriptionChangeGatewayReq.md)|  | 

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

# **subscription_config_get**
> MerchantSubscriptionConfigGet200Response subscription_config_get()

Get Merchant Subscription Config

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_config_get200_response import MerchantSubscriptionConfigGet200Response
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
    api_instance = openapi_client.Subscription(api_client)

    try:
        # Get Merchant Subscription Config
        api_response = api_instance.subscription_config_get()
        print("The response of Subscription->subscription_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_config_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantSubscriptionConfigGet200Response**](MerchantSubscriptionConfigGet200Response.md)

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

# **subscription_config_update_get**
> MerchantSubscriptionConfigGet200Response subscription_config_update_get(downgrade_effect_immediately=downgrade_effect_immediately, upgrade_proration=upgrade_proration, incomplete_expire_time=incomplete_expire_time, invoice_email=invoice_email)

Update Merchant Subscription Config

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_config_get200_response import MerchantSubscriptionConfigGet200Response
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
    api_instance = openapi_client.Subscription(api_client)
    downgrade_effect_immediately = True # bool | DowngradeEffectImmediately, whether subscription downgrade should effect immediately or at period end, default at period end (optional)
    upgrade_proration = True # bool | UpgradeProration, whether subscription update generation proration invoice or not, default yes (optional)
    incomplete_expire_time = 56 # int | IncompleteExpireTime, em.. default 1day for plan of month type (optional)
    invoice_email = True # bool | InvoiceEmail, whether to send invoice email to user, default yes (optional)

    try:
        # Update Merchant Subscription Config
        api_response = api_instance.subscription_config_update_get(downgrade_effect_immediately=downgrade_effect_immediately, upgrade_proration=upgrade_proration, incomplete_expire_time=incomplete_expire_time, invoice_email=invoice_email)
        print("The response of Subscription->subscription_config_update_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_config_update_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **downgrade_effect_immediately** | **bool**| DowngradeEffectImmediately, whether subscription downgrade should effect immediately or at period end, default at period end | [optional] 
 **upgrade_proration** | **bool**| UpgradeProration, whether subscription update generation proration invoice or not, default yes | [optional] 
 **incomplete_expire_time** | **int**| IncompleteExpireTime, em.. default 1day for plan of month type | [optional] 
 **invoice_email** | **bool**| InvoiceEmail, whether to send invoice email to user, default yes | [optional] 

### Return type

[**MerchantSubscriptionConfigGet200Response**](MerchantSubscriptionConfigGet200Response.md)

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

# **subscription_create_preview_post**
> MerchantSubscriptionCreatePreviewPost200Response subscription_create_preview_post(unibee_api_merchant_subscription_create_preview_req)

Create Subscription Preview

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_create_preview_post200_response import MerchantSubscriptionCreatePreviewPost200Response
from openapi_client.models.unibee_api_merchant_subscription_create_preview_req import UnibeeApiMerchantSubscriptionCreatePreviewReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_create_preview_req = openapi_client.UnibeeApiMerchantSubscriptionCreatePreviewReq() # UnibeeApiMerchantSubscriptionCreatePreviewReq | 

    try:
        # Create Subscription Preview
        api_response = api_instance.subscription_create_preview_post(unibee_api_merchant_subscription_create_preview_req)
        print("The response of Subscription->subscription_create_preview_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_create_preview_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_create_preview_req** | [**UnibeeApiMerchantSubscriptionCreatePreviewReq**](UnibeeApiMerchantSubscriptionCreatePreviewReq.md)|  | 

### Return type

[**MerchantSubscriptionCreatePreviewPost200Response**](MerchantSubscriptionCreatePreviewPost200Response.md)

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

# **subscription_create_submit_post**
> MerchantSubscriptionCreateSubmitPost200Response subscription_create_submit_post(unibee_api_merchant_subscription_create_req)

Create Subscription

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_create_submit_post200_response import MerchantSubscriptionCreateSubmitPost200Response
from openapi_client.models.unibee_api_merchant_subscription_create_req import UnibeeApiMerchantSubscriptionCreateReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_create_req = openapi_client.UnibeeApiMerchantSubscriptionCreateReq() # UnibeeApiMerchantSubscriptionCreateReq | 

    try:
        # Create Subscription
        api_response = api_instance.subscription_create_submit_post(unibee_api_merchant_subscription_create_req)
        print("The response of Subscription->subscription_create_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_create_submit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_create_req** | [**UnibeeApiMerchantSubscriptionCreateReq**](UnibeeApiMerchantSubscriptionCreateReq.md)|  | 

### Return type

[**MerchantSubscriptionCreateSubmitPost200Response**](MerchantSubscriptionCreateSubmitPost200Response.md)

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

# **subscription_detail_get**
> MerchantSubscriptionDetailGet200Response subscription_detail_get(subscription_id)

Subscription Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_detail_get200_response import MerchantSubscriptionDetailGet200Response
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
    api_instance = openapi_client.Subscription(api_client)
    subscription_id = 'subscription_id_example' # str | SubscriptionId

    try:
        # Subscription Detail
        api_response = api_instance.subscription_detail_get(subscription_id)
        print("The response of Subscription->subscription_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| SubscriptionId | 

### Return type

[**MerchantSubscriptionDetailGet200Response**](MerchantSubscriptionDetailGet200Response.md)

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

# **subscription_detail_post**
> MerchantSubscriptionDetailGet200Response subscription_detail_post(unibee_api_merchant_subscription_detail_req)

Subscription Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_detail_get200_response import MerchantSubscriptionDetailGet200Response
from openapi_client.models.unibee_api_merchant_subscription_detail_req import UnibeeApiMerchantSubscriptionDetailReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_detail_req = openapi_client.UnibeeApiMerchantSubscriptionDetailReq() # UnibeeApiMerchantSubscriptionDetailReq | 

    try:
        # Subscription Detail
        api_response = api_instance.subscription_detail_post(unibee_api_merchant_subscription_detail_req)
        print("The response of Subscription->subscription_detail_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_detail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_detail_req** | [**UnibeeApiMerchantSubscriptionDetailReq**](UnibeeApiMerchantSubscriptionDetailReq.md)|  | 

### Return type

[**MerchantSubscriptionDetailGet200Response**](MerchantSubscriptionDetailGet200Response.md)

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

# **subscription_list_get**
> MerchantSubscriptionListGet200Response subscription_list_get(user_id=user_id, status=status, sort_field=sort_field, sort_type=sort_type, page=page, count=count)

Subscription List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_list_get200_response import MerchantSubscriptionListGet200Response
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
    api_instance = openapi_client.Subscription(api_client)
    user_id = 56 # int | UserId (optional)
    status = [56] # List[int] | Filter, Default All，Status，0-Init | 1-Create｜2-Active｜3-Suspend | 4-Cancel | 5-Expire (optional)
    sort_field = 'sort_field_example' # str | Sort Field，gmt_create|gmt_modify，Default gmt_modify (optional)
    sort_type = 'sort_type_example' # str | Sort Type，asc|desc，Default desc (optional)
    page = 56 # int | Page, Start WIth 0 (optional)
    count = 56 # int | Count Of Page (optional)

    try:
        # Subscription List
        api_response = api_instance.subscription_list_get(user_id=user_id, status=status, sort_field=sort_field, sort_type=sort_type, page=page, count=count)
        print("The response of Subscription->subscription_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| UserId | [optional] 
 **status** | [**List[int]**](int.md)| Filter, Default All，Status，0-Init | 1-Create｜2-Active｜3-Suspend | 4-Cancel | 5-Expire | [optional] 
 **sort_field** | **str**| Sort Field，gmt_create|gmt_modify，Default gmt_modify | [optional] 
 **sort_type** | **str**| Sort Type，asc|desc，Default desc | [optional] 
 **page** | **int**| Page, Start WIth 0 | [optional] 
 **count** | **int**| Count Of Page | [optional] 

### Return type

[**MerchantSubscriptionListGet200Response**](MerchantSubscriptionListGet200Response.md)

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

# **subscription_list_post**
> MerchantSubscriptionListGet200Response subscription_list_post(unibee_api_merchant_subscription_list_req)

Subscription List

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_list_get200_response import MerchantSubscriptionListGet200Response
from openapi_client.models.unibee_api_merchant_subscription_list_req import UnibeeApiMerchantSubscriptionListReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_list_req = openapi_client.UnibeeApiMerchantSubscriptionListReq() # UnibeeApiMerchantSubscriptionListReq | 

    try:
        # Subscription List
        api_response = api_instance.subscription_list_post(unibee_api_merchant_subscription_list_req)
        print("The response of Subscription->subscription_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_list_req** | [**UnibeeApiMerchantSubscriptionListReq**](UnibeeApiMerchantSubscriptionListReq.md)|  | 

### Return type

[**MerchantSubscriptionListGet200Response**](MerchantSubscriptionListGet200Response.md)

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

# **subscription_renew_post**
> MerchantSubscriptionCreateSubmitPost200Response subscription_renew_post(unibee_api_merchant_subscription_renew_req)

Renew Subscription, will create new subscription based on one provided 

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_create_submit_post200_response import MerchantSubscriptionCreateSubmitPost200Response
from openapi_client.models.unibee_api_merchant_subscription_renew_req import UnibeeApiMerchantSubscriptionRenewReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_renew_req = openapi_client.UnibeeApiMerchantSubscriptionRenewReq() # UnibeeApiMerchantSubscriptionRenewReq | 

    try:
        # Renew Subscription, will create new subscription based on one provided 
        api_response = api_instance.subscription_renew_post(unibee_api_merchant_subscription_renew_req)
        print("The response of Subscription->subscription_renew_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_renew_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_renew_req** | [**UnibeeApiMerchantSubscriptionRenewReq**](UnibeeApiMerchantSubscriptionRenewReq.md)|  | 

### Return type

[**MerchantSubscriptionCreateSubmitPost200Response**](MerchantSubscriptionCreateSubmitPost200Response.md)

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

# **subscription_resume_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_resume_post(unibee_api_merchant_subscription_resume_req)

Merchant Edit Subscription-Resume

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_resume_req import UnibeeApiMerchantSubscriptionResumeReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_resume_req = openapi_client.UnibeeApiMerchantSubscriptionResumeReq() # UnibeeApiMerchantSubscriptionResumeReq | 

    try:
        # Merchant Edit Subscription-Resume
        api_response = api_instance.subscription_resume_post(unibee_api_merchant_subscription_resume_req)
        print("The response of Subscription->subscription_resume_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_resume_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_resume_req** | [**UnibeeApiMerchantSubscriptionResumeReq**](UnibeeApiMerchantSubscriptionResumeReq.md)|  | 

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

# **subscription_suspend_post**
> MerchantAuthSsoLoginOTPPost200Response subscription_suspend_post(unibee_api_merchant_subscription_suspend_req)

Merchant Edit Subscription-Stop

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_subscription_suspend_req import UnibeeApiMerchantSubscriptionSuspendReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_suspend_req = openapi_client.UnibeeApiMerchantSubscriptionSuspendReq() # UnibeeApiMerchantSubscriptionSuspendReq | 

    try:
        # Merchant Edit Subscription-Stop
        api_response = api_instance.subscription_suspend_post(unibee_api_merchant_subscription_suspend_req)
        print("The response of Subscription->subscription_suspend_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_suspend_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_suspend_req** | [**UnibeeApiMerchantSubscriptionSuspendReq**](UnibeeApiMerchantSubscriptionSuspendReq.md)|  | 

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

# **subscription_update_preview_post**
> MerchantSubscriptionUpdatePreviewPost200Response subscription_update_preview_post(unibee_api_merchant_subscription_update_preview_req)

Merchant Update Subscription Preview

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_update_preview_post200_response import MerchantSubscriptionUpdatePreviewPost200Response
from openapi_client.models.unibee_api_merchant_subscription_update_preview_req import UnibeeApiMerchantSubscriptionUpdatePreviewReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_update_preview_req = openapi_client.UnibeeApiMerchantSubscriptionUpdatePreviewReq() # UnibeeApiMerchantSubscriptionUpdatePreviewReq | 

    try:
        # Merchant Update Subscription Preview
        api_response = api_instance.subscription_update_preview_post(unibee_api_merchant_subscription_update_preview_req)
        print("The response of Subscription->subscription_update_preview_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_update_preview_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_update_preview_req** | [**UnibeeApiMerchantSubscriptionUpdatePreviewReq**](UnibeeApiMerchantSubscriptionUpdatePreviewReq.md)|  | 

### Return type

[**MerchantSubscriptionUpdatePreviewPost200Response**](MerchantSubscriptionUpdatePreviewPost200Response.md)

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

# **subscription_update_submit_post**
> MerchantSubscriptionUpdateSubmitPost200Response subscription_update_submit_post(unibee_api_merchant_subscription_update_req)

Merchant Update Subscription Submit

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_update_submit_post200_response import MerchantSubscriptionUpdateSubmitPost200Response
from openapi_client.models.unibee_api_merchant_subscription_update_req import UnibeeApiMerchantSubscriptionUpdateReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_update_req = openapi_client.UnibeeApiMerchantSubscriptionUpdateReq() # UnibeeApiMerchantSubscriptionUpdateReq | 

    try:
        # Merchant Update Subscription Submit
        api_response = api_instance.subscription_update_submit_post(unibee_api_merchant_subscription_update_req)
        print("The response of Subscription->subscription_update_submit_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_update_submit_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_update_req** | [**UnibeeApiMerchantSubscriptionUpdateReq**](UnibeeApiMerchantSubscriptionUpdateReq.md)|  | 

### Return type

[**MerchantSubscriptionUpdateSubmitPost200Response**](MerchantSubscriptionUpdateSubmitPost200Response.md)

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

# **subscription_user_subscription_detail_get**
> MerchantSubscriptionUserSubscriptionDetailGet200Response subscription_user_subscription_detail_get(user_id)

Subscription Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_user_subscription_detail_get200_response import MerchantSubscriptionUserSubscriptionDetailGet200Response
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
    api_instance = openapi_client.Subscription(api_client)
    user_id = 56 # int | UserId

    try:
        # Subscription Detail
        api_response = api_instance.subscription_user_subscription_detail_get(user_id)
        print("The response of Subscription->subscription_user_subscription_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_user_subscription_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| UserId | 

### Return type

[**MerchantSubscriptionUserSubscriptionDetailGet200Response**](MerchantSubscriptionUserSubscriptionDetailGet200Response.md)

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

# **subscription_user_subscription_detail_post**
> MerchantSubscriptionUserSubscriptionDetailGet200Response subscription_user_subscription_detail_post(unibee_api_merchant_subscription_user_subscription_detail_req)

Subscription Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_subscription_user_subscription_detail_get200_response import MerchantSubscriptionUserSubscriptionDetailGet200Response
from openapi_client.models.unibee_api_merchant_subscription_user_subscription_detail_req import UnibeeApiMerchantSubscriptionUserSubscriptionDetailReq
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
    api_instance = openapi_client.Subscription(api_client)
    unibee_api_merchant_subscription_user_subscription_detail_req = openapi_client.UnibeeApiMerchantSubscriptionUserSubscriptionDetailReq() # UnibeeApiMerchantSubscriptionUserSubscriptionDetailReq | 

    try:
        # Subscription Detail
        api_response = api_instance.subscription_user_subscription_detail_post(unibee_api_merchant_subscription_user_subscription_detail_req)
        print("The response of Subscription->subscription_user_subscription_detail_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Subscription->subscription_user_subscription_detail_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_subscription_user_subscription_detail_req** | [**UnibeeApiMerchantSubscriptionUserSubscriptionDetailReq**](UnibeeApiMerchantSubscriptionUserSubscriptionDetailReq.md)|  | 

### Return type

[**MerchantSubscriptionUserSubscriptionDetailGet200Response**](MerchantSubscriptionUserSubscriptionDetailGet200Response.md)

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

