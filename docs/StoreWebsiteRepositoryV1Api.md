# swagger_client.StoreWebsiteRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**store_website_repository_v1_get_list_get**](StoreWebsiteRepositoryV1Api.md#store_website_repository_v1_get_list_get) | **GET** /V1/store/websites | 


# **store_website_repository_v1_get_list_get**
> list[StoreDataWebsiteInterface] store_website_repository_v1_get_list_get()



Retrieve list of all websites

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StoreWebsiteRepositoryV1Api()

try: 
    api_response = api_instance.store_website_repository_v1_get_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoreWebsiteRepositoryV1Api->store_website_repository_v1_get_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[StoreDataWebsiteInterface]**](StoreDataWebsiteInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

