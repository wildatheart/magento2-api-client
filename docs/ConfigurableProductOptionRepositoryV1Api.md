# swagger_client.ConfigurableProductOptionRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configurable_product_option_repository_v1_delete_by_id_delete**](ConfigurableProductOptionRepositoryV1Api.md#configurable_product_option_repository_v1_delete_by_id_delete) | **DELETE** /V1/configurable-products/{sku}/options/{id} | 
[**configurable_product_option_repository_v1_get_get**](ConfigurableProductOptionRepositoryV1Api.md#configurable_product_option_repository_v1_get_get) | **GET** /V1/configurable-products/{sku}/options/{id} | 
[**configurable_product_option_repository_v1_get_list_get**](ConfigurableProductOptionRepositoryV1Api.md#configurable_product_option_repository_v1_get_list_get) | **GET** /V1/configurable-products/{sku}/options/all | 
[**configurable_product_option_repository_v1_save_post**](ConfigurableProductOptionRepositoryV1Api.md#configurable_product_option_repository_v1_save_post) | **POST** /V1/configurable-products/{sku}/options | 
[**configurable_product_option_repository_v1_save_put**](ConfigurableProductOptionRepositoryV1Api.md#configurable_product_option_repository_v1_save_put) | **PUT** /V1/configurable-products/{sku}/options/{id} | 


# **configurable_product_option_repository_v1_delete_by_id_delete**
> bool configurable_product_option_repository_v1_delete_by_id_delete(sku, id)



Remove option from configurable product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 
id = 56 # int | 

try: 
    api_response = api_instance.configurable_product_option_repository_v1_delete_by_id_delete(sku, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductOptionRepositoryV1Api->configurable_product_option_repository_v1_delete_by_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurable_product_option_repository_v1_get_get**
> ConfigurableProductDataOptionInterface configurable_product_option_repository_v1_get_get(sku, id)



Get option for configurable product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 
id = 56 # int | 

try: 
    api_response = api_instance.configurable_product_option_repository_v1_get_get(sku, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductOptionRepositoryV1Api->configurable_product_option_repository_v1_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **id** | **int**|  | 

### Return type

[**ConfigurableProductDataOptionInterface**](ConfigurableProductDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurable_product_option_repository_v1_get_list_get**
> list[ConfigurableProductDataOptionInterface] configurable_product_option_repository_v1_get_list_get(sku)



Get all options for configurable product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.configurable_product_option_repository_v1_get_list_get(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductOptionRepositoryV1Api->configurable_product_option_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

[**list[ConfigurableProductDataOptionInterface]**](ConfigurableProductDataOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurable_product_option_repository_v1_save_post**
> int configurable_product_option_repository_v1_save_post(sku, body=body)



Save option

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body122() # Body122 |  (optional)

try: 
    api_response = api_instance.configurable_product_option_repository_v1_save_post(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductOptionRepositoryV1Api->configurable_product_option_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body122**](Body122.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configurable_product_option_repository_v1_save_put**
> int configurable_product_option_repository_v1_save_put(sku, id, body=body)



Save option

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ConfigurableProductOptionRepositoryV1Api()
sku = 'sku_example' # str | 
id = 'id_example' # str | 
body = swagger_client.Body121() # Body121 |  (optional)

try: 
    api_response = api_instance.configurable_product_option_repository_v1_save_put(sku, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurableProductOptionRepositoryV1Api->configurable_product_option_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Body121**](Body121.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

