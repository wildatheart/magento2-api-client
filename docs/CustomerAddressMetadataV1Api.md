# swagger_client.CustomerAddressMetadataV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_address_metadata_v1_get_all_attributes_metadata_get**](CustomerAddressMetadataV1Api.md#customer_address_metadata_v1_get_all_attributes_metadata_get) | **GET** /V1/attributeMetadata/customerAddress | 
[**customer_address_metadata_v1_get_attribute_metadata_get**](CustomerAddressMetadataV1Api.md#customer_address_metadata_v1_get_attribute_metadata_get) | **GET** /V1/attributeMetadata/customerAddress/attribute/{attributeCode} | 
[**customer_address_metadata_v1_get_attributes_get**](CustomerAddressMetadataV1Api.md#customer_address_metadata_v1_get_attributes_get) | **GET** /V1/attributeMetadata/customerAddress/form/{formCode} | 
[**customer_address_metadata_v1_get_custom_attributes_metadata_get**](CustomerAddressMetadataV1Api.md#customer_address_metadata_v1_get_custom_attributes_metadata_get) | **GET** /V1/attributeMetadata/customerAddress/custom | 


# **customer_address_metadata_v1_get_all_attributes_metadata_get**
> list[CustomerDataAttributeMetadataInterface] customer_address_metadata_v1_get_all_attributes_metadata_get()



Get all attribute metadata.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressMetadataV1Api()

try: 
    api_response = api_instance.customer_address_metadata_v1_get_all_attributes_metadata_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressMetadataV1Api->customer_address_metadata_v1_get_all_attributes_metadata_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CustomerDataAttributeMetadataInterface]**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_address_metadata_v1_get_attribute_metadata_get**
> CustomerDataAttributeMetadataInterface customer_address_metadata_v1_get_attribute_metadata_get(attribute_code)



Retrieve attribute metadata.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressMetadataV1Api()
attribute_code = 'attribute_code_example' # str | 

try: 
    api_response = api_instance.customer_address_metadata_v1_get_attribute_metadata_get(attribute_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressMetadataV1Api->customer_address_metadata_v1_get_attribute_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_code** | **str**|  | 

### Return type

[**CustomerDataAttributeMetadataInterface**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_address_metadata_v1_get_attributes_get**
> list[CustomerDataAttributeMetadataInterface] customer_address_metadata_v1_get_attributes_get(form_code)



Retrieve all attributes filtered by form code

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressMetadataV1Api()
form_code = 'form_code_example' # str | 

try: 
    api_response = api_instance.customer_address_metadata_v1_get_attributes_get(form_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressMetadataV1Api->customer_address_metadata_v1_get_attributes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **form_code** | **str**|  | 

### Return type

[**list[CustomerDataAttributeMetadataInterface]**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_address_metadata_v1_get_custom_attributes_metadata_get**
> list[CustomerDataAttributeMetadataInterface] customer_address_metadata_v1_get_custom_attributes_metadata_get(data_interface_name=data_interface_name)



Get custom attributes metadata for the given data interface.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAddressMetadataV1Api()
data_interface_name = 'data_interface_name_example' # str |  (optional)

try: 
    api_response = api_instance.customer_address_metadata_v1_get_custom_attributes_metadata_get(data_interface_name=data_interface_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAddressMetadataV1Api->customer_address_metadata_v1_get_custom_attributes_metadata_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_interface_name** | **str**|  | [optional] 

### Return type

[**list[CustomerDataAttributeMetadataInterface]**](CustomerDataAttributeMetadataInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

