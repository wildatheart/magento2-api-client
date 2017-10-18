# swagger_client.SalesRuleRuleRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_rule_rule_repository_v1_delete_by_id_delete**](SalesRuleRuleRepositoryV1Api.md#sales_rule_rule_repository_v1_delete_by_id_delete) | **DELETE** /V1/salesRules/{ruleId} | 
[**sales_rule_rule_repository_v1_get_by_id_get**](SalesRuleRuleRepositoryV1Api.md#sales_rule_rule_repository_v1_get_by_id_get) | **GET** /V1/salesRules/{ruleId} | 
[**sales_rule_rule_repository_v1_get_list_get**](SalesRuleRuleRepositoryV1Api.md#sales_rule_rule_repository_v1_get_list_get) | **GET** /V1/salesRules/search | 
[**sales_rule_rule_repository_v1_save_post**](SalesRuleRuleRepositoryV1Api.md#sales_rule_rule_repository_v1_save_post) | **POST** /V1/salesRules | 
[**sales_rule_rule_repository_v1_save_put**](SalesRuleRuleRepositoryV1Api.md#sales_rule_rule_repository_v1_save_put) | **PUT** /V1/salesRules/{ruleId} | 


# **sales_rule_rule_repository_v1_delete_by_id_delete**
> bool sales_rule_rule_repository_v1_delete_by_id_delete(rule_id)



Delete rule by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleRuleRepositoryV1Api()
rule_id = 56 # int | 

try: 
    api_response = api_instance.sales_rule_rule_repository_v1_delete_by_id_delete(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleRuleRepositoryV1Api->sales_rule_rule_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_rule_repository_v1_get_by_id_get**
> SalesRuleDataRuleInterface sales_rule_rule_repository_v1_get_by_id_get(rule_id)



Get rule by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleRuleRepositoryV1Api()
rule_id = 56 # int | 

try: 
    api_response = api_instance.sales_rule_rule_repository_v1_get_by_id_get(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleRuleRepositoryV1Api->sales_rule_rule_repository_v1_get_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **int**|  | 

### Return type

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_rule_repository_v1_get_list_get**
> SalesRuleDataRuleSearchResultInterface sales_rule_rule_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve sales rules that match te specified criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See http://devdocs.magento.com/codelinks/attributes.html#RuleRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleRuleRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.sales_rule_rule_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleRuleRepositoryV1Api->sales_rule_rule_repository_v1_get_list_get: %s\n" % e)
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

[**SalesRuleDataRuleSearchResultInterface**](SalesRuleDataRuleSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_rule_repository_v1_save_post**
> SalesRuleDataRuleInterface sales_rule_rule_repository_v1_save_post(body=body)



Save sales rule.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleRuleRepositoryV1Api()
body = swagger_client.Body124() # Body124 |  (optional)

try: 
    api_response = api_instance.sales_rule_rule_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleRuleRepositoryV1Api->sales_rule_rule_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body124**](Body124.md)|  | [optional] 

### Return type

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_rule_repository_v1_save_put**
> SalesRuleDataRuleInterface sales_rule_rule_repository_v1_save_put(rule_id, body=body)



Save sales rule.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleRuleRepositoryV1Api()
rule_id = 'rule_id_example' # str | 
body = swagger_client.Body123() # Body123 |  (optional)

try: 
    api_response = api_instance.sales_rule_rule_repository_v1_save_put(rule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleRuleRepositoryV1Api->sales_rule_rule_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **body** | [**Body123**](Body123.md)|  | [optional] 

### Return type

[**SalesRuleDataRuleInterface**](SalesRuleDataRuleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

