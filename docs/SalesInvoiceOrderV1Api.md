# swagger_client.SalesInvoiceOrderV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_invoice_order_v1_execute_post**](SalesInvoiceOrderV1Api.md#sales_invoice_order_v1_execute_post) | **POST** /V1/order/{orderId}/invoice | 


# **sales_invoice_order_v1_execute_post**
> int sales_invoice_order_v1_execute_post(order_id, body=body)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesInvoiceOrderV1Api()
order_id = 56 # int | 
body = swagger_client.Body102() # Body102 |  (optional)

try: 
    api_response = api_instance.sales_invoice_order_v1_execute_post(order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoiceOrderV1Api->sales_invoice_order_v1_execute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **body** | [**Body102**](Body102.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

