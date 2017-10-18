# swagger_client.CatalogTierPriceStorageV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_tier_price_storage_v1_delete_post**](CatalogTierPriceStorageV1Api.md#catalog_tier_price_storage_v1_delete_post) | **POST** /V1/products/tier-prices-delete | 
[**catalog_tier_price_storage_v1_get_post**](CatalogTierPriceStorageV1Api.md#catalog_tier_price_storage_v1_get_post) | **POST** /V1/products/tier-prices-information | 
[**catalog_tier_price_storage_v1_replace_put**](CatalogTierPriceStorageV1Api.md#catalog_tier_price_storage_v1_replace_put) | **PUT** /V1/products/tier-prices | 
[**catalog_tier_price_storage_v1_update_post**](CatalogTierPriceStorageV1Api.md#catalog_tier_price_storage_v1_update_post) | **POST** /V1/products/tier-prices | 


# **catalog_tier_price_storage_v1_delete_post**
> list[CatalogDataPriceUpdateResultInterface] catalog_tier_price_storage_v1_delete_post(body=body)



Delete product tier prices. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from delete list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogTierPriceStorageV1Api()
body = swagger_client.Body33() # Body33 |  (optional)

try: 
    api_response = api_instance.catalog_tier_price_storage_v1_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogTierPriceStorageV1Api->catalog_tier_price_storage_v1_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body33**](Body33.md)|  | [optional] 

### Return type

[**list[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_tier_price_storage_v1_get_post**
> list[CatalogDataTierPriceInterface] catalog_tier_price_storage_v1_get_post(body=body)



Return product prices. In case of at least one of skus is not found exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogTierPriceStorageV1Api()
body = swagger_client.Body30() # Body30 |  (optional)

try: 
    api_response = api_instance.catalog_tier_price_storage_v1_get_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogTierPriceStorageV1Api->catalog_tier_price_storage_v1_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body30**](Body30.md)|  | [optional] 

### Return type

[**list[CatalogDataTierPriceInterface]**](CatalogDataTierPriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_tier_price_storage_v1_replace_put**
> list[CatalogDataPriceUpdateResultInterface] catalog_tier_price_storage_v1_replace_put(body=body)



Remove existing tier prices and replace them with the new ones. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from replace list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogTierPriceStorageV1Api()
body = swagger_client.Body31() # Body31 |  (optional)

try: 
    api_response = api_instance.catalog_tier_price_storage_v1_replace_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogTierPriceStorageV1Api->catalog_tier_price_storage_v1_replace_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body31**](Body31.md)|  | [optional] 

### Return type

[**list[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_tier_price_storage_v1_update_post**
> list[CatalogDataPriceUpdateResultInterface] catalog_tier_price_storage_v1_update_post(body=body)



Add or update product prices. If any items will have invalid price, price type, website id, sku, customer group or quantity, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogTierPriceStorageV1Api()
body = swagger_client.Body32() # Body32 |  (optional)

try: 
    api_response = api_instance.catalog_tier_price_storage_v1_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogTierPriceStorageV1Api->catalog_tier_price_storage_v1_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body32**](Body32.md)|  | [optional] 

### Return type

[**list[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

