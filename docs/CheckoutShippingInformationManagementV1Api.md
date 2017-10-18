# swagger_client.CheckoutShippingInformationManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_shipping_information_management_v1_save_address_information_post**](CheckoutShippingInformationManagementV1Api.md#checkout_shipping_information_management_v1_save_address_information_post) | **POST** /V1/carts/mine/shipping-information | 
[**checkout_shipping_information_management_v1_save_address_information_post_0**](CheckoutShippingInformationManagementV1Api.md#checkout_shipping_information_management_v1_save_address_information_post_0) | **POST** /V1/carts/{cartId}/shipping-information | 


# **checkout_shipping_information_management_v1_save_address_information_post**
> CheckoutDataPaymentDetailsInterface checkout_shipping_information_management_v1_save_address_information_post(body=body)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutShippingInformationManagementV1Api()
body = swagger_client.Body110() # Body110 |  (optional)

try: 
    api_response = api_instance.checkout_shipping_information_management_v1_save_address_information_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutShippingInformationManagementV1Api->checkout_shipping_information_management_v1_save_address_information_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body110**](Body110.md)|  | [optional] 

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_shipping_information_management_v1_save_address_information_post_0**
> CheckoutDataPaymentDetailsInterface checkout_shipping_information_management_v1_save_address_information_post_0(cart_id, body=body)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutShippingInformationManagementV1Api()
cart_id = 56 # int | 
body = swagger_client.Body111() # Body111 |  (optional)

try: 
    api_response = api_instance.checkout_shipping_information_management_v1_save_address_information_post_0(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutShippingInformationManagementV1Api->checkout_shipping_information_management_v1_save_address_information_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**|  | 
 **body** | [**Body111**](Body111.md)|  | [optional] 

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

