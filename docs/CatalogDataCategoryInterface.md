# CatalogDataCategoryInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**parent_id** | **int** | Parent category ID | [optional] 
**name** | **str** | Category name | 
**is_active** | **bool** | Whether category is active | [optional] 
**position** | **int** | Category position | [optional] 
**level** | **int** | Category level | [optional] 
**children** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**available_sort_by** | **list[str]** |  | [optional] 
**include_in_menu** | **bool** |  | [optional] 
**extension_attributes** | [**CatalogDataCategoryExtensionInterface**](CatalogDataCategoryExtensionInterface.md) |  | [optional] 
**custom_attributes** | [**list[FrameworkAttributeInterface]**](FrameworkAttributeInterface.md) | Custom attributes values. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


