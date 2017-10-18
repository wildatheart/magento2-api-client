# swagger_client.SalesShipmentCommentRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_shipment_comment_repository_v1_save_post**](SalesShipmentCommentRepositoryV1Api.md#sales_shipment_comment_repository_v1_save_post) | **POST** /V1/shipment/{id}/comments | 


# **sales_shipment_comment_repository_v1_save_post**
> SalesDataShipmentCommentInterface sales_shipment_comment_repository_v1_save_post(id, body=body)



Performs persist operations for a specified shipment comment.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesShipmentCommentRepositoryV1Api()
id = 'id_example' # str | 
body = swagger_client.Body99() # Body99 |  (optional)

try: 
    api_response = api_instance.sales_shipment_comment_repository_v1_save_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesShipmentCommentRepositoryV1Api->sales_shipment_comment_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**Body99**](Body99.md)|  | [optional] 

### Return type

[**SalesDataShipmentCommentInterface**](SalesDataShipmentCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

