# swagger_client.CatalogAttributeSetManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_attribute_set_management_v1_create_post**](CatalogAttributeSetManagementV1Api.md#catalog_attribute_set_management_v1_create_post) | **POST** /V1/products/attribute-sets | 


# **catalog_attribute_set_management_v1_create_post**
> EavDataAttributeSetInterface catalog_attribute_set_management_v1_create_post(body=body)



Create attribute set from data

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogAttributeSetManagementV1Api()
body = swagger_client.Body23() # Body23 |  (optional)

try: 
    api_response = api_instance.catalog_attribute_set_management_v1_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogAttributeSetManagementV1Api->catalog_attribute_set_management_v1_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body23**](Body23.md)|  | [optional] 

### Return type

[**EavDataAttributeSetInterface**](EavDataAttributeSetInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

