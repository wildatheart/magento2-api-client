# swagger_client.CmsPageRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cms_page_repository_v1_delete_by_id_delete**](CmsPageRepositoryV1Api.md#cms_page_repository_v1_delete_by_id_delete) | **DELETE** /V1/cmsPage/{pageId} | 
[**cms_page_repository_v1_get_by_id_get**](CmsPageRepositoryV1Api.md#cms_page_repository_v1_get_by_id_get) | **GET** /V1/cmsPage/{pageId} | 
[**cms_page_repository_v1_get_list_get**](CmsPageRepositoryV1Api.md#cms_page_repository_v1_get_list_get) | **GET** /V1/cmsPage/search | 
[**cms_page_repository_v1_save_post**](CmsPageRepositoryV1Api.md#cms_page_repository_v1_save_post) | **POST** /V1/cmsPage | 
[**cms_page_repository_v1_save_put**](CmsPageRepositoryV1Api.md#cms_page_repository_v1_save_put) | **PUT** /V1/cmsPage/{id} | 


# **cms_page_repository_v1_delete_by_id_delete**
> bool cms_page_repository_v1_delete_by_id_delete(page_id)



Delete page by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsPageRepositoryV1Api()
page_id = 56 # int | 

try: 
    api_response = api_instance.cms_page_repository_v1_delete_by_id_delete(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsPageRepositoryV1Api->cms_page_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_page_repository_v1_get_by_id_get**
> CmsDataPageInterface cms_page_repository_v1_get_by_id_get(page_id)



Retrieve page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsPageRepositoryV1Api()
page_id = 56 # int | 

try: 
    api_response = api_instance.cms_page_repository_v1_get_by_id_get(page_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsPageRepositoryV1Api->cms_page_repository_v1_get_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **int**|  | 

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_page_repository_v1_get_list_get**
> CmsDataPageSearchResultsInterface cms_page_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve pages matching the specified criteria.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsPageRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.cms_page_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsPageRepositoryV1Api->cms_page_repository_v1_get_list_get: %s\n" % e)
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

[**CmsDataPageSearchResultsInterface**](CmsDataPageSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_page_repository_v1_save_post**
> CmsDataPageInterface cms_page_repository_v1_save_post(body=body)



Save page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsPageRepositoryV1Api()
body = swagger_client.Body14() # Body14 |  (optional)

try: 
    api_response = api_instance.cms_page_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsPageRepositoryV1Api->cms_page_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body14**](Body14.md)|  | [optional] 

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cms_page_repository_v1_save_put**
> CmsDataPageInterface cms_page_repository_v1_save_put(id, body=body)



Save page.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CmsPageRepositoryV1Api()
id = 'id_example' # str | 
body = swagger_client.Body15() # Body15 |  (optional)

try: 
    api_response = api_instance.cms_page_repository_v1_save_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CmsPageRepositoryV1Api->cms_page_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body15**](Body15.md)|  | [optional] 

### Return type

[**CmsDataPageInterface**](CmsDataPageInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

