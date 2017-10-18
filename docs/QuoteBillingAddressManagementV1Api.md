# swagger_client.QuoteBillingAddressManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quote_billing_address_management_v1_assign_post**](QuoteBillingAddressManagementV1Api.md#quote_billing_address_management_v1_assign_post) | **POST** /V1/carts/{cartId}/billing-address | 
[**quote_billing_address_management_v1_assign_post_0**](QuoteBillingAddressManagementV1Api.md#quote_billing_address_management_v1_assign_post_0) | **POST** /V1/carts/mine/billing-address | 
[**quote_billing_address_management_v1_get_get**](QuoteBillingAddressManagementV1Api.md#quote_billing_address_management_v1_get_get) | **GET** /V1/carts/{cartId}/billing-address | 
[**quote_billing_address_management_v1_get_get_0**](QuoteBillingAddressManagementV1Api.md#quote_billing_address_management_v1_get_get_0) | **GET** /V1/carts/mine/billing-address | 


# **quote_billing_address_management_v1_assign_post**
> int quote_billing_address_management_v1_assign_post(cart_id, body=body)



Assigns a specified billing address to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteBillingAddressManagementV1Api()
cart_id = 56 # int | The cart ID.
body = swagger_client.Body73() # Body73 |  (optional)

try: 
    api_response = api_instance.quote_billing_address_management_v1_assign_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteBillingAddressManagementV1Api->quote_billing_address_management_v1_assign_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 
 **body** | [**Body73**](Body73.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_billing_address_management_v1_assign_post_0**
> int quote_billing_address_management_v1_assign_post_0(body=body)



Assigns a specified billing address to a specified cart.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteBillingAddressManagementV1Api()
body = swagger_client.Body74() # Body74 |  (optional)

try: 
    api_response = api_instance.quote_billing_address_management_v1_assign_post_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteBillingAddressManagementV1Api->quote_billing_address_management_v1_assign_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body74**](Body74.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_billing_address_management_v1_get_get**
> QuoteDataAddressInterface quote_billing_address_management_v1_get_get(cart_id)



Returns the billing address for a specified quote.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteBillingAddressManagementV1Api()
cart_id = 56 # int | The cart ID.

try: 
    api_response = api_instance.quote_billing_address_management_v1_get_get(cart_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteBillingAddressManagementV1Api->quote_billing_address_management_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| The cart ID. | 

### Return type

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_billing_address_management_v1_get_get_0**
> QuoteDataAddressInterface quote_billing_address_management_v1_get_get_0()



Returns the billing address for a specified quote.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.QuoteBillingAddressManagementV1Api()

try: 
    api_response = api_instance.quote_billing_address_management_v1_get_get_0()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QuoteBillingAddressManagementV1Api->quote_billing_address_management_v1_get_get_0: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuoteDataAddressInterface**](QuoteDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

