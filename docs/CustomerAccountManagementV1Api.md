# swagger_client.CustomerAccountManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customer_account_management_v1_activate_by_id_put**](CustomerAccountManagementV1Api.md#customer_account_management_v1_activate_by_id_put) | **PUT** /V1/customers/me/activate | 
[**customer_account_management_v1_activate_put**](CustomerAccountManagementV1Api.md#customer_account_management_v1_activate_put) | **PUT** /V1/customers/{email}/activate | 
[**customer_account_management_v1_change_password_by_id_put**](CustomerAccountManagementV1Api.md#customer_account_management_v1_change_password_by_id_put) | **PUT** /V1/customers/me/password | 
[**customer_account_management_v1_create_account_post**](CustomerAccountManagementV1Api.md#customer_account_management_v1_create_account_post) | **POST** /V1/customers | 
[**customer_account_management_v1_get_confirmation_status_get**](CustomerAccountManagementV1Api.md#customer_account_management_v1_get_confirmation_status_get) | **GET** /V1/customers/{customerId}/confirm | 
[**customer_account_management_v1_get_default_billing_address_get**](CustomerAccountManagementV1Api.md#customer_account_management_v1_get_default_billing_address_get) | **GET** /V1/customers/me/billingAddress | 
[**customer_account_management_v1_get_default_billing_address_get_0**](CustomerAccountManagementV1Api.md#customer_account_management_v1_get_default_billing_address_get_0) | **GET** /V1/customers/{customerId}/billingAddress | 
[**customer_account_management_v1_get_default_shipping_address_get**](CustomerAccountManagementV1Api.md#customer_account_management_v1_get_default_shipping_address_get) | **GET** /V1/customers/me/shippingAddress | 
[**customer_account_management_v1_get_default_shipping_address_get_0**](CustomerAccountManagementV1Api.md#customer_account_management_v1_get_default_shipping_address_get_0) | **GET** /V1/customers/{customerId}/shippingAddress | 
[**customer_account_management_v1_initiate_password_reset_put**](CustomerAccountManagementV1Api.md#customer_account_management_v1_initiate_password_reset_put) | **PUT** /V1/customers/password | 
[**customer_account_management_v1_is_email_available_post**](CustomerAccountManagementV1Api.md#customer_account_management_v1_is_email_available_post) | **POST** /V1/customers/isEmailAvailable | 
[**customer_account_management_v1_is_readonly_get**](CustomerAccountManagementV1Api.md#customer_account_management_v1_is_readonly_get) | **GET** /V1/customers/{customerId}/permissions/readonly | 
[**customer_account_management_v1_resend_confirmation_post**](CustomerAccountManagementV1Api.md#customer_account_management_v1_resend_confirmation_post) | **POST** /V1/customers/confirm | 
[**customer_account_management_v1_validate_put**](CustomerAccountManagementV1Api.md#customer_account_management_v1_validate_put) | **PUT** /V1/customers/validate | 
[**customer_account_management_v1_validate_reset_password_link_token_get**](CustomerAccountManagementV1Api.md#customer_account_management_v1_validate_reset_password_link_token_get) | **GET** /V1/customers/{customerId}/password/resetLinkToken/{resetPasswordLinkToken} | 


# **customer_account_management_v1_activate_by_id_put**
> CustomerDataCustomerInterface customer_account_management_v1_activate_by_id_put(body=body)



Activate a customer account using a key that was sent in a confirmation email.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
body = swagger_client.Body7() # Body7 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_activate_by_id_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_activate_by_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_activate_put**
> CustomerDataCustomerInterface customer_account_management_v1_activate_put(email, body=body)



Activate a customer account using a key that was sent in a confirmation email.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
email = 'email_example' # str | 
body = swagger_client.Body8() # Body8 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_activate_put(email, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_activate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_change_password_by_id_put**
> bool customer_account_management_v1_change_password_by_id_put(body=body)



Change customer password.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
body = swagger_client.Body9() # Body9 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_change_password_by_id_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_change_password_by_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_create_account_post**
> CustomerDataCustomerInterface customer_account_management_v1_create_account_post(body=body)



Create customer account. Perform necessary business operations like sending email.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
body = swagger_client.Body6() # Body6 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_create_account_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_create_account_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

[**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_get_confirmation_status_get**
> str customer_account_management_v1_get_confirmation_status_get(customer_id)



Gets the account confirmation status.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
customer_id = 56 # int | 

try: 
    api_response = api_instance.customer_account_management_v1_get_confirmation_status_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_get_confirmation_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_get_default_billing_address_get**
> CustomerDataAddressInterface customer_account_management_v1_get_default_billing_address_get()



Retrieve default billing address for the given customerId.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()

try: 
    api_response = api_instance.customer_account_management_v1_get_default_billing_address_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_get_default_billing_address_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_get_default_billing_address_get_0**
> CustomerDataAddressInterface customer_account_management_v1_get_default_billing_address_get_0(customer_id)



Retrieve default billing address for the given customerId.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
customer_id = 56 # int | 

try: 
    api_response = api_instance.customer_account_management_v1_get_default_billing_address_get_0(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_get_default_billing_address_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_get_default_shipping_address_get**
> CustomerDataAddressInterface customer_account_management_v1_get_default_shipping_address_get()



Retrieve default shipping address for the given customerId.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()

try: 
    api_response = api_instance.customer_account_management_v1_get_default_shipping_address_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_get_default_shipping_address_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_get_default_shipping_address_get_0**
> CustomerDataAddressInterface customer_account_management_v1_get_default_shipping_address_get_0(customer_id)



Retrieve default shipping address for the given customerId.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
customer_id = 56 # int | 

try: 
    api_response = api_instance.customer_account_management_v1_get_default_shipping_address_get_0(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_get_default_shipping_address_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

[**CustomerDataAddressInterface**](CustomerDataAddressInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_initiate_password_reset_put**
> bool customer_account_management_v1_initiate_password_reset_put(body=body)



Send an email to the customer with a password reset link.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
body = swagger_client.Body10() # Body10 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_initiate_password_reset_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_initiate_password_reset_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_is_email_available_post**
> bool customer_account_management_v1_is_email_available_post(body=body)



Check if given email is associated with a customer account in given website.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
body = swagger_client.Body13() # Body13 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_is_email_available_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_is_email_available_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body13**](Body13.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_is_readonly_get**
> bool customer_account_management_v1_is_readonly_get(customer_id)



Check if customer can be deleted.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
customer_id = 56 # int | 

try: 
    api_response = api_instance.customer_account_management_v1_is_readonly_get(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_is_readonly_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_resend_confirmation_post**
> bool customer_account_management_v1_resend_confirmation_post(body=body)



Resend confirmation email.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
body = swagger_client.Body11() # Body11 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_resend_confirmation_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_resend_confirmation_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_validate_put**
> CustomerDataValidationResultsInterface customer_account_management_v1_validate_put(body=body)



Validate customer data.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
body = swagger_client.Body12() # Body12 |  (optional)

try: 
    api_response = api_instance.customer_account_management_v1_validate_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_validate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body12**](Body12.md)|  | [optional] 

### Return type

[**CustomerDataValidationResultsInterface**](CustomerDataValidationResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **customer_account_management_v1_validate_reset_password_link_token_get**
> bool customer_account_management_v1_validate_reset_password_link_token_get(customer_id, reset_password_link_token)



Check if password reset token is valid.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CustomerAccountManagementV1Api()
customer_id = 56 # int | 
reset_password_link_token = 'reset_password_link_token_example' # str | 

try: 
    api_response = api_instance.customer_account_management_v1_validate_reset_password_link_token_get(customer_id, reset_password_link_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerAccountManagementV1Api->customer_account_management_v1_validate_reset_password_link_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **reset_password_link_token** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

