# swagger_client.CatalogProductRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_repository_v1_delete_by_id_delete**](CatalogProductRepositoryV1Api.md#catalog_product_repository_v1_delete_by_id_delete) | **DELETE** /V1/products/{sku} | 
[**catalog_product_repository_v1_get_get**](CatalogProductRepositoryV1Api.md#catalog_product_repository_v1_get_get) | **GET** /V1/products/{sku} | 
[**catalog_product_repository_v1_get_list_get**](CatalogProductRepositoryV1Api.md#catalog_product_repository_v1_get_list_get) | **GET** /V1/products | 
[**catalog_product_repository_v1_save_post**](CatalogProductRepositoryV1Api.md#catalog_product_repository_v1_save_post) | **POST** /V1/products | 
[**catalog_product_repository_v1_save_put**](CatalogProductRepositoryV1Api.md#catalog_product_repository_v1_save_put) | **PUT** /V1/products/{sku} | 


# **catalog_product_repository_v1_delete_by_id_delete**
> bool catalog_product_repository_v1_delete_by_id_delete(sku)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductRepositoryV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.catalog_product_repository_v1_delete_by_id_delete(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductRepositoryV1Api->catalog_product_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_repository_v1_get_get**
> CatalogDataProductInterface catalog_product_repository_v1_get_get(sku, edit_mode=edit_mode, store_id=store_id, force_reload=force_reload)



Get info about product by product SKU

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductRepositoryV1Api()
sku = 'sku_example' # str | 
edit_mode = true # bool |  (optional)
store_id = 56 # int |  (optional)
force_reload = true # bool |  (optional)

try: 
    api_response = api_instance.catalog_product_repository_v1_get_get(sku, edit_mode=edit_mode, store_id=store_id, force_reload=force_reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductRepositoryV1Api->catalog_product_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **edit_mode** | **bool**|  | [optional] 
 **store_id** | **int**|  | [optional] 
 **force_reload** | **bool**|  | [optional] 

### Return type

[**CatalogDataProductInterface**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_repository_v1_get_list_get**
> CatalogDataProductSearchResultsInterface catalog_product_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Get product list

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.catalog_product_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductRepositoryV1Api->catalog_product_repository_v1_get_list_get: %s\n" % e)
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

[**CatalogDataProductSearchResultsInterface**](CatalogDataProductSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_repository_v1_save_post**
> CatalogDataProductInterface catalog_product_repository_v1_save_post(body=body)



Create product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductRepositoryV1Api()
body = swagger_client.Body18() # Body18 |  (optional)

try: 
    api_response = api_instance.catalog_product_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductRepositoryV1Api->catalog_product_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body18**](Body18.md)|  | [optional] 

### Return type

[**CatalogDataProductInterface**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_repository_v1_save_put**
> CatalogDataProductInterface catalog_product_repository_v1_save_put(sku, body=body)



Create product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductRepositoryV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body19() # Body19 |  (optional)

try: 
    api_response = api_instance.catalog_product_repository_v1_save_put(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductRepositoryV1Api->catalog_product_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body19**](Body19.md)|  | [optional] 

### Return type

[**CatalogDataProductInterface**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

