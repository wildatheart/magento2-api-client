# swagger_client.SalesRuleCouponRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_rule_coupon_repository_v1_delete_by_id_delete**](SalesRuleCouponRepositoryV1Api.md#sales_rule_coupon_repository_v1_delete_by_id_delete) | **DELETE** /V1/coupons/{couponId} | 
[**sales_rule_coupon_repository_v1_get_by_id_get**](SalesRuleCouponRepositoryV1Api.md#sales_rule_coupon_repository_v1_get_by_id_get) | **GET** /V1/coupons/{couponId} | 
[**sales_rule_coupon_repository_v1_get_list_get**](SalesRuleCouponRepositoryV1Api.md#sales_rule_coupon_repository_v1_get_list_get) | **GET** /V1/coupons/search | 
[**sales_rule_coupon_repository_v1_save_post**](SalesRuleCouponRepositoryV1Api.md#sales_rule_coupon_repository_v1_save_post) | **POST** /V1/coupons | 
[**sales_rule_coupon_repository_v1_save_put**](SalesRuleCouponRepositoryV1Api.md#sales_rule_coupon_repository_v1_save_put) | **PUT** /V1/coupons/{couponId} | 


# **sales_rule_coupon_repository_v1_delete_by_id_delete**
> bool sales_rule_coupon_repository_v1_delete_by_id_delete(coupon_id)



Delete coupon by coupon id.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponRepositoryV1Api()
coupon_id = 56 # int | 

try: 
    api_response = api_instance.sales_rule_coupon_repository_v1_delete_by_id_delete(coupon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponRepositoryV1Api->sales_rule_coupon_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_coupon_repository_v1_get_by_id_get**
> SalesRuleDataCouponInterface sales_rule_coupon_repository_v1_get_by_id_get(coupon_id)



Get coupon by coupon id.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponRepositoryV1Api()
coupon_id = 56 # int | 

try: 
    api_response = api_instance.sales_rule_coupon_repository_v1_get_by_id_get(coupon_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponRepositoryV1Api->sales_rule_coupon_repository_v1_get_by_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_id** | **int**|  | 

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_coupon_repository_v1_get_list_get**
> SalesRuleDataCouponSearchResultInterface sales_rule_coupon_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)



Retrieve a coupon using the specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See http://devdocs.magento.com/codelinks/attributes.html#CouponRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponRepositoryV1Api()
search_criteria_filter_groups_filters_field = 'search_criteria_filter_groups_filters_field_example' # str | Field (optional)
search_criteria_filter_groups_filters_value = 'search_criteria_filter_groups_filters_value_example' # str | Value (optional)
search_criteria_filter_groups_filters_condition_type = 'search_criteria_filter_groups_filters_condition_type_example' # str | Condition type (optional)
search_criteria_sort_orders_field = 'search_criteria_sort_orders_field_example' # str | Sorting field. (optional)
search_criteria_sort_orders_direction = 'search_criteria_sort_orders_direction_example' # str | Sorting direction. (optional)
search_criteria_page_size = 56 # int | Page size. (optional)
search_criteria_current_page = 56 # int | Current page. (optional)

try: 
    api_response = api_instance.sales_rule_coupon_repository_v1_get_list_get(search_criteria_filter_groups_filters_field=search_criteria_filter_groups_filters_field, search_criteria_filter_groups_filters_value=search_criteria_filter_groups_filters_value, search_criteria_filter_groups_filters_condition_type=search_criteria_filter_groups_filters_condition_type, search_criteria_sort_orders_field=search_criteria_sort_orders_field, search_criteria_sort_orders_direction=search_criteria_sort_orders_direction, search_criteria_page_size=search_criteria_page_size, search_criteria_current_page=search_criteria_current_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponRepositoryV1Api->sales_rule_coupon_repository_v1_get_list_get: %s\n" % e)
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

[**SalesRuleDataCouponSearchResultInterface**](SalesRuleDataCouponSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_coupon_repository_v1_save_post**
> SalesRuleDataCouponInterface sales_rule_coupon_repository_v1_save_post(body=body)



Save a coupon.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponRepositoryV1Api()
body = swagger_client.Body126() # Body126 |  (optional)

try: 
    api_response = api_instance.sales_rule_coupon_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponRepositoryV1Api->sales_rule_coupon_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body126**](Body126.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_coupon_repository_v1_save_put**
> SalesRuleDataCouponInterface sales_rule_coupon_repository_v1_save_put(coupon_id, body=body)



Save a coupon.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponRepositoryV1Api()
coupon_id = 'coupon_id_example' # str | 
body = swagger_client.Body125() # Body125 |  (optional)

try: 
    api_response = api_instance.sales_rule_coupon_repository_v1_save_put(coupon_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponRepositoryV1Api->sales_rule_coupon_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_id** | **str**|  | 
 **body** | [**Body125**](Body125.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

