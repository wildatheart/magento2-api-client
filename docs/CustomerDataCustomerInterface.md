# CustomerDataCustomerInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Customer id | [optional] 
**group_id** | **int** | Group id | [optional] 
**default_billing** | **str** | Default billing address id | [optional] 
**default_shipping** | **str** | Default shipping address id | [optional] 
**confirmation** | **str** | Confirmation | [optional] 
**created_at** | **str** | Created at time | [optional] 
**updated_at** | **str** | Updated at time | [optional] 
**created_in** | **str** | Created in area | [optional] 
**dob** | **str** | Date of birth | [optional] 
**email** | **str** | Email address | 
**firstname** | **str** | First name | 
**lastname** | **str** | Last name | 
**middlename** | **str** | Middle name | [optional] 
**prefix** | **str** | Prefix | [optional] 
**suffix** | **str** | Suffix | [optional] 
**gender** | **int** | Gender | [optional] 
**store_id** | **int** | Store id | [optional] 
**taxvat** | **str** | Tax Vat | [optional] 
**website_id** | **int** | Website id | [optional] 
**addresses** | [**list[CustomerDataAddressInterface]**](CustomerDataAddressInterface.md) | Customer addresses. | [optional] 
**disable_auto_group_change** | **int** | Disable auto group change flag. | [optional] 
**extension_attributes** | [**CustomerDataCustomerExtensionInterface**](CustomerDataCustomerExtensionInterface.md) |  | [optional] 
**custom_attributes** | [**list[FrameworkAttributeInterface]**](FrameworkAttributeInterface.md) | Custom attributes values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


