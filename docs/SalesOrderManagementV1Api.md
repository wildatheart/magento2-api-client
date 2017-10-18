# swagger_client.SalesOrderManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_order_management_v1_add_comment_post**](SalesOrderManagementV1Api.md#sales_order_management_v1_add_comment_post) | **POST** /V1/orders/{id}/comments | 
[**sales_order_management_v1_cancel_post**](SalesOrderManagementV1Api.md#sales_order_management_v1_cancel_post) | **POST** /V1/orders/{id}/cancel | 
[**sales_order_management_v1_get_comments_list_get**](SalesOrderManagementV1Api.md#sales_order_management_v1_get_comments_list_get) | **GET** /V1/orders/{id}/comments | 
[**sales_order_management_v1_get_status_get**](SalesOrderManagementV1Api.md#sales_order_management_v1_get_status_get) | **GET** /V1/orders/{id}/statuses | 
[**sales_order_management_v1_hold_post**](SalesOrderManagementV1Api.md#sales_order_management_v1_hold_post) | **POST** /V1/orders/{id}/hold | 
[**sales_order_management_v1_notify_post**](SalesOrderManagementV1Api.md#sales_order_management_v1_notify_post) | **POST** /V1/orders/{id}/emails | 
[**sales_order_management_v1_un_hold_post**](SalesOrderManagementV1Api.md#sales_order_management_v1_un_hold_post) | **POST** /V1/orders/{id}/unhold | 


# **sales_order_management_v1_add_comment_post**
> bool sales_order_management_v1_add_comment_post(id, body=body)



Adds a comment to a specified order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderManagementV1Api()
id = 56 # int | The order ID.
body = swagger_client.Body89() # Body89 |  (optional)

try: 
    api_response = api_instance.sales_order_management_v1_add_comment_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderManagementV1Api->sales_order_management_v1_add_comment_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The order ID. | 
 **body** | [**Body89**](Body89.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_management_v1_cancel_post**
> bool sales_order_management_v1_cancel_post(id)



Cancels a specified order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderManagementV1Api()
id = 56 # int | The order ID.

try: 
    api_response = api_instance.sales_order_management_v1_cancel_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderManagementV1Api->sales_order_management_v1_cancel_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The order ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_management_v1_get_comments_list_get**
> SalesDataOrderStatusHistorySearchResultInterface sales_order_management_v1_get_comments_list_get(id)



Lists comments for a specified order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderManagementV1Api()
id = 56 # int | The order ID.

try: 
    api_response = api_instance.sales_order_management_v1_get_comments_list_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderManagementV1Api->sales_order_management_v1_get_comments_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The order ID. | 

### Return type

[**SalesDataOrderStatusHistorySearchResultInterface**](SalesDataOrderStatusHistorySearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_management_v1_get_status_get**
> str sales_order_management_v1_get_status_get(id)



Gets the status for a specified order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderManagementV1Api()
id = 56 # int | The order ID.

try: 
    api_response = api_instance.sales_order_management_v1_get_status_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderManagementV1Api->sales_order_management_v1_get_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The order ID. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_management_v1_hold_post**
> bool sales_order_management_v1_hold_post(id)



Holds a specified order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderManagementV1Api()
id = 56 # int | The order ID.

try: 
    api_response = api_instance.sales_order_management_v1_hold_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderManagementV1Api->sales_order_management_v1_hold_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The order ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_management_v1_notify_post**
> bool sales_order_management_v1_notify_post(id)



Emails a user a specified order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderManagementV1Api()
id = 56 # int | The order ID.

try: 
    api_response = api_instance.sales_order_management_v1_notify_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderManagementV1Api->sales_order_management_v1_notify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The order ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_order_management_v1_un_hold_post**
> bool sales_order_management_v1_un_hold_post(id)



Releases a specified order from hold status.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesOrderManagementV1Api()
id = 56 # int | The order ID.

try: 
    api_response = api_instance.sales_order_management_v1_un_hold_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesOrderManagementV1Api->sales_order_management_v1_un_hold_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The order ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

