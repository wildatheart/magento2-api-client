# swagger_client.CatalogProductRenderListV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_render_list_v1_get_list_get**](CatalogProductRenderListV1Api.md#catalog_product_render_list_v1_get_list_get) | **GET** /V1/products-render-info | 


# **catalog_product_render_list_v1_get_list_get**
> CatalogDataProductRenderSearchResultsInterface catalog_product_render_list_v1_get_list_get(store_id, currency_code, search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Collect and retrieve the list of product render info This info contains raw prices and formated prices, product name, stock status, store_id, etc

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductRenderListV1Api()
store_id = 56 # int | 
currency_code = 'currency_code_example' # str | 
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.catalog_product_render_list_v1_get_list_get(store_id, currency_code, search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductRenderListV1Api->catalog_product_render_list_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **int**|  | 
 **currency_code** | **str**|  | 
 **search_criteria_filter_groups_filters_field** | **str**| Field | [optional] 
 **search_criteria_filter_groups_filters_value** | **str**| Value | [optional] 
 **search_criteria_filter_groups_filters_condition_type** | **str**| Condition type | [optional] 
 **search_criteria_sort_orders_field** | **str**| Sorting field. | [optional] 
 **search_criteria_sort_orders_direction** | **str**| Sorting direction. | [optional] 
 **search_criteria_page_size** | **int**| Page size. | [optional] 
 **search_criteria_current_page** | **int**| Current page. | [optional] 

### Return type

[**CatalogDataProductRenderSearchResultsInterface**](CatalogDataProductRenderSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

