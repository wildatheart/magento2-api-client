# swagger_client.CustomerCustomerGroupConfigV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_customer_group_config_v1_set_default_customer_group_put**](CustomerCustomerGroupConfigV1Api.md#customer_customer_group_config_v1_set_default_customer_group_put) | **PUT** /V1/customerGroups/default/{id} | 


# **customer_customer_group_config_v1_set_default_customer_group_put**
> int customer_customer_group_config_v1_set_default_customer_group_put(id)



Set system default customer group.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerCustomerGroupConfigV1Api()
id = 56 # int | 

try: 
    api_response = api_instance.customer_customer_group_config_v1_set_default_customer_group_put(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerCustomerGroupConfigV1Api->customer_customer_group_config_v1_set_default_customer_group_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

