# swagger_client.CatalogProductCustomOptionTypeListV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_custom_option_type_list_v1_get_items_get**](CatalogProductCustomOptionTypeListV1Api.md#catalog_product_custom_option_type_list_v1_get_items_get) | **GET** /V1/products/options/types | 


# **catalog_product_custom_option_type_list_v1_get_items_get**
> list[CatalogDataProductCustomOptionTypeInterface] catalog_product_custom_option_type_list_v1_get_items_get()



Get custom option types

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductCustomOptionTypeListV1Api()

try: 
    api_response = api_instance.catalog_product_custom_option_type_list_v1_get_items_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductCustomOptionTypeListV1Api->catalog_product_custom_option_type_list_v1_get_items_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CatalogDataProductCustomOptionTypeInterface]**](CatalogDataProductCustomOptionTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

