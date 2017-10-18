# swagger_client.CatalogProductLinkRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_link_repository_v1_delete_by_id_delete**](CatalogProductLinkRepositoryV1Api.md#catalog_product_link_repository_v1_delete_by_id_delete) | **DELETE** /V1/products/{sku}/links/{type}/{linkedProductSku} | 
[**catalog_product_link_repository_v1_save_put**](CatalogProductLinkRepositoryV1Api.md#catalog_product_link_repository_v1_save_put) | **PUT** /V1/products/{sku}/links | 


# **catalog_product_link_repository_v1_delete_by_id_delete**
> bool catalog_product_link_repository_v1_delete_by_id_delete(sku, type, linked_product_sku)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductLinkRepositoryV1Api()
sku = 'sku_example' # str | 
type = 'type_example' # str | 
linked_product_sku = 'linked_product_sku_example' # str | 

try: 
    api_response = api_instance.catalog_product_link_repository_v1_delete_by_id_delete(sku, type, linked_product_sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductLinkRepositoryV1Api->catalog_product_link_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **type** | **str**|  | 
 **linked_product_sku** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_link_repository_v1_save_put**
> bool catalog_product_link_repository_v1_save_put(sku, body=body)



Save product link

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductLinkRepositoryV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body47() # Body47 |  (optional)

try: 
    api_response = api_instance.catalog_product_link_repository_v1_save_put(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductLinkRepositoryV1Api->catalog_product_link_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body47**](Body47.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

