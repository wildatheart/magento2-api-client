# swagger_client.QuoteGuestShippingMethodManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_shipping_method_management_v1_get_list_get**](QuoteGuestShippingMethodManagementV1Api.md#quote_guest_shipping_method_management_v1_get_list_get) | **GET** /V1/guest-carts/{cartId}/shipping-methods | 


# **quote_guest_shipping_method_management_v1_get_list_get**
> list[QuoteDataShippingMethodInterface] quote_guest_shipping_method_management_v1_get_list_get(cart_id)



List applicable shipping methods for a specified quote.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestShippingMethodManagementV1Api()
cart_id = 'cart_id_example' # str | The shopping cart ID.

try: 
    api_response = api_instance.quote_guest_shipping_method_management_v1_get_list_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestShippingMethodManagementV1Api->quote_guest_shipping_method_management_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The shopping cart ID. | 

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

