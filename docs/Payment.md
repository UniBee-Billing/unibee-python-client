# openapi_client.Payment

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_cancel_post**](Payment.md#payment_cancel_post) | **POST** /merchant/payment/cancel | Cancel Payment
[**payment_capture_post**](Payment.md#payment_capture_post) | **POST** /merchant/payment/capture | Capture Payment
[**payment_detail_get**](Payment.md#payment_detail_get) | **GET** /merchant/payment/detail | Query Payment Detail
[**payment_list_get**](Payment.md#payment_list_get) | **GET** /merchant/payment/list | Query Payment List
[**payment_method_list_get**](Payment.md#payment_method_list_get) | **GET** /merchant/payment/method_list | Query Payment Method List
[**payment_new_post**](Payment.md#payment_new_post) | **POST** /merchant/payment/new | New Payment
[**payment_refund_cancel_post**](Payment.md#payment_refund_cancel_post) | **POST** /merchant/payment/refund/cancel | Cancel Payment Refund
[**payment_refund_detail_get**](Payment.md#payment_refund_detail_get) | **GET** /merchant/payment/refund/detail | Query Payment Refund Detail
[**payment_refund_list_get**](Payment.md#payment_refund_list_get) | **GET** /merchant/payment/refund/list | Query Payment Refund List
[**payment_refund_new_post**](Payment.md#payment_refund_new_post) | **POST** /merchant/payment/refund/new | New Payment Refund
[**payment_timeline_list_get**](Payment.md#payment_timeline_list_get) | **GET** /merchant/payment/timeline/list | Payment TimeLine List


# **payment_cancel_post**
> MerchantAuthSsoLoginOTPPost200Response payment_cancel_post(unibee_api_merchant_payment_cancel_req)

Cancel Payment

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_payment_cancel_req import UnibeeApiMerchantPaymentCancelReq
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
    api_instance = openapi_client.Payment(api_client)
    unibee_api_merchant_payment_cancel_req = openapi_client.UnibeeApiMerchantPaymentCancelReq() # UnibeeApiMerchantPaymentCancelReq | 

    try:
        # Cancel Payment
        api_response = api_instance.payment_cancel_post(unibee_api_merchant_payment_cancel_req)
        print("The response of Payment->payment_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_payment_cancel_req** | [**UnibeeApiMerchantPaymentCancelReq**](UnibeeApiMerchantPaymentCancelReq.md)|  | 

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

# **payment_capture_post**
> MerchantAuthSsoLoginOTPPost200Response payment_capture_post(unibee_api_merchant_payment_capture_req)

Capture Payment

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_payment_capture_req import UnibeeApiMerchantPaymentCaptureReq
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
    api_instance = openapi_client.Payment(api_client)
    unibee_api_merchant_payment_capture_req = openapi_client.UnibeeApiMerchantPaymentCaptureReq() # UnibeeApiMerchantPaymentCaptureReq | 

    try:
        # Capture Payment
        api_response = api_instance.payment_capture_post(unibee_api_merchant_payment_capture_req)
        print("The response of Payment->payment_capture_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_capture_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_payment_capture_req** | [**UnibeeApiMerchantPaymentCaptureReq**](UnibeeApiMerchantPaymentCaptureReq.md)|  | 

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

# **payment_detail_get**
> MerchantPaymentDetailGet200Response payment_detail_get(payment_id)

Query Payment Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_detail_get200_response import MerchantPaymentDetailGet200Response
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
    api_instance = openapi_client.Payment(api_client)
    payment_id = 'payment_id_example' # str | PaymentId

    try:
        # Query Payment Detail
        api_response = api_instance.payment_detail_get(payment_id)
        print("The response of Payment->payment_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| PaymentId | 

### Return type

[**MerchantPaymentDetailGet200Response**](MerchantPaymentDetailGet200Response.md)

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

# **payment_list_get**
> MerchantPaymentListGet200Response payment_list_get(gateway_id=gateway_id, user_id=user_id, email=email, status=status, currency=currency, country_code=country_code, sort_field=sort_field, sort_type=sort_type, page=page, count=count)

Query Payment List

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_list_get200_response import MerchantPaymentListGet200Response
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
    api_instance = openapi_client.Payment(api_client)
    gateway_id = 56 # int | GatewayId (optional)
    user_id = 56 # int | UserId  (optional)
    email = 'email_example' # str | Email (optional)
    status = 56 # int | Status, 10-Created|20-Success|30-Failed|40-Cancelled (optional)
    currency = 'currency_example' # str | Currency (optional)
    country_code = 'country_code_example' # str | CountryCode (optional)
    sort_field = 'sort_field_example' # str | Sort Field，user_id|create_time|status (optional)
    sort_type = 'sort_type_example' # str | Sort Type，asc|desc (optional)
    page = 56 # int | Page, Start With 0 (optional)
    count = 56 # int | Count Of Page (optional)

    try:
        # Query Payment List
        api_response = api_instance.payment_list_get(gateway_id=gateway_id, user_id=user_id, email=email, status=status, currency=currency, country_code=country_code, sort_field=sort_field, sort_type=sort_type, page=page, count=count)
        print("The response of Payment->payment_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| GatewayId | [optional] 
 **user_id** | **int**| UserId  | [optional] 
 **email** | **str**| Email | [optional] 
 **status** | **int**| Status, 10-Created|20-Success|30-Failed|40-Cancelled | [optional] 
 **currency** | **str**| Currency | [optional] 
 **country_code** | **str**| CountryCode | [optional] 
 **sort_field** | **str**| Sort Field，user_id|create_time|status | [optional] 
 **sort_type** | **str**| Sort Type，asc|desc | [optional] 
 **page** | **int**| Page, Start With 0 | [optional] 
 **count** | **int**| Count Of Page | [optional] 

### Return type

[**MerchantPaymentListGet200Response**](MerchantPaymentListGet200Response.md)

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

# **payment_method_list_get**
> MerchantPaymentMethodListGet200Response payment_method_list_get(gateway_id, user_id=user_id, payment_id=payment_id)

Query Payment Method List

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_method_list_get200_response import MerchantPaymentMethodListGet200Response
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
    api_instance = openapi_client.Payment(api_client)
    gateway_id = 56 # int | GatewayId
    user_id = 56 # int | UserId (optional)
    payment_id = 'payment_id_example' # str | PaymentId (optional)

    try:
        # Query Payment Method List
        api_response = api_instance.payment_method_list_get(gateway_id, user_id=user_id, payment_id=payment_id)
        print("The response of Payment->payment_method_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_method_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **int**| GatewayId | 
 **user_id** | **int**| UserId | [optional] 
 **payment_id** | **str**| PaymentId | [optional] 

### Return type

[**MerchantPaymentMethodListGet200Response**](MerchantPaymentMethodListGet200Response.md)

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

# **payment_new_post**
> MerchantPaymentNewPost200Response payment_new_post(unibee_api_merchant_payment_new_req)

New Payment

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_new_post200_response import MerchantPaymentNewPost200Response
from openapi_client.models.unibee_api_merchant_payment_new_req import UnibeeApiMerchantPaymentNewReq
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
    api_instance = openapi_client.Payment(api_client)
    unibee_api_merchant_payment_new_req = openapi_client.UnibeeApiMerchantPaymentNewReq() # UnibeeApiMerchantPaymentNewReq | 

    try:
        # New Payment
        api_response = api_instance.payment_new_post(unibee_api_merchant_payment_new_req)
        print("The response of Payment->payment_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_payment_new_req** | [**UnibeeApiMerchantPaymentNewReq**](UnibeeApiMerchantPaymentNewReq.md)|  | 

### Return type

[**MerchantPaymentNewPost200Response**](MerchantPaymentNewPost200Response.md)

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

# **payment_refund_cancel_post**
> MerchantAuthSsoLoginOTPPost200Response payment_refund_cancel_post(unibee_api_merchant_payment_refund_cancel_req)

Cancel Payment Refund

### Example


```python
import openapi_client
from openapi_client.models.merchant_auth_sso_login_otp_post200_response import MerchantAuthSsoLoginOTPPost200Response
from openapi_client.models.unibee_api_merchant_payment_refund_cancel_req import UnibeeApiMerchantPaymentRefundCancelReq
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
    api_instance = openapi_client.Payment(api_client)
    unibee_api_merchant_payment_refund_cancel_req = openapi_client.UnibeeApiMerchantPaymentRefundCancelReq() # UnibeeApiMerchantPaymentRefundCancelReq | 

    try:
        # Cancel Payment Refund
        api_response = api_instance.payment_refund_cancel_post(unibee_api_merchant_payment_refund_cancel_req)
        print("The response of Payment->payment_refund_cancel_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_refund_cancel_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_payment_refund_cancel_req** | [**UnibeeApiMerchantPaymentRefundCancelReq**](UnibeeApiMerchantPaymentRefundCancelReq.md)|  | 

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

# **payment_refund_detail_get**
> MerchantPaymentRefundDetailGet200Response payment_refund_detail_get(refund_id=refund_id)

Query Payment Refund Detail

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_refund_detail_get200_response import MerchantPaymentRefundDetailGet200Response
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
    api_instance = openapi_client.Payment(api_client)
    refund_id = 'refund_id_example' # str | RefundId (optional)

    try:
        # Query Payment Refund Detail
        api_response = api_instance.payment_refund_detail_get(refund_id=refund_id)
        print("The response of Payment->payment_refund_detail_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_refund_detail_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_id** | **str**| RefundId | [optional] 

### Return type

[**MerchantPaymentRefundDetailGet200Response**](MerchantPaymentRefundDetailGet200Response.md)

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

# **payment_refund_list_get**
> MerchantPaymentRefundListGet200Response payment_refund_list_get(payment_id, status=status, gateway_id=gateway_id, user_id=user_id, email=email, currency=currency)

Query Payment Refund List

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_refund_list_get200_response import MerchantPaymentRefundListGet200Response
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
    api_instance = openapi_client.Payment(api_client)
    payment_id = 'payment_id_example' # str | PaymentId
    status = 56 # int | Status,10-create|20-success|30-Failed|40-Reverse (optional)
    gateway_id = 56 # int | GatewayId (optional)
    user_id = 56 # int | UserId (optional)
    email = 'email_example' # str | Email (optional)
    currency = 'currency_example' # str | Currency (optional)

    try:
        # Query Payment Refund List
        api_response = api_instance.payment_refund_list_get(payment_id, status=status, gateway_id=gateway_id, user_id=user_id, email=email, currency=currency)
        print("The response of Payment->payment_refund_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_refund_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| PaymentId | 
 **status** | **int**| Status,10-create|20-success|30-Failed|40-Reverse | [optional] 
 **gateway_id** | **int**| GatewayId | [optional] 
 **user_id** | **int**| UserId | [optional] 
 **email** | **str**| Email | [optional] 
 **currency** | **str**| Currency | [optional] 

### Return type

[**MerchantPaymentRefundListGet200Response**](MerchantPaymentRefundListGet200Response.md)

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

# **payment_refund_new_post**
> MerchantPaymentRefundNewPost200Response payment_refund_new_post(unibee_api_merchant_payment_new_payment_refund_req)

New Payment Refund

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_refund_new_post200_response import MerchantPaymentRefundNewPost200Response
from openapi_client.models.unibee_api_merchant_payment_new_payment_refund_req import UnibeeApiMerchantPaymentNewPaymentRefundReq
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
    api_instance = openapi_client.Payment(api_client)
    unibee_api_merchant_payment_new_payment_refund_req = openapi_client.UnibeeApiMerchantPaymentNewPaymentRefundReq() # UnibeeApiMerchantPaymentNewPaymentRefundReq | 

    try:
        # New Payment Refund
        api_response = api_instance.payment_refund_new_post(unibee_api_merchant_payment_new_payment_refund_req)
        print("The response of Payment->payment_refund_new_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_refund_new_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unibee_api_merchant_payment_new_payment_refund_req** | [**UnibeeApiMerchantPaymentNewPaymentRefundReq**](UnibeeApiMerchantPaymentNewPaymentRefundReq.md)|  | 

### Return type

[**MerchantPaymentRefundNewPost200Response**](MerchantPaymentRefundNewPost200Response.md)

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

# **payment_timeline_list_get**
> MerchantPaymentTimelineListGet200Response payment_timeline_list_get(user_id=user_id, sort_field=sort_field, sort_type=sort_type, page=page, count=count)

Payment TimeLine List

### Example


```python
import openapi_client
from openapi_client.models.merchant_payment_timeline_list_get200_response import MerchantPaymentTimelineListGet200Response
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
    api_instance = openapi_client.Payment(api_client)
    user_id = 56 # int | Filter UserId, Default All (optional)
    sort_field = 'sort_field_example' # str | Sort，invoice_id|gmt_create|gmt_modify|period_end|total_amount，Default gmt_modify (optional)
    sort_type = 'sort_type_example' # str | Sort Type，asc|desc，Default desc (optional)
    page = 56 # int | Page,Start 0 (optional)
    count = 56 # int | Count Of Page (optional)

    try:
        # Payment TimeLine List
        api_response = api_instance.payment_timeline_list_get(user_id=user_id, sort_field=sort_field, sort_type=sort_type, page=page, count=count)
        print("The response of Payment->payment_timeline_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Payment->payment_timeline_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Filter UserId, Default All | [optional] 
 **sort_field** | **str**| Sort，invoice_id|gmt_create|gmt_modify|period_end|total_amount，Default gmt_modify | [optional] 
 **sort_type** | **str**| Sort Type，asc|desc，Default desc | [optional] 
 **page** | **int**| Page,Start 0 | [optional] 
 **count** | **int**| Count Of Page | [optional] 

### Return type

[**MerchantPaymentTimelineListGet200Response**](MerchantPaymentTimelineListGet200Response.md)

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

