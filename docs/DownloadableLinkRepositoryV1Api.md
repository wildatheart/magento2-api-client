# swagger_client.DownloadableLinkRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadable_link_repository_v1_delete_delete**](DownloadableLinkRepositoryV1Api.md#downloadable_link_repository_v1_delete_delete) | **DELETE** /V1/products/downloadable-links/{id} | 
[**downloadable_link_repository_v1_get_list_get**](DownloadableLinkRepositoryV1Api.md#downloadable_link_repository_v1_get_list_get) | **GET** /V1/products/{sku}/downloadable-links | 
[**downloadable_link_repository_v1_save_post**](DownloadableLinkRepositoryV1Api.md#downloadable_link_repository_v1_save_post) | **POST** /V1/products/{sku}/downloadable-links | 
[**downloadable_link_repository_v1_save_put**](DownloadableLinkRepositoryV1Api.md#downloadable_link_repository_v1_save_put) | **PUT** /V1/products/{sku}/downloadable-links/{id} | 


# **downloadable_link_repository_v1_delete_delete**
> bool downloadable_link_repository_v1_delete_delete(id)



Delete downloadable link

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableLinkRepositoryV1Api()
id = 56 # int | 

try: 
    api_response = api_instance.downloadable_link_repository_v1_delete_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableLinkRepositoryV1Api->downloadable_link_repository_v1_delete_delete: %s\n" % e)
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

# **downloadable_link_repository_v1_get_list_get**
> list[DownloadableDataLinkInterface] downloadable_link_repository_v1_get_list_get(sku)



List of links with associated samples

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableLinkRepositoryV1Api()
sku = 'sku_example' # str | 

try: 
    api_response = api_instance.downloadable_link_repository_v1_get_list_get(sku)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableLinkRepositoryV1Api->downloadable_link_repository_v1_get_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 

### Return type

[**list[DownloadableDataLinkInterface]**](DownloadableDataLinkInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **downloadable_link_repository_v1_save_post**
> int downloadable_link_repository_v1_save_post(sku, body=body)



Update downloadable link of the given product (link type and its resources cannot be changed)

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableLinkRepositoryV1Api()
sku = 'sku_example' # str | 
body = swagger_client.Body83() # Body83 |  (optional)

try: 
    api_response = api_instance.downloadable_link_repository_v1_save_post(sku, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableLinkRepositoryV1Api->downloadable_link_repository_v1_save_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **body** | [**Body83**](Body83.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **downloadable_link_repository_v1_save_put**
> int downloadable_link_repository_v1_save_put(sku, id, body=body)



Update downloadable link of the given product (link type and its resources cannot be changed)

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadableLinkRepositoryV1Api()
sku = 'sku_example' # str | 
id = 'id_example' # str | 
body = swagger_client.Body84() # Body84 |  (optional)

try: 
    api_response = api_instance.downloadable_link_repository_v1_save_put(sku, id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadableLinkRepositoryV1Api->downloadable_link_repository_v1_save_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sku** | **str**|  | 
 **id** | **str**|  | 
 **body** | [**Body84**](Body84.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

