# swagger_client.CheckoutGuestShippingInformationManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_guest_shipping_information_management_v1_save_address_information_post**](CheckoutGuestShippingInformationManagementV1Api.md#checkout_guest_shipping_information_management_v1_save_address_information_post) | **POST** /V1/guest-carts/{cartId}/shipping-information | 


# **checkout_guest_shipping_information_management_v1_save_address_information_post**
> CheckoutDataPaymentDetailsInterface checkout_guest_shipping_information_management_v1_save_address_information_post(cart_id, body=body)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutGuestShippingInformationManagementV1Api()
cart_id = 'cart_id_example' # str | 
body = swagger_client.Body109() # Body109 |  (optional)

try: 
    api_response = api_instance.checkout_guest_shipping_information_management_v1_save_address_information_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutGuestShippingInformationManagementV1Api->checkout_guest_shipping_information_management_v1_save_address_information_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **body** | [**Body109**](Body109.md)|  | [optional] 

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

