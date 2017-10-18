# swagger_client.StoreStoreConfigManagerV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_store_config_manager_v1_get_store_configs_get**](StoreStoreConfigManagerV1Api.md#store_store_config_manager_v1_get_store_configs_get) | **GET** /V1/store/storeConfigs | 


# **store_store_config_manager_v1_get_store_configs_get**
> list[StoreDataStoreConfigInterface] store_store_config_manager_v1_get_store_configs_get(store_codes=store_codes)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreStoreConfigManagerV1Api()
store_codes = ['store_codes_example'] # list[str] |  (optional)

try: 
    api_response = api_instance.store_store_config_manager_v1_get_store_configs_get(store_codes=store_codes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreStoreConfigManagerV1Api->store_store_config_manager_v1_get_store_configs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_codes** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**list[StoreDataStoreConfigInterface]**](StoreDataStoreConfigInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

