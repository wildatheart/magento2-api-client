# swagger_client.CatalogProductMediaAttributeManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_media_attribute_management_v1_get_list_get**](CatalogProductMediaAttributeManagementV1Api.md#catalog_product_media_attribute_management_v1_get_list_get) | **GET** /V1/products/media/types/{attributeSetName} | 


# **catalog_product_media_attribute_management_v1_get_list_get**
> list[CatalogDataProductAttributeInterface] catalog_product_media_attribute_management_v1_get_list_get(attribute_set_name)



Retrieve the list of media attributes (fronted input type is media_image) assigned to the given attribute set.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductMediaAttributeManagementV1Api()
attribute_set_name = 'attribute_set_name_example' # str | 

try: 
    api_response = api_instance.catalog_product_media_attribute_management_v1_get_list_get(attribute_set_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductMediaAttributeManagementV1Api->catalog_product_media_attribute_management_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_set_name** | **str**|  | 

### Return type

[**list[CatalogDataProductAttributeInterface]**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

