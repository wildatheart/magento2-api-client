# SalesDataOrderPaymentInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_status** | **str** | Account status. | 
**additional_data** | **str** | Additional data. | [optional] 
**additional_information** | **list[str]** | Array of additional information. | 
**address_status** | **str** | Address status. | [optional] 
**amount_authorized** | **float** | Amount authorized. | [optional] 
**amount_canceled** | **float** | Amount canceled. | [optional] 
**amount_ordered** | **float** | Amount ordered. | [optional] 
**amount_paid** | **float** | Amount paid. | [optional] 
**amount_refunded** | **float** | Amount refunded. | [optional] 
**anet_trans_method** | **str** | Anet transaction method. | [optional] 
**base_amount_authorized** | **float** | Base amount authorized. | [optional] 
**base_amount_canceled** | **float** | Base amount canceled. | [optional] 
**base_amount_ordered** | **float** | Base amount ordered. | [optional] 
**base_amount_paid** | **float** | Base amount paid. | [optional] 
**base_amount_paid_online** | **float** | Base amount paid online. | [optional] 
**base_amount_refunded** | **float** | Base amount refunded. | [optional] 
**base_amount_refunded_online** | **float** | Base amount refunded online. | [optional] 
**base_shipping_amount** | **float** | Base shipping amount. | [optional] 
**base_shipping_captured** | **float** | Base shipping captured amount. | [optional] 
**base_shipping_refunded** | **float** | Base shipping refunded amount. | [optional] 
**cc_approval** | **str** | Credit card approval. | [optional] 
**cc_avs_status** | **str** | Credit card avs status. | [optional] 
**cc_cid_status** | **str** | Credit card CID status. | [optional] 
**cc_debug_request_body** | **str** | Credit card debug request body. | [optional] 
**cc_debug_response_body** | **str** | Credit card debug response body. | [optional] 
**cc_debug_response_serialized** | **str** | Credit card debug response serialized. | [optional] 
**cc_exp_month** | **str** | Credit card expiration month. | [optional] 
**cc_exp_year** | **str** | Credit card expiration year. | [optional] 
**cc_last4** | **str** | Last four digits of the credit card. | 
**cc_number_enc** | **str** | Encrypted credit card number. | [optional] 
**cc_owner** | **str** | Credit card number. | [optional] 
**cc_secure_verify** | **str** | Credit card secure verify. | [optional] 
**cc_ss_issue** | **str** | Credit card SS issue. | [optional] 
**cc_ss_start_month** | **str** | Credit card SS start month. | [optional] 
**cc_ss_start_year** | **str** | Credit card SS start year. | [optional] 
**cc_status** | **str** | Credit card status. | [optional] 
**cc_status_description** | **str** | Credit card status description. | [optional] 
**cc_trans_id** | **str** | Credit card transaction ID. | [optional] 
**cc_type** | **str** | Credit card type. | [optional] 
**echeck_account_name** | **str** | eCheck account name. | [optional] 
**echeck_account_type** | **str** | eCheck account type. | [optional] 
**echeck_bank_name** | **str** | eCheck bank name. | [optional] 
**echeck_routing_number** | **str** | eCheck routing number. | [optional] 
**echeck_type** | **str** | eCheck type. | [optional] 
**entity_id** | **int** | Entity ID. | [optional] 
**last_trans_id** | **str** | Last transaction ID. | [optional] 
**method** | **str** | Method. | 
**parent_id** | **int** | Parent ID. | [optional] 
**po_number** | **str** | PO number. | [optional] 
**protection_eligibility** | **str** | Protection eligibility. | [optional] 
**quote_payment_id** | **int** | Quote payment ID. | [optional] 
**shipping_amount** | **float** | Shipping amount. | [optional] 
**shipping_captured** | **float** | Shipping captured. | [optional] 
**shipping_refunded** | **float** | Shipping refunded. | [optional] 
**extension_attributes** | [**SalesDataOrderPaymentExtensionInterface**](SalesDataOrderPaymentExtensionInterface.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


