# swagger_client.CatalogProductCustomOptionRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_custom_option_repository_v1_delete_by_identifier_delete**](CatalogProductCustomOptionRepositoryV1Api.md#catalog_product_custom_option_repository_v1_delete_by_identifier_delete) | **DELETE** /V1/products/{sku}/options/{optionId} | 
[**catalog_product_custom_option_repository_v1_get_get**](CatalogProductCustomOptionRepositoryV1Api.md#catalog_product_custom_option_repository_v1_get_get) | **GET** /V1/products/{sku}/options/{optionId} | 
[**catalog_product_custom_option_repository_v1_get_list_get**](CatalogProductCustomOptionRepositoryV1Api.md#catalog_product_custom_option_repository_v1_get_list_get) | **GET** /V1/products/{sku}/options | 
[**catalog_product_custom_option_repository_v1_save_post**](CatalogProductCustomOptionRepositoryV1Api.md#catalog_product_custom_option_repository_v1_save_post) | **POST** /V1/products/options | 
[**catalog_product_custom_option_repository_v1_save_put**](CatalogProductCustomOptionRepositoryV1Api.md#catalog_product_custom_option_repository_v1_save_put) | **PUT** /V1/products/options/{optionId} | 


# **catalog_product_custom_option_repository_v1_delete_by_identifier_delete**
> bool catalog_product_custom_option_repository_v1_delete_by_identifier_delete(sku, option_id)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductCustomOptionRepositoryV1Api()
sku = 'sku_example' # str | 
option_id = 56 # int | 

try: 
    api_response = api_instance.catalog_product_custom_option_repository_v1_delete_by_identifier_delete(sku, option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductCustomOptionRepositoryV1Api->catalog_product_custom_option_repository_v1_delete_by_identifier_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **option_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_custom_option_repository_v1_get_get**
> CatalogDataProductCustomOptionInterface catalog_product_custom_option_repository_v1_get_get(sku, option_id)



Get custom option for a specific product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductCustomOptionRepositoryV1Api()
sku = 'sku_example' # str | 
option_id = 56 # int | 

try: 
    api_response = api_instance.catalog_product_custom_option_repository_v1_get_get(sku, option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductCustomOptionRepositoryV1Api->catalog_product_custom_option_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **option_id** | **int**|  | 

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_custom_option_repository_v1_get_list_get**
> list[CatalogDataProductCustomOptionInterface] catalog_product_custom_option_repository_v1_get_list_get(sku)



Get the list of custom options for a specific product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductCustomOptionRepositoryV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.catalog_product_custom_option_repository_v1_get_list_get(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductCustomOptionRepositoryV1Api->catalog_product_custom_option_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

[**list[CatalogDataProductCustomOptionInterface]**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_custom_option_repository_v1_save_post**
> CatalogDataProductCustomOptionInterface catalog_product_custom_option_repository_v1_save_post(body=body)



Save Custom Option

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductCustomOptionRepositoryV1Api()
body = swagger_client.Body45() # Body45 |  (optional)

try: 
    api_response = api_instance.catalog_product_custom_option_repository_v1_save_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductCustomOptionRepositoryV1Api->catalog_product_custom_option_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body45**](Body45.md)|  | [optional] 

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_custom_option_repository_v1_save_put**
> CatalogDataProductCustomOptionInterface catalog_product_custom_option_repository_v1_save_put(option_id, body=body)



Save Custom Option

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductCustomOptionRepositoryV1Api()
option_id = 'option_id_example' # str | 
body = swagger_client.Body46() # Body46 |  (optional)

try: 
    api_response = api_instance.catalog_product_custom_option_repository_v1_save_put(option_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductCustomOptionRepositoryV1Api->catalog_product_custom_option_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option_id** | **str**|  | 
 **body** | [**Body46**](Body46.md)|  | [optional] 

### Return type

[**CatalogDataProductCustomOptionInterface**](CatalogDataProductCustomOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

