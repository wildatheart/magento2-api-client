# swagger_client.CatalogProductLinkManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_link_management_v1_get_linked_items_by_type_get**](CatalogProductLinkManagementV1Api.md#catalog_product_link_management_v1_get_linked_items_by_type_get) | **GET** /V1/products/{sku}/links/{type} | 
[**catalog_product_link_management_v1_set_product_links_post**](CatalogProductLinkManagementV1Api.md#catalog_product_link_management_v1_set_product_links_post) | **POST** /V1/products/{sku}/links | 


# **catalog_product_link_management_v1_get_linked_items_by_type_get**
> list[CatalogDataProductLinkInterface] catalog_product_link_management_v1_get_linked_items_by_type_get(sku, type)



Provide the list of links for a specific product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductLinkManagementV1Api()
sku = 'sku_example' # str | 
type = 'type_example' # str | 

try: 
    api_response = api_instance.catalog_product_link_management_v1_get_linked_items_by_type_get(sku, type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductLinkManagementV1Api->catalog_product_link_management_v1_get_linked_items_by_type_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **type** | **str**|  | 

### Return type

[**list[CatalogDataProductLinkInterface]**](CatalogDataProductLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_link_management_v1_set_product_links_post**
> bool catalog_product_link_management_v1_set_product_links_post(sku, body=body)



Assign a product link to another product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductLinkManagementV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body48() # Body48 |  (optional)

try: 
    api_response = api_instance.catalog_product_link_management_v1_set_product_links_post(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductLinkManagementV1Api->catalog_product_link_management_v1_set_product_links_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body48**](Body48.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

