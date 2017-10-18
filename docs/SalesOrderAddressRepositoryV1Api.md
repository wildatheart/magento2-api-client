# swagger_client.SalesOrderAddressRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_order_address_repository_v1_save_put**](SalesOrderAddressRepositoryV1Api.md#sales_order_address_repository_v1_save_put) | **PUT** /V1/orders/{parent_id} | 


# **sales_order_address_repository_v1_save_put**
> SalesDataOrderAddressInterface sales_order_address_repository_v1_save_put(parent_id, body=body)



Performs persist operations for a specified order address.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderAddressRepositoryV1Api()
parent_id = 'parent_id_example' # str | 
body = swagger_client.Body90() # Body90 |  (optional)

try: 
    api_response = api_instance.sales_order_address_repository_v1_save_put(parent_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderAddressRepositoryV1Api->sales_order_address_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_id** | **str**|  | 
 **body** | [**Body90**](Body90.md)|  | [optional] 

### Return type

[**SalesDataOrderAddressInterface**](SalesDataOrderAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

