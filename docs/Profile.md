# openapi_client.Profile

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**country_config_list_post**](Profile.md#country_config_list_post) | **POST** /merchant/country_config_list | Merchant Edit Country Config
[**edit_country_config_post**](Profile.md#edit_country_config_post) | **POST** /merchant/edit_country_config | Merchant Country Config List
[**get_get**](Profile.md#get_get) | **GET** /merchant/get | Get Merchant Info
[**update_post**](Profile.md#update_post) | **POST** /merchant/update | Update Merchant Info


# **country_config_list_post**
> MerchantCountryConfigListPost200Response country_config_list_post(body)

Merchant Edit Country Config

### Example


```python
import openapi_client
from openapi_client.models.merchant_country_config_list_post200_response import MerchantCountryConfigListPost200Response
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
    api_instance = openapi_client.Profile(api_client)
    body = None # object | 

    try:
        # Merchant Edit Country Config
        api_response = api_instance.country_config_list_post(body)
        print("The response of Profile->country_config_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Profile->country_config_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

### Return type

[**MerchantCountryConfigListPost200Response**](MerchantCountryConfigListPost200Response.md)

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

# **edit_country_config_post**
> MerchantAuthSsoLoginOTPPost200Response edit_country_config_post(unibee_api_merchant_profile_edit_country_config_req)

Merchant Country Config List

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_profile_edit_country_config_req import UnibeeApiMerchantProfileEditCountryConfigReq
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
    api_instance = openapi_client.Profile(api_client)
    unibee_api_merchant_profile_edit_country_config_req = openapi_client.UnibeeApiMerchantProfileEditCountryConfigReq() # UnibeeApiMerchantProfileEditCountryConfigReq | 

    try:
        # Merchant Country Config List
        api_response = api_instance.edit_country_config_post(unibee_api_merchant_profile_edit_country_config_req)
        print("The response of Profile->edit_country_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Profile->edit_country_config_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_profile_edit_country_config_req** | [**UnibeeApiMerchantProfileEditCountryConfigReq**](UnibeeApiMerchantProfileEditCountryConfigReq.md)|  | 

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

# **get_get**
> MerchantGetGet200Response get_get()

Get Merchant Info

### Example


```python
import openapi_client
from openapi_client.models.merchant_get_get200_response import MerchantGetGet200Response
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
    api_instance = openapi_client.Profile(api_client)

    try:
        # Get Merchant Info
        api_response = api_instance.get_get()
        print("The response of Profile->get_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Profile->get_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**MerchantGetGet200Response**](MerchantGetGet200Response.md)

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

# **update_post**
> MerchantUpdatePost200Response update_post(unibee_api_merchant_profile_update_req)

Update Merchant Info

### Example


```python
import openapi_client
from openapi_client.models.merchant_update_post200_response import MerchantUpdatePost200Response
from openapi_client.models.unibee_api_merchant_profile_update_req import UnibeeApiMerchantProfileUpdateReq
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
    api_instance = openapi_client.Profile(api_client)
    unibee_api_merchant_profile_update_req = openapi_client.UnibeeApiMerchantProfileUpdateReq() # UnibeeApiMerchantProfileUpdateReq | 

    try:
        # Update Merchant Info
        api_response = api_instance.update_post(unibee_api_merchant_profile_update_req)
        print("The response of Profile->update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Profile->update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_profile_update_req** | [**UnibeeApiMerchantProfileUpdateReq**](UnibeeApiMerchantProfileUpdateReq.md)|  | 

### Return type

[**MerchantUpdatePost200Response**](MerchantUpdatePost200Response.md)

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

