# swagger_client.CheckoutAgreementsCheckoutAgreementsRepositoryV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_agreements_checkout_agreements_repository_v1_get_list_get**](CheckoutAgreementsCheckoutAgreementsRepositoryV1Api.md#checkout_agreements_checkout_agreements_repository_v1_get_list_get) | **GET** /V1/carts/licence | 


# **checkout_agreements_checkout_agreements_repository_v1_get_list_get**
> list[CheckoutAgreementsDataAgreementInterface] checkout_agreements_checkout_agreements_repository_v1_get_list_get()



Lists active checkout agreements.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CheckoutAgreementsCheckoutAgreementsRepositoryV1Api()

try: 
    api_response = api_instance.checkout_agreements_checkout_agreements_repository_v1_get_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CheckoutAgreementsCheckoutAgreementsRepositoryV1Api->checkout_agreements_checkout_agreements_repository_v1_get_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CheckoutAgreementsDataAgreementInterface]**](CheckoutAgreementsDataAgreementInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

