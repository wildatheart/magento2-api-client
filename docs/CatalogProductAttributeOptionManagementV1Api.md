# swagger_client.CatalogProductAttributeOptionManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_attribute_option_management_v1_add_post**](CatalogProductAttributeOptionManagementV1Api.md#catalog_product_attribute_option_management_v1_add_post) | **POST** /V1/products/attributes/{attributeCode}/options | 
[**catalog_product_attribute_option_management_v1_delete_delete**](CatalogProductAttributeOptionManagementV1Api.md#catalog_product_attribute_option_management_v1_delete_delete) | **DELETE** /V1/products/attributes/{attributeCode}/options/{optionId} | 
[**catalog_product_attribute_option_management_v1_get_items_get**](CatalogProductAttributeOptionManagementV1Api.md#catalog_product_attribute_option_management_v1_get_items_get) | **GET** /V1/products/attributes/{attributeCode}/options | 


# **catalog_product_attribute_option_management_v1_add_post**
> bool catalog_product_attribute_option_management_v1_add_post(attribute_code, body=body)



Add option to attribute

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeOptionManagementV1Api()
attribute_code = 'attribute_code_example' # str | 
body = swagger_client.Body27() # Body27 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_option_management_v1_add_post(attribute_code, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeOptionManagementV1Api->catalog_product_attribute_option_management_v1_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 
 **body** | [**Body27**](Body27.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_option_management_v1_delete_delete**
> bool catalog_product_attribute_option_management_v1_delete_delete(attribute_code, option_id)



Delete option from attribute

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeOptionManagementV1Api()
attribute_code = 'attribute_code_example' # str | 
option_id = 'option_id_example' # str | 

try: 
    api_response = api_instance.catalog_product_attribute_option_management_v1_delete_delete(attribute_code, option_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeOptionManagementV1Api->catalog_product_attribute_option_management_v1_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 
 **option_id** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_option_management_v1_get_items_get**
> list[EavDataAttributeOptionInterface] catalog_product_attribute_option_management_v1_get_items_get(attribute_code)



Retrieve list of attribute options

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeOptionManagementV1Api()
attribute_code = 'attribute_code_example' # str | 

try: 
    api_response = api_instance.catalog_product_attribute_option_management_v1_get_items_get(attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeOptionManagementV1Api->catalog_product_attribute_option_management_v1_get_items_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 

### Return type

[**list[EavDataAttributeOptionInterface]**](EavDataAttributeOptionInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

