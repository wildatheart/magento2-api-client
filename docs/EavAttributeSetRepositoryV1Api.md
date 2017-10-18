# swagger_client.EavAttributeSetRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eav_attribute_set_repository_v1_delete_by_id_delete**](EavAttributeSetRepositoryV1Api.md#eav_attribute_set_repository_v1_delete_by_id_delete) | **DELETE** /V1/eav/attribute-sets/{attributeSetId} | 
[**eav_attribute_set_repository_v1_get_get**](EavAttributeSetRepositoryV1Api.md#eav_attribute_set_repository_v1_get_get) | **GET** /V1/eav/attribute-sets/{attributeSetId} | 
[**eav_attribute_set_repository_v1_get_list_get**](EavAttributeSetRepositoryV1Api.md#eav_attribute_set_repository_v1_get_list_get) | **GET** /V1/eav/attribute-sets/list | 
[**eav_attribute_set_repository_v1_save_put**](EavAttributeSetRepositoryV1Api.md#eav_attribute_set_repository_v1_save_put) | **PUT** /V1/eav/attribute-sets/{attributeSetId} | 


# **eav_attribute_set_repository_v1_delete_by_id_delete**
> bool eav_attribute_set_repository_v1_delete_by_id_delete(attribute_set_id)



Remove attribute set by given ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EavAttributeSetRepositoryV1Api()
attribute_set_id = 56 # int | 

try: 
    api_response = api_instance.eav_attribute_set_repository_v1_delete_by_id_delete(attribute_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EavAttributeSetRepositoryV1Api->eav_attribute_set_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_set_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eav_attribute_set_repository_v1_get_get**
> EavDataAttributeSetInterface eav_attribute_set_repository_v1_get_get(attribute_set_id)



Retrieve attribute set information based on given ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EavAttributeSetRepositoryV1Api()
attribute_set_id = 56 # int | 

try: 
    api_response = api_instance.eav_attribute_set_repository_v1_get_get(attribute_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EavAttributeSetRepositoryV1Api->eav_attribute_set_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_set_id** | **int**|  | 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eav_attribute_set_repository_v1_get_list_get**
> EavDataAttributeSetSearchResultsInterface eav_attribute_set_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve list of Attribute Sets This call returns an array of objects, but detailed information about each object’s attributes might not be included. See http://devdocs.magento.com/codelinks/attributes.html#AttributeSetRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EavAttributeSetRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.eav_attribute_set_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EavAttributeSetRepositoryV1Api->eav_attribute_set_repository_v1_get_list_get: %s\n" % e)
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

[**EavDataAttributeSetSearchResultsInterface**](EavDataAttributeSetSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **eav_attribute_set_repository_v1_save_put**
> EavDataAttributeSetInterface eav_attribute_set_repository_v1_save_put(attribute_set_id, body=body)



Save attribute set data

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EavAttributeSetRepositoryV1Api()
attribute_set_id = 'attribute_set_id_example' # str | 
body = swagger_client.Body() # Body |  (optional)

try: 
    api_response = api_instance.eav_attribute_set_repository_v1_save_put(attribute_set_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EavAttributeSetRepositoryV1Api->eav_attribute_set_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_set_id** | **str**|  | 
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

