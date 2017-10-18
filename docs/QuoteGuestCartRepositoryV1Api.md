# swagger_client.QuoteGuestCartRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_cart_repository_v1_get_get**](QuoteGuestCartRepositoryV1Api.md#quote_guest_cart_repository_v1_get_get) | **GET** /V1/guest-carts/{cartId} | 


# **quote_guest_cart_repository_v1_get_get**
> QuoteDataCartInterface quote_guest_cart_repository_v1_get_get(cart_id)



Enable a guest user to return information for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartRepositoryV1Api()
cart_id = 'cart_id_example' # str | 

try: 
    api_response = api_instance.quote_guest_cart_repository_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartRepositoryV1Api->quote_guest_cart_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 

### Return type

[**QuoteDataCartInterface**](QuoteDataCartInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

