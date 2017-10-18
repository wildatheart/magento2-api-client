# swagger_client.CatalogProductLinkTypeListV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_link_type_list_v1_get_item_attributes_get**](CatalogProductLinkTypeListV1Api.md#catalog_product_link_type_list_v1_get_item_attributes_get) | **GET** /V1/products/links/{type}/attributes | 
[**catalog_product_link_type_list_v1_get_items_get**](CatalogProductLinkTypeListV1Api.md#catalog_product_link_type_list_v1_get_items_get) | **GET** /V1/products/links/types | 


# **catalog_product_link_type_list_v1_get_item_attributes_get**
> list[CatalogDataProductLinkAttributeInterface] catalog_product_link_type_list_v1_get_item_attributes_get(type)



Provide a list of the product link type attributes

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductLinkTypeListV1Api()
type = 'type_example' # str | 

try: 
    api_response = api_instance.catalog_product_link_type_list_v1_get_item_attributes_get(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductLinkTypeListV1Api->catalog_product_link_type_list_v1_get_item_attributes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**list[CatalogDataProductLinkAttributeInterface]**](CatalogDataProductLinkAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_link_type_list_v1_get_items_get**
> list[CatalogDataProductLinkTypeInterface] catalog_product_link_type_list_v1_get_items_get()



Retrieve information about available product link types

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductLinkTypeListV1Api()

try: 
    api_response = api_instance.catalog_product_link_type_list_v1_get_items_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductLinkTypeListV1Api->catalog_product_link_type_list_v1_get_items_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CatalogDataProductLinkTypeInterface]**](CatalogDataProductLinkTypeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

