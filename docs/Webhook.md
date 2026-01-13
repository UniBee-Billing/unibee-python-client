# openapi_client.Webhook

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_delete_endpoint_post**](Webhook.md#webhook_delete_endpoint_post) | **POST** /merchant/webhook/delete_endpoint | Merchant Delete Webhook Endpoint
[**webhook_endpoint_list_get**](Webhook.md#webhook_endpoint_list_get) | **GET** /merchant/webhook/endpoint_list | Merchant Webhook Endpoint list
[**webhook_endpoint_log_list_get**](Webhook.md#webhook_endpoint_log_list_get) | **GET** /merchant/webhook/endpoint_log_list | Merchant Webhook Endpoint Log list
[**webhook_event_list_get**](Webhook.md#webhook_event_list_get) | **GET** /merchant/webhook/event_list | Webhook Event list
[**webhook_new_endpoint_post**](Webhook.md#webhook_new_endpoint_post) | **POST** /merchant/webhook/new_endpoint | Merchant New Webhook Endpoint
[**webhook_update_endpoint_post**](Webhook.md#webhook_update_endpoint_post) | **POST** /merchant/webhook/update_endpoint | Merchant Update Webhook Endpoint


# **webhook_delete_endpoint_post**
> MerchantAuthSsoLoginOTPPost200Response webhook_delete_endpoint_post(unibee_api_merchant_webhook_delete_endpoint_req)

Merchant Delete Webhook Endpoint

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_webhook_delete_endpoint_req import UnibeeApiMerchantWebhookDeleteEndpointReq
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
    api_instance = openapi_client.Webhook(api_client)
    unibee_api_merchant_webhook_delete_endpoint_req = openapi_client.UnibeeApiMerchantWebhookDeleteEndpointReq() # UnibeeApiMerchantWebhookDeleteEndpointReq | 

    try:
        # Merchant Delete Webhook Endpoint
        api_response = api_instance.webhook_delete_endpoint_post(unibee_api_merchant_webhook_delete_endpoint_req)
        print("The response of Webhook->webhook_delete_endpoint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Webhook->webhook_delete_endpoint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_webhook_delete_endpoint_req** | [**UnibeeApiMerchantWebhookDeleteEndpointReq**](UnibeeApiMerchantWebhookDeleteEndpointReq.md)|  | 

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

# **webhook_endpoint_list_get**
> MerchantWebhookEndpointListGet200Response webhook_endpoint_list_get()

Merchant Webhook Endpoint list

### Example


```python
import openapi_client
from openapi_client.models.merchant_webhook_endpoint_list_get200_response import MerchantWebhookEndpointListGet200Response
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
    api_instance = openapi_client.Webhook(api_client)

    try:
        # Merchant Webhook Endpoint list
        api_response = api_instance.webhook_endpoint_list_get()
        print("The response of Webhook->webhook_endpoint_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Webhook->webhook_endpoint_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantWebhookEndpointListGet200Response**](MerchantWebhookEndpointListGet200Response.md)

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

# **webhook_endpoint_log_list_get**
> MerchantWebhookEndpointLogListGet200Response webhook_endpoint_log_list_get(endpoint_id, page=page, count=count)

Merchant Webhook Endpoint Log list

### Example


```python
import openapi_client
from openapi_client.models.merchant_webhook_endpoint_log_list_get200_response import MerchantWebhookEndpointLogListGet200Response
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
    api_instance = openapi_client.Webhook(api_client)
    endpoint_id = 56 # int | EndpointId
    page = 56 # int | Page, Start WIth 0 (optional)
    count = 56 # int | Count Of Page (optional)

    try:
        # Merchant Webhook Endpoint Log list
        api_response = api_instance.webhook_endpoint_log_list_get(endpoint_id, page=page, count=count)
        print("The response of Webhook->webhook_endpoint_log_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Webhook->webhook_endpoint_log_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **int**| EndpointId | 
 **page** | **int**| Page, Start WIth 0 | [optional] 
 **count** | **int**| Count Of Page | [optional] 

### Return type

[**MerchantWebhookEndpointLogListGet200Response**](MerchantWebhookEndpointLogListGet200Response.md)

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

# **webhook_event_list_get**
> MerchantWebhookEventListGet200Response webhook_event_list_get()

Webhook Event list

### Example


```python
import openapi_client
from openapi_client.models.merchant_webhook_event_list_get200_response import MerchantWebhookEventListGet200Response
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
    api_instance = openapi_client.Webhook(api_client)

    try:
        # Webhook Event list
        api_response = api_instance.webhook_event_list_get()
        print("The response of Webhook->webhook_event_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Webhook->webhook_event_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantWebhookEventListGet200Response**](MerchantWebhookEventListGet200Response.md)

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

# **webhook_new_endpoint_post**
> MerchantAuthSsoLoginOTPPost200Response webhook_new_endpoint_post(unibee_api_merchant_webhook_new_endpoint_req)

Merchant New Webhook Endpoint

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_webhook_new_endpoint_req import UnibeeApiMerchantWebhookNewEndpointReq
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
    api_instance = openapi_client.Webhook(api_client)
    unibee_api_merchant_webhook_new_endpoint_req = openapi_client.UnibeeApiMerchantWebhookNewEndpointReq() # UnibeeApiMerchantWebhookNewEndpointReq | 

    try:
        # Merchant New Webhook Endpoint
        api_response = api_instance.webhook_new_endpoint_post(unibee_api_merchant_webhook_new_endpoint_req)
        print("The response of Webhook->webhook_new_endpoint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Webhook->webhook_new_endpoint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_webhook_new_endpoint_req** | [**UnibeeApiMerchantWebhookNewEndpointReq**](UnibeeApiMerchantWebhookNewEndpointReq.md)|  | 

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

# **webhook_update_endpoint_post**
> MerchantAuthSsoLoginOTPPost200Response webhook_update_endpoint_post(unibee_api_merchant_webhook_update_endpoint_req)

Merchant Update Webhook Endpoint

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_webhook_update_endpoint_req import UnibeeApiMerchantWebhookUpdateEndpointReq
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
    api_instance = openapi_client.Webhook(api_client)
    unibee_api_merchant_webhook_update_endpoint_req = openapi_client.UnibeeApiMerchantWebhookUpdateEndpointReq() # UnibeeApiMerchantWebhookUpdateEndpointReq | 

    try:
        # Merchant Update Webhook Endpoint
        api_response = api_instance.webhook_update_endpoint_post(unibee_api_merchant_webhook_update_endpoint_req)
        print("The response of Webhook->webhook_update_endpoint_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Webhook->webhook_update_endpoint_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_webhook_update_endpoint_req** | [**UnibeeApiMerchantWebhookUpdateEndpointReq**](UnibeeApiMerchantWebhookUpdateEndpointReq.md)|  | 

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

