# swagger_client.SalesInvoiceCommentRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_invoice_comment_repository_v1_save_post**](SalesInvoiceCommentRepositoryV1Api.md#sales_invoice_comment_repository_v1_save_post) | **POST** /V1/invoices/comments | 


# **sales_invoice_comment_repository_v1_save_post**
> SalesDataInvoiceCommentInterface sales_invoice_comment_repository_v1_save_post(body=body)



Performs persist operations for a specified invoice comment.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesInvoiceCommentRepositoryV1Api()
body = swagger_client.Body92() # Body92 |  (optional)

try: 
    api_response = api_instance.sales_invoice_comment_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesInvoiceCommentRepositoryV1Api->sales_invoice_comment_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body92**](Body92.md)|  | [optional] 

### Return type

[**SalesDataInvoiceCommentInterface**](SalesDataInvoiceCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

