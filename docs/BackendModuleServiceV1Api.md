# swagger_client.BackendModuleServiceV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backend_module_service_v1_get_modules_get**](BackendModuleServiceV1Api.md#backend_module_service_v1_get_modules_get) | **GET** /V1/modules | 


# **backend_module_service_v1_get_modules_get**
> list[str] backend_module_service_v1_get_modules_get()



Returns an array of enabled modules

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BackendModuleServiceV1Api()

try: 
    api_response = api_instance.backend_module_service_v1_get_modules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BackendModuleServiceV1Api->backend_module_service_v1_get_modules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

