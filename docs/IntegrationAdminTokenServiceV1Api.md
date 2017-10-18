# swagger_client.IntegrationAdminTokenServiceV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integration_admin_token_service_v1_create_admin_access_token_post**](IntegrationAdminTokenServiceV1Api.md#integration_admin_token_service_v1_create_admin_access_token_post) | **POST** /V1/integration/admin/token | 


# **integration_admin_token_service_v1_create_admin_access_token_post**
> str integration_admin_token_service_v1_create_admin_access_token_post(body=body)



Create access token for admin given the admin credentials.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.IntegrationAdminTokenServiceV1Api()
body = swagger_client.Body130() # Body130 |  (optional)

try: 
    api_response = api_instance.integration_admin_token_service_v1_create_admin_access_token_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IntegrationAdminTokenServiceV1Api->integration_admin_token_service_v1_create_admin_access_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body130**](Body130.md)|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

