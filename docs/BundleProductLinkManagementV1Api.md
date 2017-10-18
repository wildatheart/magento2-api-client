# swagger_client.BundleProductLinkManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_product_link_management_v1_add_child_by_product_sku_post**](BundleProductLinkManagementV1Api.md#bundle_product_link_management_v1_add_child_by_product_sku_post) | **POST** /V1/bundle-products/{sku}/links/{optionId} | 
[**bundle_product_link_management_v1_get_children_get**](BundleProductLinkManagementV1Api.md#bundle_product_link_management_v1_get_children_get) | **GET** /V1/bundle-products/{productSku}/children | 
[**bundle_product_link_management_v1_remove_child_delete**](BundleProductLinkManagementV1Api.md#bundle_product_link_management_v1_remove_child_delete) | **DELETE** /V1/bundle-products/{sku}/options/{optionId}/children/{childSku} | 
[**bundle_product_link_management_v1_save_child_put**](BundleProductLinkManagementV1Api.md#bundle_product_link_management_v1_save_child_put) | **PUT** /V1/bundle-products/{sku}/links/{id} | 


# **bundle_product_link_management_v1_add_child_by_product_sku_post**
> int bundle_product_link_management_v1_add_child_by_product_sku_post(sku, option_id, body=body)



Add child product to specified Bundle option by product sku

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductLinkManagementV1Api()
sku = 'sku_example' # str | 
option_id = 56 # int | 
body = swagger_client.Body79() # Body79 |  (optional)

try: 
    api_response = api_instance.bundle_product_link_management_v1_add_child_by_product_sku_post(sku, option_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductLinkManagementV1Api->bundle_product_link_management_v1_add_child_by_product_sku_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **option_id** | **int**|  | 
 **body** | [**Body79**](Body79.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_product_link_management_v1_get_children_get**
> list[BundleDataLinkInterface] bundle_product_link_management_v1_get_children_get(product_sku, option_id=option_id)



Get all children for Bundle product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductLinkManagementV1Api()
product_sku = 'product_sku_example' # str | 
option_id = 56 # int |  (optional)

try: 
    api_response = api_instance.bundle_product_link_management_v1_get_children_get(product_sku, option_id=option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductLinkManagementV1Api->bundle_product_link_management_v1_get_children_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_sku** | **str**|  | 
 **option_id** | **int**|  | [optional] 

### Return type

[**list[BundleDataLinkInterface]**](BundleDataLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_product_link_management_v1_remove_child_delete**
> bool bundle_product_link_management_v1_remove_child_delete(sku, option_id, child_sku)



Remove product from Bundle product option

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductLinkManagementV1Api()
sku = 'sku_example' # str | 
option_id = 56 # int | 
child_sku = 'child_sku_example' # str | 

try: 
    api_response = api_instance.bundle_product_link_management_v1_remove_child_delete(sku, option_id, child_sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductLinkManagementV1Api->bundle_product_link_management_v1_remove_child_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **option_id** | **int**|  | 
 **child_sku** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_product_link_management_v1_save_child_put**
> bool bundle_product_link_management_v1_save_child_put(sku, id, body=body)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductLinkManagementV1Api()
sku = 'sku_example' # str | 
id = 'id_example' # str | 
body = swagger_client.Body80() # Body80 |  (optional)

try: 
    api_response = api_instance.bundle_product_link_management_v1_save_child_put(sku, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductLinkManagementV1Api->bundle_product_link_management_v1_save_child_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Body80**](Body80.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

