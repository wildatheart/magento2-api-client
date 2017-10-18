# swagger_client.IntegrationCustomerTokenServiceV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integration_customer_token_service_v1_create_customer_access_token_post**](IntegrationCustomerTokenServiceV1Api.md#integration_customer_token_service_v1_create_customer_access_token_post) | **POST** /V1/integration/customer/token | 


# **integration_customer_token_service_v1_create_customer_access_token_post**
> str integration_customer_token_service_v1_create_customer_access_token_post(body=body)



Create access token for admin given the customer credentials.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationCustomerTokenServiceV1Api()
body = swagger_client.Body131() # Body131 |  (optional)

try: 
    api_response = api_instance.integration_customer_token_service_v1_create_customer_access_token_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationCustomerTokenServiceV1Api->integration_customer_token_service_v1_create_customer_access_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body131**](Body131.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

