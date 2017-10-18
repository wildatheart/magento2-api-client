# swagger_client.QuoteCartTotalManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_cart_total_management_v1_collect_totals_put**](QuoteCartTotalManagementV1Api.md#quote_cart_total_management_v1_collect_totals_put) | **PUT** /V1/carts/mine/collect-totals | 


# **quote_cart_total_management_v1_collect_totals_put**
> QuoteDataTotalsInterface quote_cart_total_management_v1_collect_totals_put(body=body)



Set shipping/billing methods and additional data for cart and collect totals.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartTotalManagementV1Api()
body = swagger_client.Body77() # Body77 |  (optional)

try: 
    api_response = api_instance.quote_cart_total_management_v1_collect_totals_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartTotalManagementV1Api->quote_cart_total_management_v1_collect_totals_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body77**](Body77.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

