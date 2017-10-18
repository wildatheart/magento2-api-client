# swagger_client.SalesRefundInvoiceV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_refund_invoice_v1_execute_post**](SalesRefundInvoiceV1Api.md#sales_refund_invoice_v1_execute_post) | **POST** /V1/invoice/{invoiceId}/refund | 


# **sales_refund_invoice_v1_execute_post**
> int sales_refund_invoice_v1_execute_post(invoice_id, body=body)



Create refund for invoice

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRefundInvoiceV1Api()
invoice_id = 56 # int | 
body = swagger_client.Body93() # Body93 |  (optional)

try: 
    api_response = api_instance.sales_refund_invoice_v1_execute_post(invoice_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRefundInvoiceV1Api->sales_refund_invoice_v1_execute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**|  | 
 **body** | [**Body93**](Body93.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

