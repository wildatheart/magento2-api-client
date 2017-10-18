# swagger_client.DirectoryCountryInformationAcquirerV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directory_country_information_acquirer_v1_get_countries_info_get**](DirectoryCountryInformationAcquirerV1Api.md#directory_country_information_acquirer_v1_get_countries_info_get) | **GET** /V1/directory/countries | 
[**directory_country_information_acquirer_v1_get_country_info_get**](DirectoryCountryInformationAcquirerV1Api.md#directory_country_information_acquirer_v1_get_country_info_get) | **GET** /V1/directory/countries/{countryId} | 


# **directory_country_information_acquirer_v1_get_countries_info_get**
> list[DirectoryDataCountryInformationInterface] directory_country_information_acquirer_v1_get_countries_info_get()



Get all countries and regions information for the store.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DirectoryCountryInformationAcquirerV1Api()

try: 
    api_response = api_instance.directory_country_information_acquirer_v1_get_countries_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryCountryInformationAcquirerV1Api->directory_country_information_acquirer_v1_get_countries_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DirectoryDataCountryInformationInterface]**](DirectoryDataCountryInformationInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **directory_country_information_acquirer_v1_get_country_info_get**
> DirectoryDataCountryInformationInterface directory_country_information_acquirer_v1_get_country_info_get(country_id)



Get country and region information for the store.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DirectoryCountryInformationAcquirerV1Api()
country_id = 'country_id_example' # str | 

try: 
    api_response = api_instance.directory_country_information_acquirer_v1_get_country_info_get(country_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryCountryInformationAcquirerV1Api->directory_country_information_acquirer_v1_get_country_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 

### Return type

[**DirectoryDataCountryInformationInterface**](DirectoryDataCountryInformationInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

