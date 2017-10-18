# SalesDataShipmentInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_address_id** | **int** | Billing address ID. | [optional] 
**created_at** | **str** | Created-at timestamp. | [optional] 
**customer_id** | **int** | Customer ID. | [optional] 
**email_sent** | **int** | Email-sent flag value. | [optional] 
**entity_id** | **int** | Shipment ID. | [optional] 
**increment_id** | **str** | Increment ID. | [optional] 
**order_id** | **int** | Order ID. | 
**packages** | [**list[SalesDataShipmentPackageInterface]**](SalesDataShipmentPackageInterface.md) | Array of packages, if any. Otherwise, null. | [optional] 
**shipment_status** | **int** | Shipment status. | [optional] 
**shipping_address_id** | **int** | Shipping address ID. | [optional] 
**shipping_label** | **str** | Shipping label. | [optional] 
**store_id** | **int** | Store ID. | [optional] 
**total_qty** | **float** | Total quantity. | [optional] 
**total_weight** | **float** | Total weight. | [optional] 
**updated_at** | **str** | Updated-at timestamp. | [optional] 
**items** | [**list[SalesDataShipmentItemInterface]**](SalesDataShipmentItemInterface.md) | Array of items. | 
**tracks** | [**list[SalesDataShipmentTrackInterface]**](SalesDataShipmentTrackInterface.md) | Array of tracks. | 
**comments** | [**list[SalesDataShipmentCommentInterface]**](SalesDataShipmentCommentInterface.md) | Array of comments. | 
**extension_attributes** | [**SalesDataShipmentExtensionInterface**](SalesDataShipmentExtensionInterface.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


