# swagger_client.QuoteGuestCartItemRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_cart_item_repository_v1_delete_by_id_delete**](QuoteGuestCartItemRepositoryV1Api.md#quote_guest_cart_item_repository_v1_delete_by_id_delete) | **DELETE** /V1/guest-carts/{cartId}/items/{itemId} | 
[**quote_guest_cart_item_repository_v1_get_list_get**](QuoteGuestCartItemRepositoryV1Api.md#quote_guest_cart_item_repository_v1_get_list_get) | **GET** /V1/guest-carts/{cartId}/items | 
[**quote_guest_cart_item_repository_v1_save_post**](QuoteGuestCartItemRepositoryV1Api.md#quote_guest_cart_item_repository_v1_save_post) | **POST** /V1/guest-carts/{cartId}/items | 
[**quote_guest_cart_item_repository_v1_save_put**](QuoteGuestCartItemRepositoryV1Api.md#quote_guest_cart_item_repository_v1_save_put) | **PUT** /V1/guest-carts/{cartId}/items/{itemId} | 


# **quote_guest_cart_item_repository_v1_delete_by_id_delete**
> bool quote_guest_cart_item_repository_v1_delete_by_id_delete(cart_id, item_id)



Remove the specified item from the specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartItemRepositoryV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
item_id = 56 # int | The item ID of the item to be removed.

try: 
    api_response = api_instance.quote_guest_cart_item_repository_v1_delete_by_id_delete(cart_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartItemRepositoryV1Api->quote_guest_cart_item_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **item_id** | **int**| The item ID of the item to be removed. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_cart_item_repository_v1_get_list_get**
> list[QuoteDataCartItemInterface] quote_guest_cart_item_repository_v1_get_list_get(cart_id)



List items that are assigned to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartItemRepositoryV1Api()
cart_id = 'cart_id_example' # str | The cart ID.

try: 
    api_response = api_instance.quote_guest_cart_item_repository_v1_get_list_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartItemRepositoryV1Api->quote_guest_cart_item_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 

### Return type

[**list[QuoteDataCartItemInterface]**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_cart_item_repository_v1_save_post**
> QuoteDataCartItemInterface quote_guest_cart_item_repository_v1_save_post(cart_id, body=body)



Add/update the specified cart item.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartItemRepositoryV1Api()
cart_id = 'cart_id_example' # str | 
body = swagger_client.Body68() # Body68 |  (optional)

try: 
    api_response = api_instance.quote_guest_cart_item_repository_v1_save_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartItemRepositoryV1Api->quote_guest_cart_item_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **body** | [**Body68**](Body68.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_cart_item_repository_v1_save_put**
> QuoteDataCartItemInterface quote_guest_cart_item_repository_v1_save_put(cart_id, item_id, body=body)



Add/update the specified cart item.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCartItemRepositoryV1Api()
cart_id = 'cart_id_example' # str | 
item_id = 'item_id_example' # str | 
body = swagger_client.Body69() # Body69 |  (optional)

try: 
    api_response = api_instance.quote_guest_cart_item_repository_v1_save_put(cart_id, item_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCartItemRepositoryV1Api->quote_guest_cart_item_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
 **body** | [**Body69**](Body69.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

