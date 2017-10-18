# swagger_client.ConfigurableProductConfigurableProductManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurable_product_configurable_product_management_v1_generate_variation_put**](ConfigurableProductConfigurableProductManagementV1Api.md#configurable_product_configurable_product_management_v1_generate_variation_put) | **PUT** /V1/configurable-products/variation | 


# **configurable_product_configurable_product_management_v1_generate_variation_put**
> list[CatalogDataProductInterface] configurable_product_configurable_product_management_v1_generate_variation_put(body=body)



Generate variation based on same product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductConfigurableProductManagementV1Api()
body = swagger_client.Body120() # Body120 |  (optional)

try: 
    api_response = api_instance.configurable_product_configurable_product_management_v1_generate_variation_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductConfigurableProductManagementV1Api->configurable_product_configurable_product_management_v1_generate_variation_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body120**](Body120.md)|  | [optional] 

### Return type

[**list[CatalogDataProductInterface]**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

