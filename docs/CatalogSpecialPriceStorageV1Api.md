# swagger_client.CatalogSpecialPriceStorageV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_special_price_storage_v1_delete_post**](CatalogSpecialPriceStorageV1Api.md#catalog_special_price_storage_v1_delete_post) | **POST** /V1/products/special-price-delete | 
[**catalog_special_price_storage_v1_get_post**](CatalogSpecialPriceStorageV1Api.md#catalog_special_price_storage_v1_get_post) | **POST** /V1/products/special-price-information | 
[**catalog_special_price_storage_v1_update_post**](CatalogSpecialPriceStorageV1Api.md#catalog_special_price_storage_v1_update_post) | **POST** /V1/products/special-price | 


# **catalog_special_price_storage_v1_delete_post**
> list[CatalogDataPriceUpdateResultInterface] catalog_special_price_storage_v1_delete_post(body=body)



Delete product's special price. If any items will have invalid price, store id, sku or dates, they will be marked as failed and excluded from delete list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the delete exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogSpecialPriceStorageV1Api()
body = swagger_client.Body41() # Body41 |  (optional)

try: 
    api_response = api_instance.catalog_special_price_storage_v1_delete_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogSpecialPriceStorageV1Api->catalog_special_price_storage_v1_delete_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body41**](Body41.md)|  | [optional] 

### Return type

[**list[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_special_price_storage_v1_get_post**
> list[CatalogDataSpecialPriceInterface] catalog_special_price_storage_v1_get_post(body=body)



Return product's special price. In case of at least one of skus is not found exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogSpecialPriceStorageV1Api()
body = swagger_client.Body39() # Body39 |  (optional)

try: 
    api_response = api_instance.catalog_special_price_storage_v1_get_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogSpecialPriceStorageV1Api->catalog_special_price_storage_v1_get_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body39**](Body39.md)|  | [optional] 

### Return type

[**list[CatalogDataSpecialPriceInterface]**](CatalogDataSpecialPriceInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_special_price_storage_v1_update_post**
> list[CatalogDataPriceUpdateResultInterface] catalog_special_price_storage_v1_update_post(body=body)



Add or update product's special price. If any items will have invalid price, store id, sku or dates, they will be marked as failed and excluded from update list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the update exception will be thrown.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogSpecialPriceStorageV1Api()
body = swagger_client.Body40() # Body40 |  (optional)

try: 
    api_response = api_instance.catalog_special_price_storage_v1_update_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogSpecialPriceStorageV1Api->catalog_special_price_storage_v1_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body40**](Body40.md)|  | [optional] 

### Return type

[**list[CatalogDataPriceUpdateResultInterface]**](CatalogDataPriceUpdateResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

