# swagger_client.QuotePaymentMethodManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_payment_method_management_v1_get_get**](QuotePaymentMethodManagementV1Api.md#quote_payment_method_management_v1_get_get) | **GET** /V1/carts/{cartId}/selected-payment-method | 
[**quote_payment_method_management_v1_get_get_0**](QuotePaymentMethodManagementV1Api.md#quote_payment_method_management_v1_get_get_0) | **GET** /V1/carts/mine/selected-payment-method | 
[**quote_payment_method_management_v1_get_list_get**](QuotePaymentMethodManagementV1Api.md#quote_payment_method_management_v1_get_list_get) | **GET** /V1/carts/{cartId}/payment-methods | 
[**quote_payment_method_management_v1_get_list_get_0**](QuotePaymentMethodManagementV1Api.md#quote_payment_method_management_v1_get_list_get_0) | **GET** /V1/carts/mine/payment-methods | 
[**quote_payment_method_management_v1_set_put**](QuotePaymentMethodManagementV1Api.md#quote_payment_method_management_v1_set_put) | **PUT** /V1/carts/{cartId}/selected-payment-method | 
[**quote_payment_method_management_v1_set_put_0**](QuotePaymentMethodManagementV1Api.md#quote_payment_method_management_v1_set_put_0) | **PUT** /V1/carts/mine/selected-payment-method | 


# **quote_payment_method_management_v1_get_get**
> QuoteDataPaymentInterface quote_payment_method_management_v1_get_get(cart_id)



Returns the payment method for a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotePaymentMethodManagementV1Api()
cart_id = 56 # int | The cart ID.

try: 
    api_response = api_instance.quote_payment_method_management_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotePaymentMethodManagementV1Api->quote_payment_method_management_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 

### Return type

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_payment_method_management_v1_get_get_0**
> QuoteDataPaymentInterface quote_payment_method_management_v1_get_get_0()



Returns the payment method for a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotePaymentMethodManagementV1Api()

try: 
    api_response = api_instance.quote_payment_method_management_v1_get_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotePaymentMethodManagementV1Api->quote_payment_method_management_v1_get_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_payment_method_management_v1_get_list_get**
> list[QuoteDataPaymentMethodInterface] quote_payment_method_management_v1_get_list_get(cart_id)



Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See http://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotePaymentMethodManagementV1Api()
cart_id = 56 # int | The cart ID.

try: 
    api_response = api_instance.quote_payment_method_management_v1_get_list_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotePaymentMethodManagementV1Api->quote_payment_method_management_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 

### Return type

[**list[QuoteDataPaymentMethodInterface]**](QuoteDataPaymentMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_payment_method_management_v1_get_list_get_0**
> list[QuoteDataPaymentMethodInterface] quote_payment_method_management_v1_get_list_get_0()



Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See http://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotePaymentMethodManagementV1Api()

try: 
    api_response = api_instance.quote_payment_method_management_v1_get_list_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotePaymentMethodManagementV1Api->quote_payment_method_management_v1_get_list_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QuoteDataPaymentMethodInterface]**](QuoteDataPaymentMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_payment_method_management_v1_set_put**
> str quote_payment_method_management_v1_set_put(cart_id, body=body)



Adds a specified payment method to a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotePaymentMethodManagementV1Api()
cart_id = 56 # int | The cart ID.
body = swagger_client.Body70() # Body70 |  (optional)

try: 
    api_response = api_instance.quote_payment_method_management_v1_set_put(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotePaymentMethodManagementV1Api->quote_payment_method_management_v1_set_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 
 **body** | [**Body70**](Body70.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_payment_method_management_v1_set_put_0**
> str quote_payment_method_management_v1_set_put_0(body=body)



Adds a specified payment method to a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuotePaymentMethodManagementV1Api()
body = swagger_client.Body71() # Body71 |  (optional)

try: 
    api_response = api_instance.quote_payment_method_management_v1_set_put_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuotePaymentMethodManagementV1Api->quote_payment_method_management_v1_set_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body71**](Body71.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

