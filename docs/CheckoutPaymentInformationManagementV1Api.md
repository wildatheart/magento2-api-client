# swagger_client.CheckoutPaymentInformationManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_payment_information_management_v1_get_payment_information_get**](CheckoutPaymentInformationManagementV1Api.md#checkout_payment_information_management_v1_get_payment_information_get) | **GET** /V1/carts/mine/payment-information | 
[**checkout_payment_information_management_v1_save_payment_information_and_place_order_post**](CheckoutPaymentInformationManagementV1Api.md#checkout_payment_information_management_v1_save_payment_information_and_place_order_post) | **POST** /V1/carts/mine/payment-information | 
[**checkout_payment_information_management_v1_save_payment_information_post**](CheckoutPaymentInformationManagementV1Api.md#checkout_payment_information_management_v1_save_payment_information_post) | **POST** /V1/carts/mine/set-payment-information | 


# **checkout_payment_information_management_v1_get_payment_information_get**
> CheckoutDataPaymentDetailsInterface checkout_payment_information_management_v1_get_payment_information_get()



Get payment information

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutPaymentInformationManagementV1Api()

try: 
    api_response = api_instance.checkout_payment_information_management_v1_get_payment_information_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutPaymentInformationManagementV1Api->checkout_payment_information_management_v1_get_payment_information_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CheckoutDataPaymentDetailsInterface**](CheckoutDataPaymentDetailsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_payment_information_management_v1_save_payment_information_and_place_order_post**
> int checkout_payment_information_management_v1_save_payment_information_and_place_order_post(body=body)



Set payment information and place order for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutPaymentInformationManagementV1Api()
body = swagger_client.Body117() # Body117 |  (optional)

try: 
    api_response = api_instance.checkout_payment_information_management_v1_save_payment_information_and_place_order_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutPaymentInformationManagementV1Api->checkout_payment_information_management_v1_save_payment_information_and_place_order_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body117**](Body117.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_payment_information_management_v1_save_payment_information_post**
> int checkout_payment_information_management_v1_save_payment_information_post(body=body)



Set payment information for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutPaymentInformationManagementV1Api()
body = swagger_client.Body118() # Body118 |  (optional)

try: 
    api_response = api_instance.checkout_payment_information_management_v1_save_payment_information_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutPaymentInformationManagementV1Api->checkout_payment_information_management_v1_save_payment_information_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body118**](Body118.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

