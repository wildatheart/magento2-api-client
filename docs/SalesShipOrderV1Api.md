# swagger_client.SalesShipOrderV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_ship_order_v1_execute_post**](SalesShipOrderV1Api.md#sales_ship_order_v1_execute_post) | **POST** /V1/order/{orderId}/ship | 


# **sales_ship_order_v1_execute_post**
> int sales_ship_order_v1_execute_post(order_id, body=body)



Creates new Shipment for given Order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesShipOrderV1Api()
order_id = 56 # int | 
body = swagger_client.Body101() # Body101 |  (optional)

try: 
    api_response = api_instance.sales_ship_order_v1_execute_post(order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesShipOrderV1Api->sales_ship_order_v1_execute_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**|  | 
 **body** | [**Body101**](Body101.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

