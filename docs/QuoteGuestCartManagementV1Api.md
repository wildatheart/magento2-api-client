# swagger_client.QuoteGuestCartManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_cart_management_v1_assign_customer_put**](QuoteGuestCartManagementV1Api.md#quote_guest_cart_management_v1_assign_customer_put) | **PUT** /V1/guest-carts/{cartId} | 
[**quote_guest_cart_management_v1_create_empty_cart_post**](QuoteGuestCartManagementV1Api.md#quote_guest_cart_management_v1_create_empty_cart_post) | **POST** /V1/guest-carts | 
[**quote_guest_cart_management_v1_place_order_put**](QuoteGuestCartManagementV1Api.md#quote_guest_cart_management_v1_place_order_put) | **PUT** /V1/guest-carts/{cartId}/order | 


# **quote_guest_cart_management_v1_assign_customer_put**
> bool quote_guest_cart_management_v1_assign_customer_put(cart_id, body=body)



Assign a specified customer to a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
body = swagger_client.Body57() # Body57 |  (optional)

try: 
    api_response = api_instance.quote_guest_cart_management_v1_assign_customer_put(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartManagementV1Api->quote_guest_cart_management_v1_assign_customer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **body** | [**Body57**](Body57.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_cart_management_v1_create_empty_cart_post**
> str quote_guest_cart_management_v1_create_empty_cart_post()



Enable an customer or guest user to create an empty cart and quote for an anonymous customer.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartManagementV1Api()

try: 
    api_response = api_instance.quote_guest_cart_management_v1_create_empty_cart_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartManagementV1Api->quote_guest_cart_management_v1_create_empty_cart_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_cart_management_v1_place_order_put**
> int quote_guest_cart_management_v1_place_order_put(cart_id, body=body)



Place an order for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
body = swagger_client.Body58() # Body58 |  (optional)

try: 
    api_response = api_instance.quote_guest_cart_management_v1_place_order_put(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartManagementV1Api->quote_guest_cart_management_v1_place_order_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **body** | [**Body58**](Body58.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

