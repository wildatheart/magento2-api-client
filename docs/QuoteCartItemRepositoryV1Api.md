# swagger_client.QuoteCartItemRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_cart_item_repository_v1_delete_by_id_delete**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_delete_by_id_delete) | **DELETE** /V1/carts/{cartId}/items/{itemId} | 
[**quote_cart_item_repository_v1_delete_by_id_delete_0**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_delete_by_id_delete_0) | **DELETE** /V1/carts/mine/items/{itemId} | 
[**quote_cart_item_repository_v1_get_list_get**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_get_list_get) | **GET** /V1/carts/{cartId}/items | 
[**quote_cart_item_repository_v1_get_list_get_0**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_get_list_get_0) | **GET** /V1/carts/mine/items | 
[**quote_cart_item_repository_v1_save_post**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_save_post) | **POST** /V1/carts/{quoteId}/items | 
[**quote_cart_item_repository_v1_save_post_0**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_save_post_0) | **POST** /V1/carts/mine/items | 
[**quote_cart_item_repository_v1_save_put**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_save_put) | **PUT** /V1/carts/{cartId}/items/{itemId} | 
[**quote_cart_item_repository_v1_save_put_0**](QuoteCartItemRepositoryV1Api.md#quote_cart_item_repository_v1_save_put_0) | **PUT** /V1/carts/mine/items/{itemId} | 


# **quote_cart_item_repository_v1_delete_by_id_delete**
> bool quote_cart_item_repository_v1_delete_by_id_delete(cart_id, item_id)



Removes the specified item from the specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()
cart_id = 56 # int | The cart ID.
item_id = 56 # int | The item ID of the item to be removed.

try: 
    api_response = api_instance.quote_cart_item_repository_v1_delete_by_id_delete(cart_id, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 
 **item_id** | **int**| The item ID of the item to be removed. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_item_repository_v1_delete_by_id_delete_0**
> bool quote_cart_item_repository_v1_delete_by_id_delete_0(item_id)



Removes the specified item from the specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()
item_id = 56 # int | The item ID of the item to be removed.

try: 
    api_response = api_instance.quote_cart_item_repository_v1_delete_by_id_delete_0(item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_delete_by_id_delete_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **int**| The item ID of the item to be removed. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_item_repository_v1_get_list_get**
> list[QuoteDataCartItemInterface] quote_cart_item_repository_v1_get_list_get(cart_id)



Lists items that are assigned to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()
cart_id = 56 # int | The cart ID.

try: 
    api_response = api_instance.quote_cart_item_repository_v1_get_list_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 

### Return type

[**list[QuoteDataCartItemInterface]**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_item_repository_v1_get_list_get_0**
> list[QuoteDataCartItemInterface] quote_cart_item_repository_v1_get_list_get_0()



Lists items that are assigned to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()

try: 
    api_response = api_instance.quote_cart_item_repository_v1_get_list_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_get_list_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QuoteDataCartItemInterface]**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_item_repository_v1_save_post**
> QuoteDataCartItemInterface quote_cart_item_repository_v1_save_post(quote_id, body=body)



Add/update the specified cart item.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()
quote_id = 'quote_id_example' # str | 
body = swagger_client.Body64() # Body64 |  (optional)

try: 
    api_response = api_instance.quote_cart_item_repository_v1_save_post(quote_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_id** | **str**|  | 
 **body** | [**Body64**](Body64.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_item_repository_v1_save_post_0**
> QuoteDataCartItemInterface quote_cart_item_repository_v1_save_post_0(body=body)



Add/update the specified cart item.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()
body = swagger_client.Body66() # Body66 |  (optional)

try: 
    api_response = api_instance.quote_cart_item_repository_v1_save_post_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_save_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body66**](Body66.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_item_repository_v1_save_put**
> QuoteDataCartItemInterface quote_cart_item_repository_v1_save_put(cart_id, item_id, body=body)



Add/update the specified cart item.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()
cart_id = 'cart_id_example' # str | 
item_id = 'item_id_example' # str | 
body = swagger_client.Body65() # Body65 |  (optional)

try: 
    api_response = api_instance.quote_cart_item_repository_v1_save_put(cart_id, item_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**|  | 
 **item_id** | **str**|  | 
 **body** | [**Body65**](Body65.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_item_repository_v1_save_put_0**
> QuoteDataCartItemInterface quote_cart_item_repository_v1_save_put_0(item_id, body=body)



Add/update the specified cart item.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartItemRepositoryV1Api()
item_id = 'item_id_example' # str | 
body = swagger_client.Body67() # Body67 |  (optional)

try: 
    api_response = api_instance.quote_cart_item_repository_v1_save_put_0(item_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartItemRepositoryV1Api->quote_cart_item_repository_v1_save_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**|  | 
 **body** | [**Body67**](Body67.md)|  | [optional] 

### Return type

[**QuoteDataCartItemInterface**](QuoteDataCartItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

