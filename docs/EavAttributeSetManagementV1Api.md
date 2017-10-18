# swagger_client.EavAttributeSetManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**eav_attribute_set_management_v1_create_post**](EavAttributeSetManagementV1Api.md#eav_attribute_set_management_v1_create_post) | **POST** /V1/eav/attribute-sets | 


# **eav_attribute_set_management_v1_create_post**
> EavDataAttributeSetInterface eav_attribute_set_management_v1_create_post(body=body)



Create attribute set from data

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EavAttributeSetManagementV1Api()
body = swagger_client.Body1() # Body1 |  (optional)

try: 
    api_response = api_instance.eav_attribute_set_management_v1_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EavAttributeSetManagementV1Api->eav_attribute_set_management_v1_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

