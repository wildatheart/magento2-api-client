# swagger_client.SalesRuleCouponManagementV1Api

All URIs are relative to *http://localhost/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sales_rule_coupon_management_v1_delete_by_codes_post**](SalesRuleCouponManagementV1Api.md#sales_rule_coupon_management_v1_delete_by_codes_post) | **POST** /V1/coupons/deleteByCodes | 
[**sales_rule_coupon_management_v1_delete_by_ids_post**](SalesRuleCouponManagementV1Api.md#sales_rule_coupon_management_v1_delete_by_ids_post) | **POST** /V1/coupons/deleteByIds | 
[**sales_rule_coupon_management_v1_generate_post**](SalesRuleCouponManagementV1Api.md#sales_rule_coupon_management_v1_generate_post) | **POST** /V1/coupons/generate | 


# **sales_rule_coupon_management_v1_delete_by_codes_post**
> SalesRuleDataCouponMassDeleteResultInterface sales_rule_coupon_management_v1_delete_by_codes_post(body=body)



Delete coupon by coupon codes.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponManagementV1Api()
body = swagger_client.Body129() # Body129 |  (optional)

try: 
    api_response = api_instance.sales_rule_coupon_management_v1_delete_by_codes_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponManagementV1Api->sales_rule_coupon_management_v1_delete_by_codes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body129**](Body129.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponMassDeleteResultInterface**](SalesRuleDataCouponMassDeleteResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_coupon_management_v1_delete_by_ids_post**
> SalesRuleDataCouponMassDeleteResultInterface sales_rule_coupon_management_v1_delete_by_ids_post(body=body)



Delete coupon by coupon ids.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponManagementV1Api()
body = swagger_client.Body128() # Body128 |  (optional)

try: 
    api_response = api_instance.sales_rule_coupon_management_v1_delete_by_ids_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponManagementV1Api->sales_rule_coupon_management_v1_delete_by_ids_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body128**](Body128.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponMassDeleteResultInterface**](SalesRuleDataCouponMassDeleteResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sales_rule_coupon_management_v1_generate_post**
> list[str] sales_rule_coupon_management_v1_generate_post(body=body)



Generate coupon for a rule

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SalesRuleCouponManagementV1Api()
body = swagger_client.Body127() # Body127 |  (optional)

try: 
    api_response = api_instance.sales_rule_coupon_management_v1_generate_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SalesRuleCouponManagementV1Api->sales_rule_coupon_management_v1_generate_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body127**](Body127.md)|  | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

