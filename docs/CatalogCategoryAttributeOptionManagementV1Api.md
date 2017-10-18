# swagger_client.CatalogCategoryAttributeOptionManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_category_attribute_option_management_v1_get_items_get**](CatalogCategoryAttributeOptionManagementV1Api.md#catalog_category_attribute_option_management_v1_get_items_get) | **GET** /V1/categories/attributes/{attributeCode}/options | 


# **catalog_category_attribute_option_management_v1_get_items_get**
> list[EavDataAttributeOptionInterface] catalog_category_attribute_option_management_v1_get_items_get(attribute_code)



Retrieve list of attribute options

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryAttributeOptionManagementV1Api()
attribute_code = 'attribute_code_example' # str | 

try: 
    api_response = api_instance.catalog_category_attribute_option_management_v1_get_items_get(attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryAttributeOptionManagementV1Api->catalog_category_attribute_option_management_v1_get_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 

### Return type

[**list[EavDataAttributeOptionInterface]**](EavDataAttributeOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

