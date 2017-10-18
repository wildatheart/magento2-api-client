# TaxDataTaxRuleInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id | [optional] 
**code** | **str** | Tax rule code | 
**priority** | **int** | Priority | 
**position** | **int** | Sort order. | 
**customer_tax_class_ids** | **list[int]** | Customer tax class id | 
**product_tax_class_ids** | **list[int]** | Product tax class id | 
**tax_rate_ids** | **list[int]** | Tax rate ids | 
**calculate_subtotal** | **bool** | Calculate subtotal. | [optional] 
**extension_attributes** | [**TaxDataTaxRuleExtensionInterface**](TaxDataTaxRuleExtensionInterface.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


