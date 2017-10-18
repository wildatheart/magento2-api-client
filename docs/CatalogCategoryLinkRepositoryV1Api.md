# swagger_client.CatalogCategoryLinkRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_category_link_repository_v1_delete_by_ids_delete**](CatalogCategoryLinkRepositoryV1Api.md#catalog_category_link_repository_v1_delete_by_ids_delete) | **DELETE** /V1/categories/{categoryId}/products/{sku} | 
[**catalog_category_link_repository_v1_save_post**](CatalogCategoryLinkRepositoryV1Api.md#catalog_category_link_repository_v1_save_post) | **POST** /V1/categories/{categoryId}/products | 
[**catalog_category_link_repository_v1_save_put**](CatalogCategoryLinkRepositoryV1Api.md#catalog_category_link_repository_v1_save_put) | **PUT** /V1/categories/{categoryId}/products | 


# **catalog_category_link_repository_v1_delete_by_ids_delete**
> bool catalog_category_link_repository_v1_delete_by_ids_delete(category_id, sku)



Remove the product assignment from the category by category id and sku

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryLinkRepositoryV1Api()
category_id = 'category_id_example' # str | 
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.catalog_category_link_repository_v1_delete_by_ids_delete(category_id, sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryLinkRepositoryV1Api->catalog_category_link_repository_v1_delete_by_ids_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **sku** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_category_link_repository_v1_save_post**
> bool catalog_category_link_repository_v1_save_post(category_id, body=body)



Assign a product to the required category

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryLinkRepositoryV1Api()
category_id = 'category_id_example' # str | 
body = swagger_client.Body50() # Body50 |  (optional)

try: 
    api_response = api_instance.catalog_category_link_repository_v1_save_post(category_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryLinkRepositoryV1Api->catalog_category_link_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **body** | [**Body50**](Body50.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_category_link_repository_v1_save_put**
> bool catalog_category_link_repository_v1_save_put(category_id, body=body)



Assign a product to the required category

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryLinkRepositoryV1Api()
category_id = 'category_id_example' # str | 
body = swagger_client.Body49() # Body49 |  (optional)

try: 
    api_response = api_instance.catalog_category_link_repository_v1_save_put(category_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryLinkRepositoryV1Api->catalog_category_link_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **str**|  | 
 **body** | [**Body49**](Body49.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

