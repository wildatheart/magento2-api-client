# swagger_client.SalesShipmentTrackRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_shipment_track_repository_v1_delete_by_id_delete**](SalesShipmentTrackRepositoryV1Api.md#sales_shipment_track_repository_v1_delete_by_id_delete) | **DELETE** /V1/shipment/track/{id} | 
[**sales_shipment_track_repository_v1_save_post**](SalesShipmentTrackRepositoryV1Api.md#sales_shipment_track_repository_v1_save_post) | **POST** /V1/shipment/track | 


# **sales_shipment_track_repository_v1_delete_by_id_delete**
> bool sales_shipment_track_repository_v1_delete_by_id_delete(id)



Deletes a specified shipment track by ID.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesShipmentTrackRepositoryV1Api()
id = 56 # int | The shipment track ID.

try: 
    api_response = api_instance.sales_shipment_track_repository_v1_delete_by_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesShipmentTrackRepositoryV1Api->sales_shipment_track_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The shipment track ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_shipment_track_repository_v1_save_post**
> SalesDataShipmentTrackInterface sales_shipment_track_repository_v1_save_post(body=body)



Performs persist operations for a specified shipment track.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesShipmentTrackRepositoryV1Api()
body = swagger_client.Body100() # Body100 |  (optional)

try: 
    api_response = api_instance.sales_shipment_track_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesShipmentTrackRepositoryV1Api->sales_shipment_track_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body100**](Body100.md)|  | [optional] 

### Return type

[**SalesDataShipmentTrackInterface**](SalesDataShipmentTrackInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

