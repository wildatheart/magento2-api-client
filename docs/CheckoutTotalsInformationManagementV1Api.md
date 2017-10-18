# swagger_client.CheckoutTotalsInformationManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_totals_information_management_v1_calculate_post**](CheckoutTotalsInformationManagementV1Api.md#checkout_totals_information_management_v1_calculate_post) | **POST** /V1/carts/{cartId}/totals-information | 
[**checkout_totals_information_management_v1_calculate_post_0**](CheckoutTotalsInformationManagementV1Api.md#checkout_totals_information_management_v1_calculate_post_0) | **POST** /V1/carts/mine/totals-information | 


# **checkout_totals_information_management_v1_calculate_post**
> QuoteDataTotalsInterface checkout_totals_information_management_v1_calculate_post(cart_id, body=body)



Calculate quote totals based on address and shipping method.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutTotalsInformationManagementV1Api()
cart_id = 56 # int | 
body = swagger_client.Body112() # Body112 |  (optional)

try: 
    api_response = api_instance.checkout_totals_information_management_v1_calculate_post(cart_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutTotalsInformationManagementV1Api->checkout_totals_information_management_v1_calculate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**|  | 
 **body** | [**Body112**](Body112.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **checkout_totals_information_management_v1_calculate_post_0**
> QuoteDataTotalsInterface checkout_totals_information_management_v1_calculate_post_0(body=body)



Calculate quote totals based on address and shipping method.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutTotalsInformationManagementV1Api()
body = swagger_client.Body113() # Body113 |  (optional)

try: 
    api_response = api_instance.checkout_totals_information_management_v1_calculate_post_0(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutTotalsInformationManagementV1Api->checkout_totals_information_management_v1_calculate_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body113**](Body113.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

