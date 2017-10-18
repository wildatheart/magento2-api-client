# swagger_client.SalesCreditmemoManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_creditmemo_management_v1_cancel_put**](SalesCreditmemoManagementV1Api.md#sales_creditmemo_management_v1_cancel_put) | **PUT** /V1/creditmemo/{id} | 
[**sales_creditmemo_management_v1_get_comments_list_get**](SalesCreditmemoManagementV1Api.md#sales_creditmemo_management_v1_get_comments_list_get) | **GET** /V1/creditmemo/{id}/comments | 
[**sales_creditmemo_management_v1_notify_post**](SalesCreditmemoManagementV1Api.md#sales_creditmemo_management_v1_notify_post) | **POST** /V1/creditmemo/{id}/emails | 
[**sales_creditmemo_management_v1_refund_post**](SalesCreditmemoManagementV1Api.md#sales_creditmemo_management_v1_refund_post) | **POST** /V1/creditmemo/refund | 


# **sales_creditmemo_management_v1_cancel_put**
> bool sales_creditmemo_management_v1_cancel_put(id)



Cancels a specified credit memo.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesCreditmemoManagementV1Api()
id = 56 # int | The credit memo ID.

try: 
    api_response = api_instance.sales_creditmemo_management_v1_cancel_put(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesCreditmemoManagementV1Api->sales_creditmemo_management_v1_cancel_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The credit memo ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_creditmemo_management_v1_get_comments_list_get**
> SalesDataCreditmemoCommentSearchResultInterface sales_creditmemo_management_v1_get_comments_list_get(id)



Lists comments for a specified credit memo.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesCreditmemoManagementV1Api()
id = 56 # int | The credit memo ID.

try: 
    api_response = api_instance.sales_creditmemo_management_v1_get_comments_list_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesCreditmemoManagementV1Api->sales_creditmemo_management_v1_get_comments_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The credit memo ID. | 

### Return type

[**SalesDataCreditmemoCommentSearchResultInterface**](SalesDataCreditmemoCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_creditmemo_management_v1_notify_post**
> bool sales_creditmemo_management_v1_notify_post(id)



Emails a user a specified credit memo.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesCreditmemoManagementV1Api()
id = 56 # int | The credit memo ID.

try: 
    api_response = api_instance.sales_creditmemo_management_v1_notify_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesCreditmemoManagementV1Api->sales_creditmemo_management_v1_notify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The credit memo ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_creditmemo_management_v1_refund_post**
> SalesDataCreditmemoInterface sales_creditmemo_management_v1_refund_post(body=body)



Prepare creditmemo to refund and save it.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesCreditmemoManagementV1Api()
body = swagger_client.Body95() # Body95 |  (optional)

try: 
    api_response = api_instance.sales_creditmemo_management_v1_refund_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesCreditmemoManagementV1Api->sales_creditmemo_management_v1_refund_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body95**](Body95.md)|  | [optional] 

### Return type

[**SalesDataCreditmemoInterface**](SalesDataCreditmemoInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

