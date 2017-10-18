# swagger_client.BundleProductOptionManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_product_option_management_v1_save_post**](BundleProductOptionManagementV1Api.md#bundle_product_option_management_v1_save_post) | **POST** /V1/bundle-products/options/add | 
[**bundle_product_option_management_v1_save_put**](BundleProductOptionManagementV1Api.md#bundle_product_option_management_v1_save_put) | **PUT** /V1/bundle-products/options/{optionId} | 


# **bundle_product_option_management_v1_save_post**
> int bundle_product_option_management_v1_save_post(body=body)



Add new option for bundle product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductOptionManagementV1Api()
body = swagger_client.Body81() # Body81 |  (optional)

try: 
    api_response = api_instance.bundle_product_option_management_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductOptionManagementV1Api->bundle_product_option_management_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body81**](Body81.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_product_option_management_v1_save_put**
> int bundle_product_option_management_v1_save_put(option_id, body=body)



Add new option for bundle product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductOptionManagementV1Api()
option_id = 'option_id_example' # str | 
body = swagger_client.Body82() # Body82 |  (optional)

try: 
    api_response = api_instance.bundle_product_option_management_v1_save_put(option_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductOptionManagementV1Api->bundle_product_option_management_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option_id** | **str**|  | 
 **body** | [**Body82**](Body82.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

