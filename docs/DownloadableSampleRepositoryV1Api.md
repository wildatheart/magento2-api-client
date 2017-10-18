# swagger_client.DownloadableSampleRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadable_sample_repository_v1_delete_delete**](DownloadableSampleRepositoryV1Api.md#downloadable_sample_repository_v1_delete_delete) | **DELETE** /V1/products/downloadable-links/samples/{id} | 
[**downloadable_sample_repository_v1_get_list_get**](DownloadableSampleRepositoryV1Api.md#downloadable_sample_repository_v1_get_list_get) | **GET** /V1/products/{sku}/downloadable-links/samples | 
[**downloadable_sample_repository_v1_save_post**](DownloadableSampleRepositoryV1Api.md#downloadable_sample_repository_v1_save_post) | **POST** /V1/products/{sku}/downloadable-links/samples | 
[**downloadable_sample_repository_v1_save_put**](DownloadableSampleRepositoryV1Api.md#downloadable_sample_repository_v1_save_put) | **PUT** /V1/products/{sku}/downloadable-links/samples/{id} | 


# **downloadable_sample_repository_v1_delete_delete**
> bool downloadable_sample_repository_v1_delete_delete(id)



Delete downloadable sample

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableSampleRepositoryV1Api()
id = 56 # int | 

try: 
    api_response = api_instance.downloadable_sample_repository_v1_delete_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableSampleRepositoryV1Api->downloadable_sample_repository_v1_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **downloadable_sample_repository_v1_get_list_get**
> list[DownloadableDataSampleInterface] downloadable_sample_repository_v1_get_list_get(sku)



List of samples for downloadable product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableSampleRepositoryV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.downloadable_sample_repository_v1_get_list_get(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableSampleRepositoryV1Api->downloadable_sample_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

[**list[DownloadableDataSampleInterface]**](DownloadableDataSampleInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **downloadable_sample_repository_v1_save_post**
> int downloadable_sample_repository_v1_save_post(sku, body=body)



Update downloadable sample of the given product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableSampleRepositoryV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body85() # Body85 |  (optional)

try: 
    api_response = api_instance.downloadable_sample_repository_v1_save_post(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableSampleRepositoryV1Api->downloadable_sample_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body85**](Body85.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **downloadable_sample_repository_v1_save_put**
> int downloadable_sample_repository_v1_save_put(sku, id, body=body)



Update downloadable sample of the given product

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableSampleRepositoryV1Api()
sku = 'sku_example' # str | 
id = 'id_example' # str | 
body = swagger_client.Body86() # Body86 |  (optional)

try: 
    api_response = api_instance.downloadable_sample_repository_v1_save_put(sku, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableSampleRepositoryV1Api->downloadable_sample_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Body86**](Body86.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

