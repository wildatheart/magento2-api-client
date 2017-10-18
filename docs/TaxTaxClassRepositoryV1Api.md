# swagger_client.TaxTaxClassRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tax_tax_class_repository_v1_delete_by_id_delete**](TaxTaxClassRepositoryV1Api.md#tax_tax_class_repository_v1_delete_by_id_delete) | **DELETE** /V1/taxClasses/{taxClassId} | 
[**tax_tax_class_repository_v1_get_get**](TaxTaxClassRepositoryV1Api.md#tax_tax_class_repository_v1_get_get) | **GET** /V1/taxClasses/{taxClassId} | 
[**tax_tax_class_repository_v1_get_list_get**](TaxTaxClassRepositoryV1Api.md#tax_tax_class_repository_v1_get_list_get) | **GET** /V1/taxClasses/search | 
[**tax_tax_class_repository_v1_save_post**](TaxTaxClassRepositoryV1Api.md#tax_tax_class_repository_v1_save_post) | **POST** /V1/taxClasses | 
[**tax_tax_class_repository_v1_save_put**](TaxTaxClassRepositoryV1Api.md#tax_tax_class_repository_v1_save_put) | **PUT** /V1/taxClasses/{classId} | 


# **tax_tax_class_repository_v1_delete_by_id_delete**
> bool tax_tax_class_repository_v1_delete_by_id_delete(tax_class_id)



Delete a tax class with the given tax class id.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxTaxClassRepositoryV1Api()
tax_class_id = 56 # int | 

try: 
    api_response = api_instance.tax_tax_class_repository_v1_delete_by_id_delete(tax_class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxTaxClassRepositoryV1Api->tax_tax_class_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_class_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_tax_class_repository_v1_get_get**
> TaxDataTaxClassInterface tax_tax_class_repository_v1_get_get(tax_class_id)



Get a tax class with the given tax class id.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxTaxClassRepositoryV1Api()
tax_class_id = 56 # int | 

try: 
    api_response = api_instance.tax_tax_class_repository_v1_get_get(tax_class_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxTaxClassRepositoryV1Api->tax_tax_class_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_class_id** | **int**|  | 

### Return type

[**TaxDataTaxClassInterface**](TaxDataTaxClassInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_tax_class_repository_v1_get_list_get**
> TaxDataTaxClassSearchResultsInterface tax_tax_class_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve tax classes which match a specific criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See http://devdocs.magento.com/codelinks/attributes.html#TaxClassRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxTaxClassRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.tax_tax_class_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxTaxClassRepositoryV1Api->tax_tax_class_repository_v1_get_list_get: %s\n" % e)
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

[**TaxDataTaxClassSearchResultsInterface**](TaxDataTaxClassSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_tax_class_repository_v1_save_post**
> str tax_tax_class_repository_v1_save_post(body=body)



Create a Tax Class

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxTaxClassRepositoryV1Api()
body = swagger_client.Body136() # Body136 |  (optional)

try: 
    api_response = api_instance.tax_tax_class_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxTaxClassRepositoryV1Api->tax_tax_class_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body136**](Body136.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tax_tax_class_repository_v1_save_put**
> str tax_tax_class_repository_v1_save_put(class_id, body=body)



Create a Tax Class

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TaxTaxClassRepositoryV1Api()
class_id = 'class_id_example' # str | 
body = swagger_client.Body137() # Body137 |  (optional)

try: 
    api_response = api_instance.tax_tax_class_repository_v1_save_put(class_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TaxTaxClassRepositoryV1Api->tax_tax_class_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **class_id** | **str**|  | 
 **body** | [**Body137**](Body137.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

