# swagger_client.CmsBlockRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cms_block_repository_v1_delete_by_id_delete**](CmsBlockRepositoryV1Api.md#cms_block_repository_v1_delete_by_id_delete) | **DELETE** /V1/cmsBlock/{blockId} | 
[**cms_block_repository_v1_get_by_id_get**](CmsBlockRepositoryV1Api.md#cms_block_repository_v1_get_by_id_get) | **GET** /V1/cmsBlock/{blockId} | 
[**cms_block_repository_v1_get_list_get**](CmsBlockRepositoryV1Api.md#cms_block_repository_v1_get_list_get) | **GET** /V1/cmsBlock/search | 
[**cms_block_repository_v1_save_post**](CmsBlockRepositoryV1Api.md#cms_block_repository_v1_save_post) | **POST** /V1/cmsBlock | 
[**cms_block_repository_v1_save_put**](CmsBlockRepositoryV1Api.md#cms_block_repository_v1_save_put) | **PUT** /V1/cmsBlock/{id} | 


# **cms_block_repository_v1_delete_by_id_delete**
> bool cms_block_repository_v1_delete_by_id_delete(block_id)



Delete block by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsBlockRepositoryV1Api()
block_id = 56 # int | 

try: 
    api_response = api_instance.cms_block_repository_v1_delete_by_id_delete(block_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsBlockRepositoryV1Api->cms_block_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_block_repository_v1_get_by_id_get**
> CmsDataBlockInterface cms_block_repository_v1_get_by_id_get(block_id)



Retrieve block.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsBlockRepositoryV1Api()
block_id = 56 # int | 

try: 
    api_response = api_instance.cms_block_repository_v1_get_by_id_get(block_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsBlockRepositoryV1Api->cms_block_repository_v1_get_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_id** | **int**|  | 

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_block_repository_v1_get_list_get**
> CmsDataBlockSearchResultsInterface cms_block_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve blocks matching the specified criteria.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsBlockRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.cms_block_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsBlockRepositoryV1Api->cms_block_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_criteria_filter_groups_filters_field** | **str**| Field | [optional] 
 **search_criteria_filter_groups_filters_value** | **str**| Value | [optional] 
 **search_criteria_filter_groups_filters_condition_type** | **str**| Condition type | [optional] 
 **search_criteria_sort_orders_field** | **str**| Sorting field. | [optional] 
 **search_criteria_sort_orders_direction** | **str**| Sorting direction. | [optional] 
 **search_criteria_page_size** | **int**| Page size. | [optional] 
 **search_criteria_current_page** | **int**| Current page. | [optional] 

### Return type

[**CmsDataBlockSearchResultsInterface**](CmsDataBlockSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_block_repository_v1_save_post**
> CmsDataBlockInterface cms_block_repository_v1_save_post(body=body)



Save block.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsBlockRepositoryV1Api()
body = swagger_client.Body16() # Body16 |  (optional)

try: 
    api_response = api_instance.cms_block_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsBlockRepositoryV1Api->cms_block_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)|  | [optional] 

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_block_repository_v1_save_put**
> CmsDataBlockInterface cms_block_repository_v1_save_put(id, body=body)



Save block.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsBlockRepositoryV1Api()
id = 'id_example' # str | 
body = swagger_client.Body17() # Body17 |  (optional)

try: 
    api_response = api_instance.cms_block_repository_v1_save_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsBlockRepositoryV1Api->cms_block_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body17**](Body17.md)|  | [optional] 

### Return type

[**CmsDataBlockInterface**](CmsDataBlockInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

