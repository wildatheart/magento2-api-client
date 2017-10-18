# swagger_client.QuoteGuestPaymentMethodManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_payment_method_management_v1_get_get**](QuoteGuestPaymentMethodManagementV1Api.md#quote_guest_payment_method_management_v1_get_get) | **GET** /V1/guest-carts/{cartId}/selected-payment-method | 
[**quote_guest_payment_method_management_v1_get_list_get**](QuoteGuestPaymentMethodManagementV1Api.md#quote_guest_payment_method_management_v1_get_list_get) | **GET** /V1/guest-carts/{cartId}/payment-methods | 
[**quote_guest_payment_method_management_v1_set_put**](QuoteGuestPaymentMethodManagementV1Api.md#quote_guest_payment_method_management_v1_set_put) | **PUT** /V1/guest-carts/{cartId}/selected-payment-method | 


# **quote_guest_payment_method_management_v1_get_get**
> QuoteDataPaymentInterface quote_guest_payment_method_management_v1_get_get(cart_id)



Return the payment method for a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestPaymentMethodManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.

try: 
    api_response = api_instance.quote_guest_payment_method_management_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestPaymentMethodManagementV1Api->quote_guest_payment_method_management_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 

### Return type

[**QuoteDataPaymentInterface**](QuoteDataPaymentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_payment_method_management_v1_get_list_get**
> list[QuoteDataPaymentMethodInterface] quote_guest_payment_method_management_v1_get_list_get(cart_id)



List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See http://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestPaymentMethodManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.

try: 
    api_response = api_instance.quote_guest_payment_method_management_v1_get_list_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestPaymentMethodManagementV1Api->quote_guest_payment_method_management_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 

### Return type

[**list[QuoteDataPaymentMethodInterface]**](QuoteDataPaymentMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_payment_method_management_v1_set_put**
> int quote_guest_payment_method_management_v1_set_put(cart_id, body=body)



Add a specified payment method to a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestPaymentMethodManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
body = swagger_client.Body72() # Body72 |  (optional)

try: 
    api_response = api_instance.quote_guest_payment_method_management_v1_set_put(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestPaymentMethodManagementV1Api->quote_guest_payment_method_management_v1_set_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **body** | [**Body72**](Body72.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

