# swagger_client.QuoteGuestShipmentEstimationV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_shipment_estimation_v1_estimate_by_extended_address_post**](QuoteGuestShipmentEstimationV1Api.md#quote_guest_shipment_estimation_v1_estimate_by_extended_address_post) | **POST** /V1/guest-carts/{cartId}/estimate-shipping-methods | 


# **quote_guest_shipment_estimation_v1_estimate_by_extended_address_post**
> list[QuoteDataShippingMethodInterface] quote_guest_shipment_estimation_v1_estimate_by_extended_address_post(cart_id, body=body)



Estimate shipping by address and return list of available shipping methods

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestShipmentEstimationV1Api()
cart_id = 'cart_id_example' # str | 
body = swagger_client.Body63() # Body63 |  (optional)

try: 
    api_response = api_instance.quote_guest_shipment_estimation_v1_estimate_by_extended_address_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestShipmentEstimationV1Api->quote_guest_shipment_estimation_v1_estimate_by_extended_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **body** | [**Body63**](Body63.md)|  | [optional] 

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

