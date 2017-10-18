# swagger_client.CatalogCategoryRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_category_repository_v1_delete_by_identifier_delete**](CatalogCategoryRepositoryV1Api.md#catalog_category_repository_v1_delete_by_identifier_delete) | **DELETE** /V1/categories/{categoryId} | 
[**catalog_category_repository_v1_get_get**](CatalogCategoryRepositoryV1Api.md#catalog_category_repository_v1_get_get) | **GET** /V1/categories/{categoryId} | 
[**catalog_category_repository_v1_save_post**](CatalogCategoryRepositoryV1Api.md#catalog_category_repository_v1_save_post) | **POST** /V1/categories | 
[**catalog_category_repository_v1_save_put**](CatalogCategoryRepositoryV1Api.md#catalog_category_repository_v1_save_put) | **PUT** /V1/categories/{id} | 


# **catalog_category_repository_v1_delete_by_identifier_delete**
> bool catalog_category_repository_v1_delete_by_identifier_delete(category_id)



Delete category by identifier

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryRepositoryV1Api()
category_id = 56 # int | 

try: 
    api_response = api_instance.catalog_category_repository_v1_delete_by_identifier_delete(category_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryRepositoryV1Api->catalog_category_repository_v1_delete_by_identifier_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_category_repository_v1_get_get**
> CatalogDataCategoryInterface catalog_category_repository_v1_get_get(category_id, store_id=store_id)



Get info about category by category id

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryRepositoryV1Api()
category_id = 56 # int | 
store_id = 56 # int |  (optional)

try: 
    api_response = api_instance.catalog_category_repository_v1_get_get(category_id, store_id=store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryRepositoryV1Api->catalog_category_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category_id** | **int**|  | 
 **store_id** | **int**|  | [optional] 

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_category_repository_v1_save_post**
> CatalogDataCategoryInterface catalog_category_repository_v1_save_post(body=body)



Create category service

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryRepositoryV1Api()
body = swagger_client.Body42() # Body42 |  (optional)

try: 
    api_response = api_instance.catalog_category_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryRepositoryV1Api->catalog_category_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body42**](Body42.md)|  | [optional] 

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_category_repository_v1_save_put**
> CatalogDataCategoryInterface catalog_category_repository_v1_save_put(id, body=body)



Create category service

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCategoryRepositoryV1Api()
id = 'id_example' # str | 
body = swagger_client.Body43() # Body43 |  (optional)

try: 
    api_response = api_instance.catalog_category_repository_v1_save_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCategoryRepositoryV1Api->catalog_category_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body43**](Body43.md)|  | [optional] 

### Return type

[**CatalogDataCategoryInterface**](CatalogDataCategoryInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

