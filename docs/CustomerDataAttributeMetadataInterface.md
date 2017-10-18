# CustomerDataAttributeMetadataInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frontend_input** | **str** | HTML for input element. | 
**input_filter** | **str** | Template used for input (e.g. \&quot;date\&quot;) | 
**store_label** | **str** | Label of the store. | 
**validation_rules** | [**list[CustomerDataValidationRuleInterface]**](CustomerDataValidationRuleInterface.md) | Validation rules. | 
**multiline_count** | **int** | Of lines of the attribute value. | 
**visible** | **bool** | Attribute is visible on frontend. | 
**required** | **bool** | Attribute is required. | 
**data_model** | **str** | Data model for attribute. | 
**options** | [**list[CustomerDataOptionInterface]**](CustomerDataOptionInterface.md) | Options of the attribute (key &#x3D;&gt; value pairs for select) | 
**frontend_class** | **str** | Class which is used to display the attribute on frontend. | 
**user_defined** | **bool** | Current attribute has been defined by a user. | 
**sort_order** | **int** | Attributes sort order. | 
**frontend_label** | **str** | Label which supposed to be displayed on frontend. | 
**note** | **str** | The note attribute for the element. | 
**system** | **bool** | This is a system attribute. | 
**backend_type** | **str** | Backend type. | 
**is_used_in_grid** | **bool** | It is used in customer grid | [optional] 
**is_visible_in_grid** | **bool** | It is visible in customer grid | [optional] 
**is_filterable_in_grid** | **bool** | It is filterable in customer grid | [optional] 
**is_searchable_in_grid** | **bool** | It is searchable in customer grid | [optional] 
**attribute_code** | **str** | Code of the attribute. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


