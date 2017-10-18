# swagger_client.CustomerCustomerRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_customer_repository_v1_delete_by_id_delete**](CustomerCustomerRepositoryV1Api.md#customer_customer_repository_v1_delete_by_id_delete) | **DELETE** /V1/customers/{customerId} | 
[**customer_customer_repository_v1_get_by_id_get**](CustomerCustomerRepositoryV1Api.md#customer_customer_repository_v1_get_by_id_get) | **GET** /V1/customers/{customerId} | 
[**customer_customer_repository_v1_get_by_id_get_0**](CustomerCustomerRepositoryV1Api.md#customer_customer_repository_v1_get_by_id_get_0) | **GET** /V1/customers/me | 
[**customer_customer_repository_v1_get_list_get**](CustomerCustomerRepositoryV1Api.md#customer_customer_repository_v1_get_list_get) | **GET** /V1/customers/search | 
[**customer_customer_repository_v1_save_put**](CustomerCustomerRepositoryV1Api.md#customer_customer_repository_v1_save_put) | **PUT** /V1/customers/{id} | 
[**customer_customer_repository_v1_save_put_0**](CustomerCustomerRepositoryV1Api.md#customer_customer_repository_v1_save_put_0) | **PUT** /V1/customers/me | 


# **customer_customer_repository_v1_delete_by_id_delete**
> bool customer_customer_repository_v1_delete_by_id_delete(customer_id)



Delete customer by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerCustomerRepositoryV1Api()
customer_id = 56 # int | 

try: 
    api_response = api_instance.customer_customer_repository_v1_delete_by_id_delete(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerCustomerRepositoryV1Api->customer_customer_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_repository_v1_get_by_id_get**
> CustomerDataCustomerInterface customer_customer_repository_v1_get_by_id_get(customer_id)



Get customer by customer ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerCustomerRepositoryV1Api()
customer_id = 56 # int | 

try: 
    api_response = api_instance.customer_customer_repository_v1_get_by_id_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerCustomerRepositoryV1Api->customer_customer_repository_v1_get_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_repository_v1_get_by_id_get_0**
> CustomerDataCustomerInterface customer_customer_repository_v1_get_by_id_get_0()



Get customer by customer ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerCustomerRepositoryV1Api()

try: 
    api_response = api_instance.customer_customer_repository_v1_get_by_id_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerCustomerRepositoryV1Api->customer_customer_repository_v1_get_by_id_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_repository_v1_get_list_get**
> CustomerDataCustomerSearchResultsInterface customer_customer_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve customers which match a specified criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See http://devdocs.magento.com/codelinks/attributes.html#CustomerRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerCustomerRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.customer_customer_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerCustomerRepositoryV1Api->customer_customer_repository_v1_get_list_get: %s\n" % e)
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

[**CustomerDataCustomerSearchResultsInterface**](CustomerDataCustomerSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_repository_v1_save_put**
> CustomerDataCustomerInterface customer_customer_repository_v1_save_put(id, body=body)



Create or update a customer.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerCustomerRepositoryV1Api()
id = 'id_example' # str | 
body = swagger_client.Body4() # Body4 |  (optional)

try: 
    api_response = api_instance.customer_customer_repository_v1_save_put(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerCustomerRepositoryV1Api->customer_customer_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_customer_repository_v1_save_put_0**
> CustomerDataCustomerInterface customer_customer_repository_v1_save_put_0(body=body)



Create or update a customer.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerCustomerRepositoryV1Api()
body = swagger_client.Body5() # Body5 |  (optional)

try: 
    api_response = api_instance.customer_customer_repository_v1_save_put_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerCustomerRepositoryV1Api->customer_customer_repository_v1_save_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

