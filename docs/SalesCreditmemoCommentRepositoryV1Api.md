# swagger_client.SalesCreditmemoCommentRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_creditmemo_comment_repository_v1_save_post**](SalesCreditmemoCommentRepositoryV1Api.md#sales_creditmemo_comment_repository_v1_save_post) | **POST** /V1/creditmemo/{id}/comments | 


# **sales_creditmemo_comment_repository_v1_save_post**
> SalesDataCreditmemoCommentInterface sales_creditmemo_comment_repository_v1_save_post(id, body=body)



Performs persist operations for a specified entity.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesCreditmemoCommentRepositoryV1Api()
id = 'id_example' # str | 
body = swagger_client.Body94() # Body94 |  (optional)

try: 
    api_response = api_instance.sales_creditmemo_comment_repository_v1_save_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesCreditmemoCommentRepositoryV1Api->sales_creditmemo_comment_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body94**](Body94.md)|  | [optional] 

### Return type

[**SalesDataCreditmemoCommentInterface**](SalesDataCreditmemoCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

