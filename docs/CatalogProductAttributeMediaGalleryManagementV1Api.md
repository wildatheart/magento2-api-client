# swagger_client.CatalogProductAttributeMediaGalleryManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_attribute_media_gallery_management_v1_create_post**](CatalogProductAttributeMediaGalleryManagementV1Api.md#catalog_product_attribute_media_gallery_management_v1_create_post) | **POST** /V1/products/{sku}/media | 
[**catalog_product_attribute_media_gallery_management_v1_get_get**](CatalogProductAttributeMediaGalleryManagementV1Api.md#catalog_product_attribute_media_gallery_management_v1_get_get) | **GET** /V1/products/{sku}/media/{entryId} | 
[**catalog_product_attribute_media_gallery_management_v1_get_list_get**](CatalogProductAttributeMediaGalleryManagementV1Api.md#catalog_product_attribute_media_gallery_management_v1_get_list_get) | **GET** /V1/products/{sku}/media | 
[**catalog_product_attribute_media_gallery_management_v1_remove_delete**](CatalogProductAttributeMediaGalleryManagementV1Api.md#catalog_product_attribute_media_gallery_management_v1_remove_delete) | **DELETE** /V1/products/{sku}/media/{entryId} | 
[**catalog_product_attribute_media_gallery_management_v1_update_put**](CatalogProductAttributeMediaGalleryManagementV1Api.md#catalog_product_attribute_media_gallery_management_v1_update_put) | **PUT** /V1/products/{sku}/media/{entryId} | 


# **catalog_product_attribute_media_gallery_management_v1_create_post**
> int catalog_product_attribute_media_gallery_management_v1_create_post(sku, body=body)



Create new gallery entry

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeMediaGalleryManagementV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body29() # Body29 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_media_gallery_management_v1_create_post(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeMediaGalleryManagementV1Api->catalog_product_attribute_media_gallery_management_v1_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body29**](Body29.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_media_gallery_management_v1_get_get**
> CatalogDataProductAttributeMediaGalleryEntryInterface catalog_product_attribute_media_gallery_management_v1_get_get(sku, entry_id)



Return information about gallery entry

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeMediaGalleryManagementV1Api()
sku = 'sku_example' # str | 
entry_id = 56 # int | 

try: 
    api_response = api_instance.catalog_product_attribute_media_gallery_management_v1_get_get(sku, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeMediaGalleryManagementV1Api->catalog_product_attribute_media_gallery_management_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **entry_id** | **int**|  | 

### Return type

[**CatalogDataProductAttributeMediaGalleryEntryInterface**](CatalogDataProductAttributeMediaGalleryEntryInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_media_gallery_management_v1_get_list_get**
> list[CatalogDataProductAttributeMediaGalleryEntryInterface] catalog_product_attribute_media_gallery_management_v1_get_list_get(sku)



Retrieve the list of gallery entries associated with given product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeMediaGalleryManagementV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.catalog_product_attribute_media_gallery_management_v1_get_list_get(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeMediaGalleryManagementV1Api->catalog_product_attribute_media_gallery_management_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

[**list[CatalogDataProductAttributeMediaGalleryEntryInterface]**](CatalogDataProductAttributeMediaGalleryEntryInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_media_gallery_management_v1_remove_delete**
> bool catalog_product_attribute_media_gallery_management_v1_remove_delete(sku, entry_id)



Remove gallery entry

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeMediaGalleryManagementV1Api()
sku = 'sku_example' # str | 
entry_id = 56 # int | 

try: 
    api_response = api_instance.catalog_product_attribute_media_gallery_management_v1_remove_delete(sku, entry_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeMediaGalleryManagementV1Api->catalog_product_attribute_media_gallery_management_v1_remove_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **entry_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_media_gallery_management_v1_update_put**
> bool catalog_product_attribute_media_gallery_management_v1_update_put(sku, entry_id, body=body)



Update gallery entry

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeMediaGalleryManagementV1Api()
sku = 'sku_example' # str | 
entry_id = 'entry_id_example' # str | 
body = swagger_client.Body28() # Body28 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_media_gallery_management_v1_update_put(sku, entry_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeMediaGalleryManagementV1Api->catalog_product_attribute_media_gallery_management_v1_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **entry_id** | **str**|  | 
 **body** | [**Body28**](Body28.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

