# swagger_client.BundleProductOptionTypeListV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_product_option_type_list_v1_get_items_get**](BundleProductOptionTypeListV1Api.md#bundle_product_option_type_list_v1_get_items_get) | **GET** /V1/bundle-products/options/types | 


# **bundle_product_option_type_list_v1_get_items_get**
> list[BundleDataOptionTypeInterface] bundle_product_option_type_list_v1_get_items_get()



Get all types for options for bundle products

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductOptionTypeListV1Api()

try: 
    api_response = api_instance.bundle_product_option_type_list_v1_get_items_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductOptionTypeListV1Api->bundle_product_option_type_list_v1_get_items_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BundleDataOptionTypeInterface]**](BundleDataOptionTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

