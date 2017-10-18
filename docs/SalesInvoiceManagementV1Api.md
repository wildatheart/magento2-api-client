# swagger_client.SalesInvoiceManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_invoice_management_v1_get_comments_list_get**](SalesInvoiceManagementV1Api.md#sales_invoice_management_v1_get_comments_list_get) | **GET** /V1/invoices/{id}/comments | 
[**sales_invoice_management_v1_notify_post**](SalesInvoiceManagementV1Api.md#sales_invoice_management_v1_notify_post) | **POST** /V1/invoices/{id}/emails | 
[**sales_invoice_management_v1_set_capture_post**](SalesInvoiceManagementV1Api.md#sales_invoice_management_v1_set_capture_post) | **POST** /V1/invoices/{id}/capture | 
[**sales_invoice_management_v1_set_void_post**](SalesInvoiceManagementV1Api.md#sales_invoice_management_v1_set_void_post) | **POST** /V1/invoices/{id}/void | 


# **sales_invoice_management_v1_get_comments_list_get**
> SalesDataInvoiceCommentSearchResultInterface sales_invoice_management_v1_get_comments_list_get(id)



Lists comments for a specified invoice.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesInvoiceManagementV1Api()
id = 56 # int | The invoice ID.

try: 
    api_response = api_instance.sales_invoice_management_v1_get_comments_list_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoiceManagementV1Api->sales_invoice_management_v1_get_comments_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The invoice ID. | 

### Return type

[**SalesDataInvoiceCommentSearchResultInterface**](SalesDataInvoiceCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_management_v1_notify_post**
> bool sales_invoice_management_v1_notify_post(id)



Emails a user a specified invoice.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesInvoiceManagementV1Api()
id = 56 # int | The invoice ID.

try: 
    api_response = api_instance.sales_invoice_management_v1_notify_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoiceManagementV1Api->sales_invoice_management_v1_notify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The invoice ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_management_v1_set_capture_post**
> str sales_invoice_management_v1_set_capture_post(id)



Sets invoice capture.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesInvoiceManagementV1Api()
id = 56 # int | 

try: 
    api_response = api_instance.sales_invoice_management_v1_set_capture_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoiceManagementV1Api->sales_invoice_management_v1_set_capture_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_invoice_management_v1_set_void_post**
> bool sales_invoice_management_v1_set_void_post(id)



Voids a specified invoice.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesInvoiceManagementV1Api()
id = 56 # int | The invoice ID.

try: 
    api_response = api_instance.sales_invoice_management_v1_set_void_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoiceManagementV1Api->sales_invoice_management_v1_set_void_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The invoice ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

