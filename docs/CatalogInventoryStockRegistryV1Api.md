# swagger_client.CatalogInventoryStockRegistryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_inventory_stock_registry_v1_get_low_stock_items_get**](CatalogInventoryStockRegistryV1Api.md#catalog_inventory_stock_registry_v1_get_low_stock_items_get) | **GET** /V1/stockItems/lowStock/ | 
[**catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get**](CatalogInventoryStockRegistryV1Api.md#catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get) | **GET** /V1/stockItems/{productSku} | 
[**catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get**](CatalogInventoryStockRegistryV1Api.md#catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get) | **GET** /V1/stockStatuses/{productSku} | 
[**catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put**](CatalogInventoryStockRegistryV1Api.md#catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put) | **PUT** /V1/products/{productSku}/stockItems/{itemId} | 


# **catalog_inventory_stock_registry_v1_get_low_stock_items_get**
> CatalogInventoryDataStockStatusCollectionInterface catalog_inventory_stock_registry_v1_get_low_stock_items_get(scope_id, qty, current_page=current_page, page_size=page_size)



Retrieves a list of SKU's with low inventory qty

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogInventoryStockRegistryV1Api()
scope_id = 56 # int | 
qty = 3.4 # float | 
current_page = 56 # int |  (optional)
page_size = 56 # int |  (optional)

try: 
    api_response = api_instance.catalog_inventory_stock_registry_v1_get_low_stock_items_get(scope_id, qty, current_page=current_page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogInventoryStockRegistryV1Api->catalog_inventory_stock_registry_v1_get_low_stock_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | **int**|  | 
 **qty** | **float**|  | 
 **current_page** | **int**|  | [optional] 
 **page_size** | **int**|  | [optional] 

### Return type

[**CatalogInventoryDataStockStatusCollectionInterface**](CatalogInventoryDataStockStatusCollectionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get**
> CatalogInventoryDataStockItemInterface catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get(product_sku, scope_id=scope_id)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogInventoryStockRegistryV1Api()
product_sku = 'product_sku_example' # str | 
scope_id = 56 # int |  (optional)

try: 
    api_response = api_instance.catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get(product_sku, scope_id=scope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogInventoryStockRegistryV1Api->catalog_inventory_stock_registry_v1_get_stock_item_by_sku_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_sku** | **str**|  | 
 **scope_id** | **int**|  | [optional] 

### Return type

[**CatalogInventoryDataStockItemInterface**](CatalogInventoryDataStockItemInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get**
> CatalogInventoryDataStockStatusInterface catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get(product_sku, scope_id=scope_id)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogInventoryStockRegistryV1Api()
product_sku = 'product_sku_example' # str | 
scope_id = 56 # int |  (optional)

try: 
    api_response = api_instance.catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get(product_sku, scope_id=scope_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogInventoryStockRegistryV1Api->catalog_inventory_stock_registry_v1_get_stock_status_by_sku_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_sku** | **str**|  | 
 **scope_id** | **int**|  | [optional] 

### Return type

[**CatalogInventoryDataStockStatusInterface**](CatalogInventoryDataStockStatusInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put**
> int catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put(product_sku, item_id, body=body)





### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogInventoryStockRegistryV1Api()
product_sku = 'product_sku_example' # str | 
item_id = 'item_id_example' # str | 
body = swagger_client.Body78() # Body78 |  (optional)

try: 
    api_response = api_instance.catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put(product_sku, item_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogInventoryStockRegistryV1Api->catalog_inventory_stock_registry_v1_update_stock_item_by_sku_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_sku** | **str**|  | 
 **item_id** | **str**|  | 
 **body** | [**Body78**](Body78.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

