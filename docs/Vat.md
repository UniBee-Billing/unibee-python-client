# openapi_client.Vat

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vat_country_list_get**](Vat.md#vat_country_list_get) | **GET** /merchant/vat/country_list | Vat Country List
[**vat_country_list_post**](Vat.md#vat_country_list_post) | **POST** /merchant/vat/country_list | Vat Country List
[**vat_setup_gateway_post**](Vat.md#vat_setup_gateway_post) | **POST** /merchant/vat/setup_gateway | Vat Gateway Setup


# **vat_country_list_get**
> MerchantVatCountryListGet200Response vat_country_list_get(merchant_id)

Vat Country List

### Example


```python
import openapi_client
from openapi_client.models.merchant_vat_country_list_get200_response import MerchantVatCountryListGet200Response
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
    api_instance = openapi_client.Vat(api_client)
    merchant_id = 56 # int | MerchantId

    try:
        # Vat Country List
        api_response = api_instance.vat_country_list_get(merchant_id)
        print("The response of Vat->vat_country_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Vat->vat_country_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merchant_id** | **int**| MerchantId | 

### Return type

[**MerchantVatCountryListGet200Response**](MerchantVatCountryListGet200Response.md)

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

# **vat_country_list_post**
> MerchantVatCountryListGet200Response vat_country_list_post(unibee_api_merchant_vat_country_list_req)

Vat Country List

### Example


```python
import openapi_client
from openapi_client.models.merchant_vat_country_list_get200_response import MerchantVatCountryListGet200Response
from openapi_client.models.unibee_api_merchant_vat_country_list_req import UnibeeApiMerchantVatCountryListReq
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
    api_instance = openapi_client.Vat(api_client)
    unibee_api_merchant_vat_country_list_req = openapi_client.UnibeeApiMerchantVatCountryListReq() # UnibeeApiMerchantVatCountryListReq | 

    try:
        # Vat Country List
        api_response = api_instance.vat_country_list_post(unibee_api_merchant_vat_country_list_req)
        print("The response of Vat->vat_country_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Vat->vat_country_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_vat_country_list_req** | [**UnibeeApiMerchantVatCountryListReq**](UnibeeApiMerchantVatCountryListReq.md)|  | 

### Return type

[**MerchantVatCountryListGet200Response**](MerchantVatCountryListGet200Response.md)

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

# **vat_setup_gateway_post**
> MerchantAuthSsoLoginOTPPost200Response vat_setup_gateway_post(unibee_api_merchant_vat_setup_gateway_req)

Vat Gateway Setup

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_vat_setup_gateway_req import UnibeeApiMerchantVatSetupGatewayReq
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
    api_instance = openapi_client.Vat(api_client)
    unibee_api_merchant_vat_setup_gateway_req = openapi_client.UnibeeApiMerchantVatSetupGatewayReq() # UnibeeApiMerchantVatSetupGatewayReq | 

    try:
        # Vat Gateway Setup
        api_response = api_instance.vat_setup_gateway_post(unibee_api_merchant_vat_setup_gateway_req)
        print("The response of Vat->vat_setup_gateway_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Vat->vat_setup_gateway_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_vat_setup_gateway_req** | [**UnibeeApiMerchantVatSetupGatewayReq**](UnibeeApiMerchantVatSetupGatewayReq.md)|  | 

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

