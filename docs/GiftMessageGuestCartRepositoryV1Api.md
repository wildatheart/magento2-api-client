# swagger_client.GiftMessageGuestCartRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gift_message_guest_cart_repository_v1_get_get**](GiftMessageGuestCartRepositoryV1Api.md#gift_message_guest_cart_repository_v1_get_get) | **GET** /V1/guest-carts/{cartId}/gift-message | 
[**gift_message_guest_cart_repository_v1_save_post**](GiftMessageGuestCartRepositoryV1Api.md#gift_message_guest_cart_repository_v1_save_post) | **POST** /V1/guest-carts/{cartId}/gift-message | 


# **gift_message_guest_cart_repository_v1_get_get**
> GiftMessageDataMessageInterface gift_message_guest_cart_repository_v1_get_get(cart_id)



Return the gift message for a specified order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GiftMessageGuestCartRepositoryV1Api()
cart_id = 'cart_id_example' # str | The shopping cart ID.

try: 
    api_response = api_instance.gift_message_guest_cart_repository_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftMessageGuestCartRepositoryV1Api->gift_message_guest_cart_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The shopping cart ID. | 

### Return type

[**GiftMessageDataMessageInterface**](GiftMessageDataMessageInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gift_message_guest_cart_repository_v1_save_post**
> bool gift_message_guest_cart_repository_v1_save_post(cart_id, body=body)



Set the gift message for an entire order.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GiftMessageGuestCartRepositoryV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
body = swagger_client.Body107() # Body107 |  (optional)

try: 
    api_response = api_instance.gift_message_guest_cart_repository_v1_save_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GiftMessageGuestCartRepositoryV1Api->gift_message_guest_cart_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **body** | [**Body107**](Body107.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

