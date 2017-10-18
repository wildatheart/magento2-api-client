# swagger_client.QuoteShipmentEstimationV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_shipment_estimation_v1_estimate_by_extended_address_post**](QuoteShipmentEstimationV1Api.md#quote_shipment_estimation_v1_estimate_by_extended_address_post) | **POST** /V1/carts/{cartId}/estimate-shipping-methods | 
[**quote_shipment_estimation_v1_estimate_by_extended_address_post_0**](QuoteShipmentEstimationV1Api.md#quote_shipment_estimation_v1_estimate_by_extended_address_post_0) | **POST** /V1/carts/mine/estimate-shipping-methods | 


# **quote_shipment_estimation_v1_estimate_by_extended_address_post**
> list[QuoteDataShippingMethodInterface] quote_shipment_estimation_v1_estimate_by_extended_address_post(cart_id, body=body)



Estimate shipping by address and return list of available shipping methods

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteShipmentEstimationV1Api()
cart_id = 'cart_id_example' # str | 
body = swagger_client.Body61() # Body61 |  (optional)

try: 
    api_response = api_instance.quote_shipment_estimation_v1_estimate_by_extended_address_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteShipmentEstimationV1Api->quote_shipment_estimation_v1_estimate_by_extended_address_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **body** | [**Body61**](Body61.md)|  | [optional] 

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_shipment_estimation_v1_estimate_by_extended_address_post_0**
> list[QuoteDataShippingMethodInterface] quote_shipment_estimation_v1_estimate_by_extended_address_post_0(body=body)



Estimate shipping by address and return list of available shipping methods

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteShipmentEstimationV1Api()
body = swagger_client.Body62() # Body62 |  (optional)

try: 
    api_response = api_instance.quote_shipment_estimation_v1_estimate_by_extended_address_post_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteShipmentEstimationV1Api->quote_shipment_estimation_v1_estimate_by_extended_address_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body62**](Body62.md)|  | [optional] 

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

