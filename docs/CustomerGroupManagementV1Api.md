# swagger_client.CustomerGroupManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_group_management_v1_get_default_group_get**](CustomerGroupManagementV1Api.md#customer_group_management_v1_get_default_group_get) | **GET** /V1/customerGroups/default/{storeId} | 
[**customer_group_management_v1_get_default_group_get_0**](CustomerGroupManagementV1Api.md#customer_group_management_v1_get_default_group_get_0) | **GET** /V1/customerGroups/default | 
[**customer_group_management_v1_is_readonly_get**](CustomerGroupManagementV1Api.md#customer_group_management_v1_is_readonly_get) | **GET** /V1/customerGroups/{id}/permissions | 


# **customer_group_management_v1_get_default_group_get**
> CustomerDataGroupInterface customer_group_management_v1_get_default_group_get(store_id)



Get default customer group.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupManagementV1Api()
store_id = 56 # int | 

try: 
    api_response = api_instance.customer_group_management_v1_get_default_group_get(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupManagementV1Api->customer_group_management_v1_get_default_group_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **int**|  | 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_management_v1_get_default_group_get_0**
> CustomerDataGroupInterface customer_group_management_v1_get_default_group_get_0(store_id=store_id)



Get default customer group.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupManagementV1Api()
store_id = 56 # int |  (optional)

try: 
    api_response = api_instance.customer_group_management_v1_get_default_group_get_0(store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupManagementV1Api->customer_group_management_v1_get_default_group_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **int**|  | [optional] 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_management_v1_is_readonly_get**
> bool customer_group_management_v1_is_readonly_get(id)



Check if customer group can be deleted.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupManagementV1Api()
id = 56 # int | 

try: 
    api_response = api_instance.customer_group_management_v1_is_readonly_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupManagementV1Api->customer_group_management_v1_is_readonly_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

