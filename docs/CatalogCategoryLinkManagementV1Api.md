# swagger_client.CatalogCategoryLinkManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_category_link_management_v1_get_assigned_products_get**](CatalogCategoryLinkManagementV1Api.md#catalog_category_link_management_v1_get_assigned_products_get) | **GET** /V1/categories/{categoryId}/products | 


# **catalog_category_link_management_v1_get_assigned_products_get**
> list[CatalogDataCategoryProductLinkInterface] catalog_category_link_management_v1_get_assigned_products_get(category_id)



Get products assigned to category

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryLinkManagementV1Api()
category_id = 56 # int | 

try: 
    api_response = api_instance.catalog_category_link_management_v1_get_assigned_products_get(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryLinkManagementV1Api->catalog_category_link_management_v1_get_assigned_products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 

### Return type

[**list[CatalogDataCategoryProductLinkInterface]**](CatalogDataCategoryProductLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

