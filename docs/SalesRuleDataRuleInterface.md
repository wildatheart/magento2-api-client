# SalesRuleDataRuleInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **int** | Rule id | [optional] 
**name** | **str** | Rule name | [optional] 
**store_labels** | [**list[SalesRuleDataRuleLabelInterface]**](SalesRuleDataRuleLabelInterface.md) | Display label | [optional] 
**description** | **str** | Description | [optional] 
**website_ids** | **list[int]** | A list of websites the rule applies to | 
**customer_group_ids** | **list[int]** | Ids of customer groups that the rule applies to | 
**from_date** | **str** | The start date when the coupon is active | [optional] 
**to_date** | **str** | The end date when the coupon is active | [optional] 
**uses_per_customer** | **int** | Number of uses per customer | 
**is_active** | **bool** | The coupon is active | 
**condition** | [**SalesRuleDataConditionInterface**](SalesRuleDataConditionInterface.md) |  | [optional] 
**action_condition** | [**SalesRuleDataConditionInterface**](SalesRuleDataConditionInterface.md) |  | [optional] 
**stop_rules_processing** | **bool** | To stop rule processing | 
**is_advanced** | **bool** | Is this field needed | 
**product_ids** | **list[int]** | Product ids | [optional] 
**sort_order** | **int** | Sort order | 
**simple_action** | **str** | Simple action of the rule | [optional] 
**discount_amount** | **float** | Discount amount | 
**discount_qty** | **float** | Maximum qty discount is applied | [optional] 
**discount_step** | **int** | Discount step | 
**apply_to_shipping** | **bool** | The rule applies to shipping | 
**times_used** | **int** | How many times the rule has been used | 
**is_rss** | **bool** | Whether the rule is in RSS | 
**coupon_type** | **str** | Coupon type | 
**use_auto_generation** | **bool** | To auto generate coupon | 
**uses_per_coupon** | **int** | Limit of uses per coupon | 
**simple_free_shipping** | **str** | To grant free shipping | [optional] 
**extension_attributes** | [**SalesRuleDataRuleExtensionInterface**](SalesRuleDataRuleExtensionInterface.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


