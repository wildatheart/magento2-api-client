# swagger_client.CatalogCostStorageV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_cost_storage_v1_delete_post**](CatalogCostStorageV1Api.md#catalog_cost_storage_v1_delete_post) | **POST** /V1/products/cost-delete | 
[**catalog_cost_storage_v1_get_post**](CatalogCostStorageV1Api.md#catalog_cost_storage_v1_get_post) | **POST** /V1/products/cost-information | 
[**catalog_cost_storage_v1_update_post**](CatalogCostStorageV1Api.md#catalog_cost_storage_v1_update_post) | **POST** /V1/products/cost | 


# **catalog_cost_storage_v1_delete_post**
> bool catalog_cost_storage_v1_delete_post(body=body)



Delete product cost. In case of at least one of skus is not found exception will be thrown. If error occurred during the delete exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCostStorageV1Api()
body = swagger_client.Body38() # Body38 |  (optional)

try: 
    api_response = api_instance.catalog_cost_storage_v1_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCostStorageV1Api->catalog_cost_storage_v1_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body38**](Body38.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_cost_storage_v1_get_post**
> list[CatalogDataCostInterface] catalog_cost_storage_v1_get_post(body=body)



Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCostStorageV1Api()
body = swagger_client.Body36() # Body36 |  (optional)

try: 
    api_response = api_instance.catalog_cost_storage_v1_get_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCostStorageV1Api->catalog_cost_storage_v1_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body36**](Body36.md)|  | [optional] 

### Return type

[**list[CatalogDataCostInterface]**](CatalogDataCostInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_cost_storage_v1_update_post**
> list[CatalogDataPriceUpdateResultInterface] catalog_cost_storage_v1_update_post(body=body)



Add or update product cost. Input item should correspond to \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid cost, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogCostStorageV1Api()
body = swagger_client.Body37() # Body37 |  (optional)

try: 
    api_response = api_instance.catalog_cost_storage_v1_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogCostStorageV1Api->catalog_cost_storage_v1_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body37**](Body37.md)|  | [optional] 

### Return type

[**list[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

