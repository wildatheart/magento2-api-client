# swagger_client.QuoteGuestCartTotalManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_cart_total_management_v1_collect_totals_put**](QuoteGuestCartTotalManagementV1Api.md#quote_guest_cart_total_management_v1_collect_totals_put) | **PUT** /V1/guest-carts/{cartId}/collect-totals | 


# **quote_guest_cart_total_management_v1_collect_totals_put**
> QuoteDataTotalsInterface quote_guest_cart_total_management_v1_collect_totals_put(cart_id, body=body)



Set shipping/billing methods and additional data for cart and collect totals for guest.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartTotalManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
body = swagger_client.Body76() # Body76 |  (optional)

try: 
    api_response = api_instance.quote_guest_cart_total_management_v1_collect_totals_put(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartTotalManagementV1Api->quote_guest_cart_total_management_v1_collect_totals_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **body** | [**Body76**](Body76.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

