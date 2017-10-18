# SalesDataTransactionInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **int** | Transaction ID. | 
**parent_id** | **int** | The parent ID for the transaction. Otherwise, null. | [optional] 
**order_id** | **int** | Order ID. | 
**payment_id** | **int** | Payment ID. | 
**txn_id** | **str** | Transaction business ID. | 
**parent_txn_id** | **str** | Parent transaction business ID. | 
**txn_type** | **str** | Transaction type. | 
**is_closed** | **int** | Is-closed flag value. | 
**additional_information** | **list[str]** | Array of additional information. Otherwise, null. | [optional] 
**created_at** | **str** | Created-at timestamp. | 
**child_transactions** | [**list[SalesDataTransactionInterface]**](SalesDataTransactionInterface.md) | Array of child transactions. | 
**extension_attributes** | [**SalesDataTransactionExtensionInterface**](SalesDataTransactionExtensionInterface.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


