# swagger_client.QuoteGuestCouponManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_guest_coupon_management_v1_get_get**](QuoteGuestCouponManagementV1Api.md#quote_guest_coupon_management_v1_get_get) | **GET** /V1/guest-carts/{cartId}/coupons | 
[**quote_guest_coupon_management_v1_remove_delete**](QuoteGuestCouponManagementV1Api.md#quote_guest_coupon_management_v1_remove_delete) | **DELETE** /V1/guest-carts/{cartId}/coupons | 
[**quote_guest_coupon_management_v1_set_put**](QuoteGuestCouponManagementV1Api.md#quote_guest_coupon_management_v1_set_put) | **PUT** /V1/guest-carts/{cartId}/coupons/{couponCode} | 


# **quote_guest_coupon_management_v1_get_get**
> str quote_guest_coupon_management_v1_get_get(cart_id)



Return information for a coupon in a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCouponManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.

try: 
    api_response = api_instance.quote_guest_coupon_management_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCouponManagementV1Api->quote_guest_coupon_management_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_coupon_management_v1_remove_delete**
> bool quote_guest_coupon_management_v1_remove_delete(cart_id)



Delete a coupon from a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCouponManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.

try: 
    api_response = api_instance.quote_guest_coupon_management_v1_remove_delete(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCouponManagementV1Api->quote_guest_coupon_management_v1_remove_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_guest_coupon_management_v1_set_put**
> bool quote_guest_coupon_management_v1_set_put(cart_id, coupon_code)



Add a coupon by code to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteGuestCouponManagementV1Api()
cart_id = 'cart_id_example' # str | The cart ID.
coupon_code = 'coupon_code_example' # str | The coupon code data.

try: 
    api_response = api_instance.quote_guest_coupon_management_v1_set_put(cart_id, coupon_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteGuestCouponManagementV1Api->quote_guest_coupon_management_v1_set_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **str**| The cart ID. | 
 **coupon_code** | **str**| The coupon code data. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

