# swagger_client.ConfigurableProductLinkManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurable_product_link_management_v1_add_child_post**](ConfigurableProductLinkManagementV1Api.md#configurable_product_link_management_v1_add_child_post) | **POST** /V1/configurable-products/{sku}/child | 
[**configurable_product_link_management_v1_get_children_get**](ConfigurableProductLinkManagementV1Api.md#configurable_product_link_management_v1_get_children_get) | **GET** /V1/configurable-products/{sku}/children | 
[**configurable_product_link_management_v1_remove_child_delete**](ConfigurableProductLinkManagementV1Api.md#configurable_product_link_management_v1_remove_child_delete) | **DELETE** /V1/configurable-products/{sku}/children/{childSku} | 


# **configurable_product_link_management_v1_add_child_post**
> bool configurable_product_link_management_v1_add_child_post(sku, body=body)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductLinkManagementV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body119() # Body119 |  (optional)

try: 
    api_response = api_instance.configurable_product_link_management_v1_add_child_post(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductLinkManagementV1Api->configurable_product_link_management_v1_add_child_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body119**](Body119.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurable_product_link_management_v1_get_children_get**
> list[CatalogDataProductInterface] configurable_product_link_management_v1_get_children_get(sku)



Get all children for Configurable product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductLinkManagementV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.configurable_product_link_management_v1_get_children_get(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductLinkManagementV1Api->configurable_product_link_management_v1_get_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

[**list[CatalogDataProductInterface]**](CatalogDataProductInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurable_product_link_management_v1_remove_child_delete**
> bool configurable_product_link_management_v1_remove_child_delete(sku, child_sku)



Remove configurable product option

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductLinkManagementV1Api()
sku = 'sku_example' # str | 
child_sku = 'child_sku_example' # str | 

try: 
    api_response = api_instance.configurable_product_link_management_v1_remove_child_delete(sku, child_sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductLinkManagementV1Api->configurable_product_link_management_v1_remove_child_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **child_sku** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

