# coding: utf-8

"""
    Magento Community

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SalesRuleDataRuleInterface(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'rule_id': 'int',
        'name': 'str',
        'store_labels': 'list[SalesRuleDataRuleLabelInterface]',
        'description': 'str',
        'website_ids': 'list[int]',
        'customer_group_ids': 'list[int]',
        'from_date': 'str',
        'to_date': 'str',
        'uses_per_customer': 'int',
        'is_active': 'bool',
        'condition': 'SalesRuleDataConditionInterface',
        'action_condition': 'SalesRuleDataConditionInterface',
        'stop_rules_processing': 'bool',
        'is_advanced': 'bool',
        'product_ids': 'list[int]',
        'sort_order': 'int',
        'simple_action': 'str',
        'discount_amount': 'float',
        'discount_qty': 'float',
        'discount_step': 'int',
        'apply_to_shipping': 'bool',
        'times_used': 'int',
        'is_rss': 'bool',
        'coupon_type': 'str',
        'use_auto_generation': 'bool',
        'uses_per_coupon': 'int',
        'simple_free_shipping': 'str',
        'extension_attributes': 'SalesRuleDataRuleExtensionInterface'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'name': 'name',
        'store_labels': 'store_labels',
        'description': 'description',
        'website_ids': 'website_ids',
        'customer_group_ids': 'customer_group_ids',
        'from_date': 'from_date',
        'to_date': 'to_date',
        'uses_per_customer': 'uses_per_customer',
        'is_active': 'is_active',
        'condition': 'condition',
        'action_condition': 'action_condition',
        'stop_rules_processing': 'stop_rules_processing',
        'is_advanced': 'is_advanced',
        'product_ids': 'product_ids',
        'sort_order': 'sort_order',
        'simple_action': 'simple_action',
        'discount_amount': 'discount_amount',
        'discount_qty': 'discount_qty',
        'discount_step': 'discount_step',
        'apply_to_shipping': 'apply_to_shipping',
        'times_used': 'times_used',
        'is_rss': 'is_rss',
        'coupon_type': 'coupon_type',
        'use_auto_generation': 'use_auto_generation',
        'uses_per_coupon': 'uses_per_coupon',
        'simple_free_shipping': 'simple_free_shipping',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, rule_id=None, name=None, store_labels=None, description=None, website_ids=None, customer_group_ids=None, from_date=None, to_date=None, uses_per_customer=None, is_active=None, condition=None, action_condition=None, stop_rules_processing=None, is_advanced=None, product_ids=None, sort_order=None, simple_action=None, discount_amount=None, discount_qty=None, discount_step=None, apply_to_shipping=None, times_used=None, is_rss=None, coupon_type=None, use_auto_generation=None, uses_per_coupon=None, simple_free_shipping=None, extension_attributes=None):
        """
        SalesRuleDataRuleInterface - a model defined in Swagger
        """

        self._rule_id = None
        self._name = None
        self._store_labels = None
        self._description = None
        self._website_ids = None
        self._customer_group_ids = None
        self._from_date = None
        self._to_date = None
        self._uses_per_customer = None
        self._is_active = None
        self._condition = None
        self._action_condition = None
        self._stop_rules_processing = None
        self._is_advanced = None
        self._product_ids = None
        self._sort_order = None
        self._simple_action = None
        self._discount_amount = None
        self._discount_qty = None
        self._discount_step = None
        self._apply_to_shipping = None
        self._times_used = None
        self._is_rss = None
        self._coupon_type = None
        self._use_auto_generation = None
        self._uses_per_coupon = None
        self._simple_free_shipping = None
        self._extension_attributes = None

        if rule_id is not None:
          self.rule_id = rule_id
        if name is not None:
          self.name = name
        if store_labels is not None:
          self.store_labels = store_labels
        if description is not None:
          self.description = description
        self.website_ids = website_ids
        self.customer_group_ids = customer_group_ids
        if from_date is not None:
          self.from_date = from_date
        if to_date is not None:
          self.to_date = to_date
        self.uses_per_customer = uses_per_customer
        self.is_active = is_active
        if condition is not None:
          self.condition = condition
        if action_condition is not None:
          self.action_condition = action_condition
        self.stop_rules_processing = stop_rules_processing
        self.is_advanced = is_advanced
        if product_ids is not None:
          self.product_ids = product_ids
        self.sort_order = sort_order
        if simple_action is not None:
          self.simple_action = simple_action
        self.discount_amount = discount_amount
        if discount_qty is not None:
          self.discount_qty = discount_qty
        self.discount_step = discount_step
        self.apply_to_shipping = apply_to_shipping
        self.times_used = times_used
        self.is_rss = is_rss
        self.coupon_type = coupon_type
        self.use_auto_generation = use_auto_generation
        self.uses_per_coupon = uses_per_coupon
        if simple_free_shipping is not None:
          self.simple_free_shipping = simple_free_shipping
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def rule_id(self):
        """
        Gets the rule_id of this SalesRuleDataRuleInterface.
        Rule id

        :return: The rule_id of this SalesRuleDataRuleInterface.
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this SalesRuleDataRuleInterface.
        Rule id

        :param rule_id: The rule_id of this SalesRuleDataRuleInterface.
        :type: int
        """

        self._rule_id = rule_id

    @property
    def name(self):
        """
        Gets the name of this SalesRuleDataRuleInterface.
        Rule name

        :return: The name of this SalesRuleDataRuleInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SalesRuleDataRuleInterface.
        Rule name

        :param name: The name of this SalesRuleDataRuleInterface.
        :type: str
        """

        self._name = name

    @property
    def store_labels(self):
        """
        Gets the store_labels of this SalesRuleDataRuleInterface.
        Display label

        :return: The store_labels of this SalesRuleDataRuleInterface.
        :rtype: list[SalesRuleDataRuleLabelInterface]
        """
        return self._store_labels

    @store_labels.setter
    def store_labels(self, store_labels):
        """
        Sets the store_labels of this SalesRuleDataRuleInterface.
        Display label

        :param store_labels: The store_labels of this SalesRuleDataRuleInterface.
        :type: list[SalesRuleDataRuleLabelInterface]
        """

        self._store_labels = store_labels

    @property
    def description(self):
        """
        Gets the description of this SalesRuleDataRuleInterface.
        Description

        :return: The description of this SalesRuleDataRuleInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SalesRuleDataRuleInterface.
        Description

        :param description: The description of this SalesRuleDataRuleInterface.
        :type: str
        """

        self._description = description

    @property
    def website_ids(self):
        """
        Gets the website_ids of this SalesRuleDataRuleInterface.
        A list of websites the rule applies to

        :return: The website_ids of this SalesRuleDataRuleInterface.
        :rtype: list[int]
        """
        return self._website_ids

    @website_ids.setter
    def website_ids(self, website_ids):
        """
        Sets the website_ids of this SalesRuleDataRuleInterface.
        A list of websites the rule applies to

        :param website_ids: The website_ids of this SalesRuleDataRuleInterface.
        :type: list[int]
        """
        if website_ids is None:
            raise ValueError("Invalid value for `website_ids`, must not be `None`")

        self._website_ids = website_ids

    @property
    def customer_group_ids(self):
        """
        Gets the customer_group_ids of this SalesRuleDataRuleInterface.
        Ids of customer groups that the rule applies to

        :return: The customer_group_ids of this SalesRuleDataRuleInterface.
        :rtype: list[int]
        """
        return self._customer_group_ids

    @customer_group_ids.setter
    def customer_group_ids(self, customer_group_ids):
        """
        Sets the customer_group_ids of this SalesRuleDataRuleInterface.
        Ids of customer groups that the rule applies to

        :param customer_group_ids: The customer_group_ids of this SalesRuleDataRuleInterface.
        :type: list[int]
        """
        if customer_group_ids is None:
            raise ValueError("Invalid value for `customer_group_ids`, must not be `None`")

        self._customer_group_ids = customer_group_ids

    @property
    def from_date(self):
        """
        Gets the from_date of this SalesRuleDataRuleInterface.
        The start date when the coupon is active

        :return: The from_date of this SalesRuleDataRuleInterface.
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """
        Sets the from_date of this SalesRuleDataRuleInterface.
        The start date when the coupon is active

        :param from_date: The from_date of this SalesRuleDataRuleInterface.
        :type: str
        """

        self._from_date = from_date

    @property
    def to_date(self):
        """
        Gets the to_date of this SalesRuleDataRuleInterface.
        The end date when the coupon is active

        :return: The to_date of this SalesRuleDataRuleInterface.
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """
        Sets the to_date of this SalesRuleDataRuleInterface.
        The end date when the coupon is active

        :param to_date: The to_date of this SalesRuleDataRuleInterface.
        :type: str
        """

        self._to_date = to_date

    @property
    def uses_per_customer(self):
        """
        Gets the uses_per_customer of this SalesRuleDataRuleInterface.
        Number of uses per customer

        :return: The uses_per_customer of this SalesRuleDataRuleInterface.
        :rtype: int
        """
        return self._uses_per_customer

    @uses_per_customer.setter
    def uses_per_customer(self, uses_per_customer):
        """
        Sets the uses_per_customer of this SalesRuleDataRuleInterface.
        Number of uses per customer

        :param uses_per_customer: The uses_per_customer of this SalesRuleDataRuleInterface.
        :type: int
        """
        if uses_per_customer is None:
            raise ValueError("Invalid value for `uses_per_customer`, must not be `None`")

        self._uses_per_customer = uses_per_customer

    @property
    def is_active(self):
        """
        Gets the is_active of this SalesRuleDataRuleInterface.
        The coupon is active

        :return: The is_active of this SalesRuleDataRuleInterface.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this SalesRuleDataRuleInterface.
        The coupon is active

        :param is_active: The is_active of this SalesRuleDataRuleInterface.
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")

        self._is_active = is_active

    @property
    def condition(self):
        """
        Gets the condition of this SalesRuleDataRuleInterface.

        :return: The condition of this SalesRuleDataRuleInterface.
        :rtype: SalesRuleDataConditionInterface
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """
        Sets the condition of this SalesRuleDataRuleInterface.

        :param condition: The condition of this SalesRuleDataRuleInterface.
        :type: SalesRuleDataConditionInterface
        """

        self._condition = condition

    @property
    def action_condition(self):
        """
        Gets the action_condition of this SalesRuleDataRuleInterface.

        :return: The action_condition of this SalesRuleDataRuleInterface.
        :rtype: SalesRuleDataConditionInterface
        """
        return self._action_condition

    @action_condition.setter
    def action_condition(self, action_condition):
        """
        Sets the action_condition of this SalesRuleDataRuleInterface.

        :param action_condition: The action_condition of this SalesRuleDataRuleInterface.
        :type: SalesRuleDataConditionInterface
        """

        self._action_condition = action_condition

    @property
    def stop_rules_processing(self):
        """
        Gets the stop_rules_processing of this SalesRuleDataRuleInterface.
        To stop rule processing

        :return: The stop_rules_processing of this SalesRuleDataRuleInterface.
        :rtype: bool
        """
        return self._stop_rules_processing

    @stop_rules_processing.setter
    def stop_rules_processing(self, stop_rules_processing):
        """
        Sets the stop_rules_processing of this SalesRuleDataRuleInterface.
        To stop rule processing

        :param stop_rules_processing: The stop_rules_processing of this SalesRuleDataRuleInterface.
        :type: bool
        """
        if stop_rules_processing is None:
            raise ValueError("Invalid value for `stop_rules_processing`, must not be `None`")

        self._stop_rules_processing = stop_rules_processing

    @property
    def is_advanced(self):
        """
        Gets the is_advanced of this SalesRuleDataRuleInterface.
        Is this field needed

        :return: The is_advanced of this SalesRuleDataRuleInterface.
        :rtype: bool
        """
        return self._is_advanced

    @is_advanced.setter
    def is_advanced(self, is_advanced):
        """
        Sets the is_advanced of this SalesRuleDataRuleInterface.
        Is this field needed

        :param is_advanced: The is_advanced of this SalesRuleDataRuleInterface.
        :type: bool
        """
        if is_advanced is None:
            raise ValueError("Invalid value for `is_advanced`, must not be `None`")

        self._is_advanced = is_advanced

    @property
    def product_ids(self):
        """
        Gets the product_ids of this SalesRuleDataRuleInterface.
        Product ids

        :return: The product_ids of this SalesRuleDataRuleInterface.
        :rtype: list[int]
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """
        Sets the product_ids of this SalesRuleDataRuleInterface.
        Product ids

        :param product_ids: The product_ids of this SalesRuleDataRuleInterface.
        :type: list[int]
        """

        self._product_ids = product_ids

    @property
    def sort_order(self):
        """
        Gets the sort_order of this SalesRuleDataRuleInterface.
        Sort order

        :return: The sort_order of this SalesRuleDataRuleInterface.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this SalesRuleDataRuleInterface.
        Sort order

        :param sort_order: The sort_order of this SalesRuleDataRuleInterface.
        :type: int
        """
        if sort_order is None:
            raise ValueError("Invalid value for `sort_order`, must not be `None`")

        self._sort_order = sort_order

    @property
    def simple_action(self):
        """
        Gets the simple_action of this SalesRuleDataRuleInterface.
        Simple action of the rule

        :return: The simple_action of this SalesRuleDataRuleInterface.
        :rtype: str
        """
        return self._simple_action

    @simple_action.setter
    def simple_action(self, simple_action):
        """
        Sets the simple_action of this SalesRuleDataRuleInterface.
        Simple action of the rule

        :param simple_action: The simple_action of this SalesRuleDataRuleInterface.
        :type: str
        """

        self._simple_action = simple_action

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this SalesRuleDataRuleInterface.
        Discount amount

        :return: The discount_amount of this SalesRuleDataRuleInterface.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this SalesRuleDataRuleInterface.
        Discount amount

        :param discount_amount: The discount_amount of this SalesRuleDataRuleInterface.
        :type: float
        """
        if discount_amount is None:
            raise ValueError("Invalid value for `discount_amount`, must not be `None`")

        self._discount_amount = discount_amount

    @property
    def discount_qty(self):
        """
        Gets the discount_qty of this SalesRuleDataRuleInterface.
        Maximum qty discount is applied

        :return: The discount_qty of this SalesRuleDataRuleInterface.
        :rtype: float
        """
        return self._discount_qty

    @discount_qty.setter
    def discount_qty(self, discount_qty):
        """
        Sets the discount_qty of this SalesRuleDataRuleInterface.
        Maximum qty discount is applied

        :param discount_qty: The discount_qty of this SalesRuleDataRuleInterface.
        :type: float
        """

        self._discount_qty = discount_qty

    @property
    def discount_step(self):
        """
        Gets the discount_step of this SalesRuleDataRuleInterface.
        Discount step

        :return: The discount_step of this SalesRuleDataRuleInterface.
        :rtype: int
        """
        return self._discount_step

    @discount_step.setter
    def discount_step(self, discount_step):
        """
        Sets the discount_step of this SalesRuleDataRuleInterface.
        Discount step

        :param discount_step: The discount_step of this SalesRuleDataRuleInterface.
        :type: int
        """
        if discount_step is None:
            raise ValueError("Invalid value for `discount_step`, must not be `None`")

        self._discount_step = discount_step

    @property
    def apply_to_shipping(self):
        """
        Gets the apply_to_shipping of this SalesRuleDataRuleInterface.
        The rule applies to shipping

        :return: The apply_to_shipping of this SalesRuleDataRuleInterface.
        :rtype: bool
        """
        return self._apply_to_shipping

    @apply_to_shipping.setter
    def apply_to_shipping(self, apply_to_shipping):
        """
        Sets the apply_to_shipping of this SalesRuleDataRuleInterface.
        The rule applies to shipping

        :param apply_to_shipping: The apply_to_shipping of this SalesRuleDataRuleInterface.
        :type: bool
        """
        if apply_to_shipping is None:
            raise ValueError("Invalid value for `apply_to_shipping`, must not be `None`")

        self._apply_to_shipping = apply_to_shipping

    @property
    def times_used(self):
        """
        Gets the times_used of this SalesRuleDataRuleInterface.
        How many times the rule has been used

        :return: The times_used of this SalesRuleDataRuleInterface.
        :rtype: int
        """
        return self._times_used

    @times_used.setter
    def times_used(self, times_used):
        """
        Sets the times_used of this SalesRuleDataRuleInterface.
        How many times the rule has been used

        :param times_used: The times_used of this SalesRuleDataRuleInterface.
        :type: int
        """
        if times_used is None:
            raise ValueError("Invalid value for `times_used`, must not be `None`")

        self._times_used = times_used

    @property
    def is_rss(self):
        """
        Gets the is_rss of this SalesRuleDataRuleInterface.
        Whether the rule is in RSS

        :return: The is_rss of this SalesRuleDataRuleInterface.
        :rtype: bool
        """
        return self._is_rss

    @is_rss.setter
    def is_rss(self, is_rss):
        """
        Sets the is_rss of this SalesRuleDataRuleInterface.
        Whether the rule is in RSS

        :param is_rss: The is_rss of this SalesRuleDataRuleInterface.
        :type: bool
        """
        if is_rss is None:
            raise ValueError("Invalid value for `is_rss`, must not be `None`")

        self._is_rss = is_rss

    @property
    def coupon_type(self):
        """
        Gets the coupon_type of this SalesRuleDataRuleInterface.
        Coupon type

        :return: The coupon_type of this SalesRuleDataRuleInterface.
        :rtype: str
        """
        return self._coupon_type

    @coupon_type.setter
    def coupon_type(self, coupon_type):
        """
        Sets the coupon_type of this SalesRuleDataRuleInterface.
        Coupon type

        :param coupon_type: The coupon_type of this SalesRuleDataRuleInterface.
        :type: str
        """
        if coupon_type is None:
            raise ValueError("Invalid value for `coupon_type`, must not be `None`")

        self._coupon_type = coupon_type

    @property
    def use_auto_generation(self):
        """
        Gets the use_auto_generation of this SalesRuleDataRuleInterface.
        To auto generate coupon

        :return: The use_auto_generation of this SalesRuleDataRuleInterface.
        :rtype: bool
        """
        return self._use_auto_generation

    @use_auto_generation.setter
    def use_auto_generation(self, use_auto_generation):
        """
        Sets the use_auto_generation of this SalesRuleDataRuleInterface.
        To auto generate coupon

        :param use_auto_generation: The use_auto_generation of this SalesRuleDataRuleInterface.
        :type: bool
        """
        if use_auto_generation is None:
            raise ValueError("Invalid value for `use_auto_generation`, must not be `None`")

        self._use_auto_generation = use_auto_generation

    @property
    def uses_per_coupon(self):
        """
        Gets the uses_per_coupon of this SalesRuleDataRuleInterface.
        Limit of uses per coupon

        :return: The uses_per_coupon of this SalesRuleDataRuleInterface.
        :rtype: int
        """
        return self._uses_per_coupon

    @uses_per_coupon.setter
    def uses_per_coupon(self, uses_per_coupon):
        """
        Sets the uses_per_coupon of this SalesRuleDataRuleInterface.
        Limit of uses per coupon

        :param uses_per_coupon: The uses_per_coupon of this SalesRuleDataRuleInterface.
        :type: int
        """
        if uses_per_coupon is None:
            raise ValueError("Invalid value for `uses_per_coupon`, must not be `None`")

        self._uses_per_coupon = uses_per_coupon

    @property
    def simple_free_shipping(self):
        """
        Gets the simple_free_shipping of this SalesRuleDataRuleInterface.
        To grant free shipping

        :return: The simple_free_shipping of this SalesRuleDataRuleInterface.
        :rtype: str
        """
        return self._simple_free_shipping

    @simple_free_shipping.setter
    def simple_free_shipping(self, simple_free_shipping):
        """
        Sets the simple_free_shipping of this SalesRuleDataRuleInterface.
        To grant free shipping

        :param simple_free_shipping: The simple_free_shipping of this SalesRuleDataRuleInterface.
        :type: str
        """

        self._simple_free_shipping = simple_free_shipping

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesRuleDataRuleInterface.

        :return: The extension_attributes of this SalesRuleDataRuleInterface.
        :rtype: SalesRuleDataRuleExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesRuleDataRuleInterface.

        :param extension_attributes: The extension_attributes of this SalesRuleDataRuleInterface.
        :type: SalesRuleDataRuleExtensionInterface
        """

        self._extension_attributes = extension_attributes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SalesRuleDataRuleInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
