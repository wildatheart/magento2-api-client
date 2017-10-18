# swagger_client.CatalogProductAttributeRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_attribute_repository_v1_delete_by_id_delete**](CatalogProductAttributeRepositoryV1Api.md#catalog_product_attribute_repository_v1_delete_by_id_delete) | **DELETE** /V1/products/attributes/{attributeCode} | 
[**catalog_product_attribute_repository_v1_get_get**](CatalogProductAttributeRepositoryV1Api.md#catalog_product_attribute_repository_v1_get_get) | **GET** /V1/products/attributes/{attributeCode} | 
[**catalog_product_attribute_repository_v1_get_list_get**](CatalogProductAttributeRepositoryV1Api.md#catalog_product_attribute_repository_v1_get_list_get) | **GET** /V1/products/attributes | 
[**catalog_product_attribute_repository_v1_save_post**](CatalogProductAttributeRepositoryV1Api.md#catalog_product_attribute_repository_v1_save_post) | **POST** /V1/products/attributes | 
[**catalog_product_attribute_repository_v1_save_put**](CatalogProductAttributeRepositoryV1Api.md#catalog_product_attribute_repository_v1_save_put) | **PUT** /V1/products/attributes/{attributeCode} | 


# **catalog_product_attribute_repository_v1_delete_by_id_delete**
> bool catalog_product_attribute_repository_v1_delete_by_id_delete(attribute_code)



Delete Attribute by id

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeRepositoryV1Api()
attribute_code = 'attribute_code_example' # str | 

try: 
    api_response = api_instance.catalog_product_attribute_repository_v1_delete_by_id_delete(attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeRepositoryV1Api->catalog_product_attribute_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_repository_v1_get_get**
> CatalogDataProductAttributeInterface catalog_product_attribute_repository_v1_get_get(attribute_code)



Retrieve specific attribute

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeRepositoryV1Api()
attribute_code = 'attribute_code_example' # str | 

try: 
    api_response = api_instance.catalog_product_attribute_repository_v1_get_get(attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeRepositoryV1Api->catalog_product_attribute_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_repository_v1_get_list_get**
> CatalogDataProductAttributeSearchResultsInterface catalog_product_attribute_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve all attributes for entity type

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.catalog_product_attribute_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeRepositoryV1Api->catalog_product_attribute_repository_v1_get_list_get: %s\n" % e)
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

[**CatalogDataProductAttributeSearchResultsInterface**](CatalogDataProductAttributeSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_repository_v1_save_post**
> CatalogDataProductAttributeInterface catalog_product_attribute_repository_v1_save_post(body=body)



Save attribute data

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeRepositoryV1Api()
body = swagger_client.Body21() # Body21 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeRepositoryV1Api->catalog_product_attribute_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body21**](Body21.md)|  | [optional] 

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_repository_v1_save_put**
> CatalogDataProductAttributeInterface catalog_product_attribute_repository_v1_save_put(attribute_code, body=body)



Save attribute data

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeRepositoryV1Api()
attribute_code = 'attribute_code_example' # str | 
body = swagger_client.Body20() # Body20 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_repository_v1_save_put(attribute_code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeRepositoryV1Api->catalog_product_attribute_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 
 **body** | [**Body20**](Body20.md)|  | [optional] 

### Return type

[**CatalogDataProductAttributeInterface**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

