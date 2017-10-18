# swagger_client.QuoteShippingMethodManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_shipping_method_management_v1_estimate_by_address_id_post**](QuoteShippingMethodManagementV1Api.md#quote_shipping_method_management_v1_estimate_by_address_id_post) | **POST** /V1/carts/{cartId}/estimate-shipping-methods-by-address-id | 
[**quote_shipping_method_management_v1_estimate_by_address_id_post_0**](QuoteShippingMethodManagementV1Api.md#quote_shipping_method_management_v1_estimate_by_address_id_post_0) | **POST** /V1/carts/mine/estimate-shipping-methods-by-address-id | 
[**quote_shipping_method_management_v1_get_list_get**](QuoteShippingMethodManagementV1Api.md#quote_shipping_method_management_v1_get_list_get) | **GET** /V1/carts/{cartId}/shipping-methods | 
[**quote_shipping_method_management_v1_get_list_get_0**](QuoteShippingMethodManagementV1Api.md#quote_shipping_method_management_v1_get_list_get_0) | **GET** /V1/carts/mine/shipping-methods | 


# **quote_shipping_method_management_v1_estimate_by_address_id_post**
> list[QuoteDataShippingMethodInterface] quote_shipping_method_management_v1_estimate_by_address_id_post(cart_id, body=body)



Estimate shipping

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteShippingMethodManagementV1Api()
cart_id = 56 # int | The shopping cart ID.
body = swagger_client.Body59() # Body59 |  (optional)

try: 
    api_response = api_instance.quote_shipping_method_management_v1_estimate_by_address_id_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteShippingMethodManagementV1Api->quote_shipping_method_management_v1_estimate_by_address_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The shopping cart ID. | 
 **body** | [**Body59**](Body59.md)|  | [optional] 

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_shipping_method_management_v1_estimate_by_address_id_post_0**
> list[QuoteDataShippingMethodInterface] quote_shipping_method_management_v1_estimate_by_address_id_post_0(body=body)



Estimate shipping

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteShippingMethodManagementV1Api()
body = swagger_client.Body60() # Body60 |  (optional)

try: 
    api_response = api_instance.quote_shipping_method_management_v1_estimate_by_address_id_post_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteShippingMethodManagementV1Api->quote_shipping_method_management_v1_estimate_by_address_id_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body60**](Body60.md)|  | [optional] 

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_shipping_method_management_v1_get_list_get**
> list[QuoteDataShippingMethodInterface] quote_shipping_method_management_v1_get_list_get(cart_id)



Lists applicable shipping methods for a specified quote.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteShippingMethodManagementV1Api()
cart_id = 56 # int | The shopping cart ID.

try: 
    api_response = api_instance.quote_shipping_method_management_v1_get_list_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteShippingMethodManagementV1Api->quote_shipping_method_management_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The shopping cart ID. | 

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_shipping_method_management_v1_get_list_get_0**
> list[QuoteDataShippingMethodInterface] quote_shipping_method_management_v1_get_list_get_0()



Lists applicable shipping methods for a specified quote.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteShippingMethodManagementV1Api()

try: 
    api_response = api_instance.quote_shipping_method_management_v1_get_list_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteShippingMethodManagementV1Api->quote_shipping_method_management_v1_get_list_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QuoteDataShippingMethodInterface]**](QuoteDataShippingMethodInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

