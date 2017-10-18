# swagger_client.CatalogProductAttributeGroupRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_attribute_group_repository_v1_delete_by_id_delete**](CatalogProductAttributeGroupRepositoryV1Api.md#catalog_product_attribute_group_repository_v1_delete_by_id_delete) | **DELETE** /V1/products/attribute-sets/groups/{groupId} | 
[**catalog_product_attribute_group_repository_v1_get_list_get**](CatalogProductAttributeGroupRepositoryV1Api.md#catalog_product_attribute_group_repository_v1_get_list_get) | **GET** /V1/products/attribute-sets/groups/list | 
[**catalog_product_attribute_group_repository_v1_save_post**](CatalogProductAttributeGroupRepositoryV1Api.md#catalog_product_attribute_group_repository_v1_save_post) | **POST** /V1/products/attribute-sets/groups | 
[**catalog_product_attribute_group_repository_v1_save_put**](CatalogProductAttributeGroupRepositoryV1Api.md#catalog_product_attribute_group_repository_v1_save_put) | **PUT** /V1/products/attribute-sets/{attributeSetId}/groups | 


# **catalog_product_attribute_group_repository_v1_delete_by_id_delete**
> bool catalog_product_attribute_group_repository_v1_delete_by_id_delete(group_id)



Remove attribute group by id

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeGroupRepositoryV1Api()
group_id = 56 # int | 

try: 
    api_response = api_instance.catalog_product_attribute_group_repository_v1_delete_by_id_delete(group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeGroupRepositoryV1Api->catalog_product_attribute_group_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_group_repository_v1_get_list_get**
> EavDataAttributeGroupSearchResultsInterface catalog_product_attribute_group_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve list of attribute groups

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeGroupRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.catalog_product_attribute_group_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeGroupRepositoryV1Api->catalog_product_attribute_group_repository_v1_get_list_get: %s\n" % e)
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

[**EavDataAttributeGroupSearchResultsInterface**](EavDataAttributeGroupSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_group_repository_v1_save_post**
> EavDataAttributeGroupInterface catalog_product_attribute_group_repository_v1_save_post(body=body)



Save attribute group

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeGroupRepositoryV1Api()
body = swagger_client.Body25() # Body25 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_group_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeGroupRepositoryV1Api->catalog_product_attribute_group_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body25**](Body25.md)|  | [optional] 

### Return type

[**EavDataAttributeGroupInterface**](EavDataAttributeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_group_repository_v1_save_put**
> EavDataAttributeGroupInterface catalog_product_attribute_group_repository_v1_save_put(attribute_set_id, body=body)



Save attribute group

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeGroupRepositoryV1Api()
attribute_set_id = 'attribute_set_id_example' # str | 
body = swagger_client.Body26() # Body26 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_group_repository_v1_save_put(attribute_set_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeGroupRepositoryV1Api->catalog_product_attribute_group_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_set_id** | **str**|  | 
 **body** | [**Body26**](Body26.md)|  | [optional] 

### Return type

[**EavDataAttributeGroupInterface**](EavDataAttributeGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

