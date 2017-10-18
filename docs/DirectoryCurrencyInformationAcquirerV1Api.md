# swagger_client.DirectoryCurrencyInformationAcquirerV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**directory_currency_information_acquirer_v1_get_currency_info_get**](DirectoryCurrencyInformationAcquirerV1Api.md#directory_currency_information_acquirer_v1_get_currency_info_get) | **GET** /V1/directory/currency | 


# **directory_currency_information_acquirer_v1_get_currency_info_get**
> DirectoryDataCurrencyInformationInterface directory_currency_information_acquirer_v1_get_currency_info_get()



Get currency information for the store.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DirectoryCurrencyInformationAcquirerV1Api()

try: 
    api_response = api_instance.directory_currency_information_acquirer_v1_get_currency_info_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectoryCurrencyInformationAcquirerV1Api->directory_currency_information_acquirer_v1_get_currency_info_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DirectoryDataCurrencyInformationInterface**](DirectoryDataCurrencyInformationInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

