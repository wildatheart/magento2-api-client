# swagger_client.QuoteCartTotalRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_cart_total_repository_v1_get_get**](QuoteCartTotalRepositoryV1Api.md#quote_cart_total_repository_v1_get_get) | **GET** /V1/carts/{cartId}/totals | 
[**quote_cart_total_repository_v1_get_get_0**](QuoteCartTotalRepositoryV1Api.md#quote_cart_total_repository_v1_get_get_0) | **GET** /V1/carts/mine/totals | 


# **quote_cart_total_repository_v1_get_get**
> QuoteDataTotalsInterface quote_cart_total_repository_v1_get_get(cart_id)



Returns quote totals data for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartTotalRepositoryV1Api()
cart_id = 56 # int | The cart ID.

try: 
    api_response = api_instance.quote_cart_total_repository_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartTotalRepositoryV1Api->quote_cart_total_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_total_repository_v1_get_get_0**
> QuoteDataTotalsInterface quote_cart_total_repository_v1_get_get_0()



Returns quote totals data for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartTotalRepositoryV1Api()

try: 
    api_response = api_instance.quote_cart_total_repository_v1_get_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartTotalRepositoryV1Api->quote_cart_total_repository_v1_get_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

