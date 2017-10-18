# CustomerDataAddressInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**customer_id** | **int** | Customer ID | [optional] 
**region** | [**CustomerDataRegionInterface**](CustomerDataRegionInterface.md) |  | [optional] 
**region_id** | **int** | Region ID | [optional] 
**country_id** | **str** | Country code in ISO_3166-2 format | [optional] 
**street** | **list[str]** | Street | [optional] 
**company** | **str** | Company | [optional] 
**telephone** | **str** | Telephone number | [optional] 
**fax** | **str** | Fax number | [optional] 
**postcode** | **str** | Postcode | [optional] 
**city** | **str** | City name | [optional] 
**firstname** | **str** | First name | [optional] 
**lastname** | **str** | Last name | [optional] 
**middlename** | **str** | Middle name | [optional] 
**prefix** | **str** | Prefix | [optional] 
**suffix** | **str** | Suffix | [optional] 
**vat_id** | **str** | Vat id | [optional] 
**default_shipping** | **bool** | If this address is default shipping address. | [optional] 
**default_billing** | **bool** | If this address is default billing address | [optional] 
**extension_attributes** | [**CustomerDataAddressExtensionInterface**](CustomerDataAddressExtensionInterface.md) |  | [optional] 
**custom_attributes** | [**list[FrameworkAttributeInterface]**](FrameworkAttributeInterface.md) | Custom attributes values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


