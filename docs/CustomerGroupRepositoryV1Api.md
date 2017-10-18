# swagger_client.CustomerGroupRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_group_repository_v1_delete_by_id_delete**](CustomerGroupRepositoryV1Api.md#customer_group_repository_v1_delete_by_id_delete) | **DELETE** /V1/customerGroups/{id} | 
[**customer_group_repository_v1_get_by_id_get**](CustomerGroupRepositoryV1Api.md#customer_group_repository_v1_get_by_id_get) | **GET** /V1/customerGroups/{id} | 
[**customer_group_repository_v1_get_list_get**](CustomerGroupRepositoryV1Api.md#customer_group_repository_v1_get_list_get) | **GET** /V1/customerGroups/search | 
[**customer_group_repository_v1_save_post**](CustomerGroupRepositoryV1Api.md#customer_group_repository_v1_save_post) | **POST** /V1/customerGroups | 
[**customer_group_repository_v1_save_put**](CustomerGroupRepositoryV1Api.md#customer_group_repository_v1_save_put) | **PUT** /V1/customerGroups/{id} | 


# **customer_group_repository_v1_delete_by_id_delete**
> bool customer_group_repository_v1_delete_by_id_delete(id)



Delete customer group by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupRepositoryV1Api()
id = 56 # int | 

try: 
    api_response = api_instance.customer_group_repository_v1_delete_by_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupRepositoryV1Api->customer_group_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_repository_v1_get_by_id_get**
> CustomerDataGroupInterface customer_group_repository_v1_get_by_id_get(id)



Get customer group by group ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupRepositoryV1Api()
id = 56 # int | 

try: 
    api_response = api_instance.customer_group_repository_v1_get_by_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupRepositoryV1Api->customer_group_repository_v1_get_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_repository_v1_get_list_get**
> CustomerDataGroupSearchResultsInterface customer_group_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve customer groups. The list of groups can be filtered to exclude the NOT_LOGGED_IN group using the first parameter and/or it can be filtered by tax class. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See http://devdocs.magento.com/codelinks/attributes.html#GroupRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.customer_group_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupRepositoryV1Api->customer_group_repository_v1_get_list_get: %s\n" % e)
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

[**CustomerDataGroupSearchResultsInterface**](CustomerDataGroupSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_repository_v1_save_post**
> CustomerDataGroupInterface customer_group_repository_v1_save_post(body=body)



Save customer group.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupRepositoryV1Api()
body = swagger_client.Body3() # Body3 |  (optional)

try: 
    api_response = api_instance.customer_group_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupRepositoryV1Api->customer_group_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_group_repository_v1_save_put**
> CustomerDataGroupInterface customer_group_repository_v1_save_put(id, body=body)



Save customer group.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerGroupRepositoryV1Api()
id = 'id_example' # str | 
body = swagger_client.Body2() # Body2 |  (optional)

try: 
    api_response = api_instance.customer_group_repository_v1_save_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerGroupRepositoryV1Api->customer_group_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

