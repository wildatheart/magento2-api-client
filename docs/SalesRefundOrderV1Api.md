# swagger_client.SalesRefundOrderV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_refund_order_v1_execute_post**](SalesRefundOrderV1Api.md#sales_refund_order_v1_execute_post) | **POST** /V1/order/{orderId}/refund | 


# **sales_refund_order_v1_execute_post**
> int sales_refund_order_v1_execute_post(order_id, body=body)



Create offline refund for order

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRefundOrderV1Api()
order_id = 56 # int | 
body = swagger_client.Body97() # Body97 |  (optional)

try: 
    api_response = api_instance.sales_refund_order_v1_execute_post(order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRefundOrderV1Api->sales_refund_order_v1_execute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **body** | [**Body97**](Body97.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

