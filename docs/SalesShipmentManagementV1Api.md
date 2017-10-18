# swagger_client.SalesShipmentManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_shipment_management_v1_get_comments_list_get**](SalesShipmentManagementV1Api.md#sales_shipment_management_v1_get_comments_list_get) | **GET** /V1/shipment/{id}/comments | 
[**sales_shipment_management_v1_get_label_get**](SalesShipmentManagementV1Api.md#sales_shipment_management_v1_get_label_get) | **GET** /V1/shipment/{id}/label | 
[**sales_shipment_management_v1_notify_post**](SalesShipmentManagementV1Api.md#sales_shipment_management_v1_notify_post) | **POST** /V1/shipment/{id}/emails | 


# **sales_shipment_management_v1_get_comments_list_get**
> SalesDataShipmentCommentSearchResultInterface sales_shipment_management_v1_get_comments_list_get(id)



Lists comments for a specified shipment.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesShipmentManagementV1Api()
id = 56 # int | The shipment ID.

try: 
    api_response = api_instance.sales_shipment_management_v1_get_comments_list_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesShipmentManagementV1Api->sales_shipment_management_v1_get_comments_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shipment ID. | 

### Return type

[**SalesDataShipmentCommentSearchResultInterface**](SalesDataShipmentCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_shipment_management_v1_get_label_get**
> str sales_shipment_management_v1_get_label_get(id)



Gets a specified shipment label.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesShipmentManagementV1Api()
id = 56 # int | The shipment label ID.

try: 
    api_response = api_instance.sales_shipment_management_v1_get_label_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesShipmentManagementV1Api->sales_shipment_management_v1_get_label_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shipment label ID. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_shipment_management_v1_notify_post**
> bool sales_shipment_management_v1_notify_post(id)



Emails user a specified shipment.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesShipmentManagementV1Api()
id = 56 # int | The shipment ID.

try: 
    api_response = api_instance.sales_shipment_management_v1_notify_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesShipmentManagementV1Api->sales_shipment_management_v1_notify_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shipment ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

