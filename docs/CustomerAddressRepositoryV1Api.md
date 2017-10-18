# swagger_client.CustomerAddressRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_address_repository_v1_delete_by_id_delete**](CustomerAddressRepositoryV1Api.md#customer_address_repository_v1_delete_by_id_delete) | **DELETE** /V1/addresses/{addressId} | 
[**customer_address_repository_v1_get_by_id_get**](CustomerAddressRepositoryV1Api.md#customer_address_repository_v1_get_by_id_get) | **GET** /V1/customers/addresses/{addressId} | 


# **customer_address_repository_v1_delete_by_id_delete**
> bool customer_address_repository_v1_delete_by_id_delete(address_id)



Delete customer address by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressRepositoryV1Api()
address_id = 56 # int | 

try: 
    api_response = api_instance.customer_address_repository_v1_delete_by_id_delete(address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressRepositoryV1Api->customer_address_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_address_repository_v1_get_by_id_get**
> CustomerDataAddressInterface customer_address_repository_v1_get_by_id_get(address_id)



Retrieve customer address.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressRepositoryV1Api()
address_id = 56 # int | 

try: 
    api_response = api_instance.customer_address_repository_v1_get_by_id_get(address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressRepositoryV1Api->customer_address_repository_v1_get_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_id** | **int**|  | 

### Return type

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

