# CatalogDataProductRenderInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**add_to_cart_button** | [**CatalogDataProductRenderButtonInterface**](CatalogDataProductRenderButtonInterface.md) |  | 
**add_to_compare_button** | [**CatalogDataProductRenderButtonInterface**](CatalogDataProductRenderButtonInterface.md) |  | 
**price_info** | [**CatalogDataProductRenderPriceInfoInterface**](CatalogDataProductRenderPriceInfoInterface.md) |  | 
**images** | [**list[CatalogDataProductRenderImageInterface]**](CatalogDataProductRenderImageInterface.md) | Enough information, that needed to render image on front | 
**url** | **str** | Product url | 
**id** | **int** | Product identifier | 
**name** | **str** | Product name | 
**type** | **str** | Product type. Such as bundle, grouped, simple, etc... | 
**is_salable** | **str** | Information about product saleability (In Stock) | 
**store_id** | **int** | Information about current store id or requested store id | 
**currency_code** | **str** | Current or desired currency code to product | 
**extension_attributes** | [**CatalogDataProductRenderExtensionInterface**](CatalogDataProductRenderExtensionInterface.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


