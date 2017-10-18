# swagger_client.CatalogBasePriceStorageV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_base_price_storage_v1_get_post**](CatalogBasePriceStorageV1Api.md#catalog_base_price_storage_v1_get_post) | **POST** /V1/products/base-prices-information | 
[**catalog_base_price_storage_v1_update_post**](CatalogBasePriceStorageV1Api.md#catalog_base_price_storage_v1_update_post) | **POST** /V1/products/base-prices | 


# **catalog_base_price_storage_v1_get_post**
> list[CatalogDataBasePriceInterface] catalog_base_price_storage_v1_get_post(body=body)



Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogBasePriceStorageV1Api()
body = swagger_client.Body34() # Body34 |  (optional)

try: 
    api_response = api_instance.catalog_base_price_storage_v1_get_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogBasePriceStorageV1Api->catalog_base_price_storage_v1_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body34**](Body34.md)|  | [optional] 

### Return type

[**list[CatalogDataBasePriceInterface]**](CatalogDataBasePriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_base_price_storage_v1_update_post**
> list[CatalogDataPriceUpdateResultInterface] catalog_base_price_storage_v1_update_post(body=body)



Add or update product prices. Input item should correspond \\Magento\\Catalog\\Api\\Data\\CostInterface. If any items will have invalid price, store id or sku, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogBasePriceStorageV1Api()
body = swagger_client.Body35() # Body35 |  (optional)

try: 
    api_response = api_instance.catalog_base_price_storage_v1_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogBasePriceStorageV1Api->catalog_base_price_storage_v1_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body35**](Body35.md)|  | [optional] 

### Return type

[**list[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

