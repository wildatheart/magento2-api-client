# TaxDataTaxRateInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id | [optional] 
**tax_country_id** | **str** | Country id | 
**tax_region_id** | **int** | Region id | [optional] 
**region_name** | **str** | Region name | [optional] 
**tax_postcode** | **str** | Postcode | [optional] 
**zip_is_range** | **int** | Zip is range | [optional] 
**zip_from** | **int** | Zip range from | [optional] 
**zip_to** | **int** | Zip range to | [optional] 
**rate** | **float** | Tax rate in percentage | 
**code** | **str** | Tax rate code | 
**titles** | [**list[TaxDataTaxRateTitleInterface]**](TaxDataTaxRateTitleInterface.md) | Tax rate titles | [optional] 
**extension_attributes** | [**TaxDataTaxRateExtensionInterface**](TaxDataTaxRateExtensionInterface.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


