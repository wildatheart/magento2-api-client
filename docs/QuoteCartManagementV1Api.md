# swagger_client.QuoteCartManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_cart_management_v1_assign_customer_put**](QuoteCartManagementV1Api.md#quote_cart_management_v1_assign_customer_put) | **PUT** /V1/carts/{cartId} | 
[**quote_cart_management_v1_create_empty_cart_for_customer_post**](QuoteCartManagementV1Api.md#quote_cart_management_v1_create_empty_cart_for_customer_post) | **POST** /V1/carts/mine | 
[**quote_cart_management_v1_create_empty_cart_for_customer_post_0**](QuoteCartManagementV1Api.md#quote_cart_management_v1_create_empty_cart_for_customer_post_0) | **POST** /V1/customers/{customerId}/carts | 
[**quote_cart_management_v1_create_empty_cart_post**](QuoteCartManagementV1Api.md#quote_cart_management_v1_create_empty_cart_post) | **POST** /V1/carts/ | 
[**quote_cart_management_v1_get_cart_for_customer_get**](QuoteCartManagementV1Api.md#quote_cart_management_v1_get_cart_for_customer_get) | **GET** /V1/carts/mine | 
[**quote_cart_management_v1_place_order_put**](QuoteCartManagementV1Api.md#quote_cart_management_v1_place_order_put) | **PUT** /V1/carts/mine/order | 
[**quote_cart_management_v1_place_order_put_0**](QuoteCartManagementV1Api.md#quote_cart_management_v1_place_order_put_0) | **PUT** /V1/carts/{cartId}/order | 


# **quote_cart_management_v1_assign_customer_put**
> bool quote_cart_management_v1_assign_customer_put(cart_id, body=body)



Assigns a specified customer to a specified shopping cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartManagementV1Api()
cart_id = 56 # int | The cart ID.
body = swagger_client.Body53() # Body53 |  (optional)

try: 
    api_response = api_instance.quote_cart_management_v1_assign_customer_put(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartManagementV1Api->quote_cart_management_v1_assign_customer_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 
 **body** | [**Body53**](Body53.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_management_v1_create_empty_cart_for_customer_post**
> int quote_cart_management_v1_create_empty_cart_for_customer_post()



Creates an empty cart and quote for a specified customer if customer does not have a cart yet.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartManagementV1Api()

try: 
    api_response = api_instance.quote_cart_management_v1_create_empty_cart_for_customer_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartManagementV1Api->quote_cart_management_v1_create_empty_cart_for_customer_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_management_v1_create_empty_cart_for_customer_post_0**
> int quote_cart_management_v1_create_empty_cart_for_customer_post_0(customer_id)



Creates an empty cart and quote for a specified customer if customer does not have a cart yet.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartManagementV1Api()
customer_id = 56 # int | The customer ID.

try: 
    api_response = api_instance.quote_cart_management_v1_create_empty_cart_for_customer_post_0(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartManagementV1Api->quote_cart_management_v1_create_empty_cart_for_customer_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| The customer ID. | 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_management_v1_create_empty_cart_post**
> int quote_cart_management_v1_create_empty_cart_post()



Creates an empty cart and quote for a guest.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartManagementV1Api()

try: 
    api_response = api_instance.quote_cart_management_v1_create_empty_cart_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartManagementV1Api->quote_cart_management_v1_create_empty_cart_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_management_v1_get_cart_for_customer_get**
> QuoteDataCartInterface quote_cart_management_v1_get_cart_for_customer_get()



Returns information for the cart for a specified customer.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartManagementV1Api()

try: 
    api_response = api_instance.quote_cart_management_v1_get_cart_for_customer_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartManagementV1Api->quote_cart_management_v1_get_cart_for_customer_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuoteDataCartInterface**](QuoteDataCartInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_management_v1_place_order_put**
> int quote_cart_management_v1_place_order_put(body=body)



Places an order for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartManagementV1Api()
body = swagger_client.Body55() # Body55 |  (optional)

try: 
    api_response = api_instance.quote_cart_management_v1_place_order_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartManagementV1Api->quote_cart_management_v1_place_order_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body55**](Body55.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_cart_management_v1_place_order_put_0**
> int quote_cart_management_v1_place_order_put_0(cart_id, body=body)



Places an order for a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCartManagementV1Api()
cart_id = 56 # int | The cart ID.
body = swagger_client.Body56() # Body56 |  (optional)

try: 
    api_response = api_instance.quote_cart_management_v1_place_order_put_0(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCartManagementV1Api->quote_cart_management_v1_place_order_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 
 **body** | [**Body56**](Body56.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

