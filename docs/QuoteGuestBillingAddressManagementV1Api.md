# swagger_client.QuoteGuestBillingAddressManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_billing_address_management_v1_assign_post**](QuoteGuestBillingAddressManagementV1Api.md#quote_guest_billing_address_management_v1_assign_post) | **POST** /V1/guest-carts/{cartId}/billing-address | 
[**quote_guest_billing_address_management_v1_get_get**](QuoteGuestBillingAddressManagementV1Api.md#quote_guest_billing_address_management_v1_get_get) | **GET** /V1/guest-carts/{cartId}/billing-address | 


# **quote_guest_billing_address_management_v1_assign_post**
> int quote_guest_billing_address_management_v1_assign_post(cart_id, body=body)



Assign a specified billing address to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestBillingAddressManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
body = swagger_client.Body75() # Body75 |  (optional)

try: 
    api_response = api_instance.quote_guest_billing_address_management_v1_assign_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestBillingAddressManagementV1Api->quote_guest_billing_address_management_v1_assign_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **body** | [**Body75**](Body75.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_billing_address_management_v1_get_get**
> QuoteDataAddressInterface quote_guest_billing_address_management_v1_get_get(cart_id)



Return the billing address for a specified quote.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestBillingAddressManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.

try: 
    api_response = api_instance.quote_guest_billing_address_management_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestBillingAddressManagementV1Api->quote_guest_billing_address_management_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 

### Return type

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

