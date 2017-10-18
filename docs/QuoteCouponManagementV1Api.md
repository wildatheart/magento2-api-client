# swagger_client.QuoteCouponManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_coupon_management_v1_get_get**](QuoteCouponManagementV1Api.md#quote_coupon_management_v1_get_get) | **GET** /V1/carts/{cartId}/coupons | 
[**quote_coupon_management_v1_get_get_0**](QuoteCouponManagementV1Api.md#quote_coupon_management_v1_get_get_0) | **GET** /V1/carts/mine/coupons | 
[**quote_coupon_management_v1_remove_delete**](QuoteCouponManagementV1Api.md#quote_coupon_management_v1_remove_delete) | **DELETE** /V1/carts/{cartId}/coupons | 
[**quote_coupon_management_v1_remove_delete_0**](QuoteCouponManagementV1Api.md#quote_coupon_management_v1_remove_delete_0) | **DELETE** /V1/carts/mine/coupons | 
[**quote_coupon_management_v1_set_put**](QuoteCouponManagementV1Api.md#quote_coupon_management_v1_set_put) | **PUT** /V1/carts/{cartId}/coupons/{couponCode} | 
[**quote_coupon_management_v1_set_put_0**](QuoteCouponManagementV1Api.md#quote_coupon_management_v1_set_put_0) | **PUT** /V1/carts/mine/coupons/{couponCode} | 


# **quote_coupon_management_v1_get_get**
> str quote_coupon_management_v1_get_get(cart_id)



Returns information for a coupon in a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCouponManagementV1Api()
cart_id = 56 # int | The cart ID.

try: 
    api_response = api_instance.quote_coupon_management_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCouponManagementV1Api->quote_coupon_management_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_coupon_management_v1_get_get_0**
> str quote_coupon_management_v1_get_get_0()



Returns information for a coupon in a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCouponManagementV1Api()

try: 
    api_response = api_instance.quote_coupon_management_v1_get_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCouponManagementV1Api->quote_coupon_management_v1_get_get_0: %s\n" % e)
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

# **quote_coupon_management_v1_remove_delete**
> bool quote_coupon_management_v1_remove_delete(cart_id)



Deletes a coupon from a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCouponManagementV1Api()
cart_id = 56 # int | The cart ID.

try: 
    api_response = api_instance.quote_coupon_management_v1_remove_delete(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCouponManagementV1Api->quote_coupon_management_v1_remove_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_coupon_management_v1_remove_delete_0**
> bool quote_coupon_management_v1_remove_delete_0()



Deletes a coupon from a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCouponManagementV1Api()

try: 
    api_response = api_instance.quote_coupon_management_v1_remove_delete_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCouponManagementV1Api->quote_coupon_management_v1_remove_delete_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_coupon_management_v1_set_put**
> bool quote_coupon_management_v1_set_put(cart_id, coupon_code)



Adds a coupon by code to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCouponManagementV1Api()
cart_id = 56 # int | The cart ID.
coupon_code = 'coupon_code_example' # str | The coupon code data.

try: 
    api_response = api_instance.quote_coupon_management_v1_set_put(cart_id, coupon_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCouponManagementV1Api->quote_coupon_management_v1_set_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 
 **coupon_code** | **str**| The coupon code data. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_coupon_management_v1_set_put_0**
> bool quote_coupon_management_v1_set_put_0(coupon_code)



Adds a coupon by code to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteCouponManagementV1Api()
coupon_code = 'coupon_code_example' # str | The coupon code data.

try: 
    api_response = api_instance.quote_coupon_management_v1_set_put_0(coupon_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteCouponManagementV1Api->quote_coupon_management_v1_set_put_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**| The coupon code data. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

