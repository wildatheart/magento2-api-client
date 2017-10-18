# swagger_client.CatalogProductAttributeTypesListV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_attribute_types_list_v1_get_items_get**](CatalogProductAttributeTypesListV1Api.md#catalog_product_attribute_types_list_v1_get_items_get) | **GET** /V1/products/attributes/types | 


# **catalog_product_attribute_types_list_v1_get_items_get**
> list[CatalogDataProductAttributeTypeInterface] catalog_product_attribute_types_list_v1_get_items_get()



Retrieve list of product attribute types

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeTypesListV1Api()

try: 
    api_response = api_instance.catalog_product_attribute_types_list_v1_get_items_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeTypesListV1Api->catalog_product_attribute_types_list_v1_get_items_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CatalogDataProductAttributeTypeInterface]**](CatalogDataProductAttributeTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

