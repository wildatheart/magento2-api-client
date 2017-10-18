# swagger_client.CatalogCategoryManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_category_management_v1_get_tree_get**](CatalogCategoryManagementV1Api.md#catalog_category_management_v1_get_tree_get) | **GET** /V1/categories | 
[**catalog_category_management_v1_move_put**](CatalogCategoryManagementV1Api.md#catalog_category_management_v1_move_put) | **PUT** /V1/categories/{categoryId}/move | 


# **catalog_category_management_v1_get_tree_get**
> CatalogDataCategoryTreeInterface catalog_category_management_v1_get_tree_get(root_category_id=root_category_id, depth=depth)



Retrieve list of categories

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryManagementV1Api()
root_category_id = 56 # int |  (optional)
depth = 56 # int |  (optional)

try: 
    api_response = api_instance.catalog_category_management_v1_get_tree_get(root_category_id=root_category_id, depth=depth)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryManagementV1Api->catalog_category_management_v1_get_tree_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **root_category_id** | **int**|  | [optional] 
 **depth** | **int**|  | [optional] 

### Return type

[**CatalogDataCategoryTreeInterface**](CatalogDataCategoryTreeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_category_management_v1_move_put**
> bool catalog_category_management_v1_move_put(category_id, body=body)



Move category

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryManagementV1Api()
category_id = 56 # int | 
body = swagger_client.Body44() # Body44 |  (optional)

try: 
    api_response = api_instance.catalog_category_management_v1_move_put(category_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryManagementV1Api->catalog_category_management_v1_move_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **body** | [**Body44**](Body44.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

