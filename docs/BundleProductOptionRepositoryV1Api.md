# swagger_client.BundleProductOptionRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bundle_product_option_repository_v1_delete_by_id_delete**](BundleProductOptionRepositoryV1Api.md#bundle_product_option_repository_v1_delete_by_id_delete) | **DELETE** /V1/bundle-products/{sku}/options/{optionId} | 
[**bundle_product_option_repository_v1_get_get**](BundleProductOptionRepositoryV1Api.md#bundle_product_option_repository_v1_get_get) | **GET** /V1/bundle-products/{sku}/options/{optionId} | 
[**bundle_product_option_repository_v1_get_list_get**](BundleProductOptionRepositoryV1Api.md#bundle_product_option_repository_v1_get_list_get) | **GET** /V1/bundle-products/{sku}/options/all | 


# **bundle_product_option_repository_v1_delete_by_id_delete**
> bool bundle_product_option_repository_v1_delete_by_id_delete(sku, option_id)



Remove bundle option

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 
option_id = 56 # int | 

try: 
    api_response = api_instance.bundle_product_option_repository_v1_delete_by_id_delete(sku, option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductOptionRepositoryV1Api->bundle_product_option_repository_v1_delete_by_id_delete: %s\n" % e)
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

# **bundle_product_option_repository_v1_get_get**
> BundleDataOptionInterface bundle_product_option_repository_v1_get_get(sku, option_id)



Get option for bundle product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 
option_id = 56 # int | 

try: 
    api_response = api_instance.bundle_product_option_repository_v1_get_get(sku, option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductOptionRepositoryV1Api->bundle_product_option_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **option_id** | **int**|  | 

### Return type

[**BundleDataOptionInterface**](BundleDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bundle_product_option_repository_v1_get_list_get**
> list[BundleDataOptionInterface] bundle_product_option_repository_v1_get_list_get(sku)



Get all options for bundle product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BundleProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.bundle_product_option_repository_v1_get_list_get(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BundleProductOptionRepositoryV1Api->bundle_product_option_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

[**list[BundleDataOptionInterface]**](BundleDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

