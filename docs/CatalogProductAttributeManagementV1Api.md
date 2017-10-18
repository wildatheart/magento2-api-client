# swagger_client.CatalogProductAttributeManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalog_product_attribute_management_v1_assign_post**](CatalogProductAttributeManagementV1Api.md#catalog_product_attribute_management_v1_assign_post) | **POST** /V1/products/attribute-sets/attributes | 
[**catalog_product_attribute_management_v1_get_attributes_get**](CatalogProductAttributeManagementV1Api.md#catalog_product_attribute_management_v1_get_attributes_get) | **GET** /V1/products/attribute-sets/{attributeSetId}/attributes | 
[**catalog_product_attribute_management_v1_unassign_delete**](CatalogProductAttributeManagementV1Api.md#catalog_product_attribute_management_v1_unassign_delete) | **DELETE** /V1/products/attribute-sets/{attributeSetId}/attributes/{attributeCode} | 


# **catalog_product_attribute_management_v1_assign_post**
> int catalog_product_attribute_management_v1_assign_post(body=body)



Assign attribute to attribute set

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeManagementV1Api()
body = swagger_client.Body24() # Body24 |  (optional)

try: 
    api_response = api_instance.catalog_product_attribute_management_v1_assign_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeManagementV1Api->catalog_product_attribute_management_v1_assign_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body24**](Body24.md)|  | [optional] 

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_management_v1_get_attributes_get**
> list[CatalogDataProductAttributeInterface] catalog_product_attribute_management_v1_get_attributes_get(attribute_set_id)



Retrieve related attributes based on given attribute set ID

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeManagementV1Api()
attribute_set_id = 'attribute_set_id_example' # str | 

try: 
    api_response = api_instance.catalog_product_attribute_management_v1_get_attributes_get(attribute_set_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeManagementV1Api->catalog_product_attribute_management_v1_get_attributes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_set_id** | **str**|  | 

### Return type

[**list[CatalogDataProductAttributeInterface]**](CatalogDataProductAttributeInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalog_product_attribute_management_v1_unassign_delete**
> bool catalog_product_attribute_management_v1_unassign_delete(attribute_set_id, attribute_code)



Remove attribute from attribute set

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogProductAttributeManagementV1Api()
attribute_set_id = 'attribute_set_id_example' # str | 
attribute_code = 'attribute_code_example' # str | 

try: 
    api_response = api_instance.catalog_product_attribute_management_v1_unassign_delete(attribute_set_id, attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogProductAttributeManagementV1Api->catalog_product_attribute_management_v1_unassign_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_set_id** | **str**|  | 
 **attribute_code** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

