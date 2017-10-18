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


class SalesDataInvoiceItemInterface(object):
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
        'additional_data': 'str',
        'base_cost': 'float',
        'base_discount_amount': 'float',
        'base_discount_tax_compensation_amount': 'float',
        'base_price': 'float',
        'base_price_incl_tax': 'float',
        'base_row_total': 'float',
        'base_row_total_incl_tax': 'float',
        'base_tax_amount': 'float',
        'description': 'str',
        'discount_amount': 'float',
        'entity_id': 'int',
        'discount_tax_compensation_amount': 'float',
        'name': 'str',
        'parent_id': 'int',
        'price': 'float',
        'price_incl_tax': 'float',
        'product_id': 'int',
        'row_total': 'float',
        'row_total_incl_tax': 'float',
        'sku': 'str',
        'tax_amount': 'float',
        'extension_attributes': 'SalesDataInvoiceItemExtensionInterface',
        'order_item_id': 'int',
        'qty': 'float'
    }

    attribute_map = {
        'additional_data': 'additional_data',
        'base_cost': 'base_cost',
        'base_discount_amount': 'base_discount_amount',
        'base_discount_tax_compensation_amount': 'base_discount_tax_compensation_amount',
        'base_price': 'base_price',
        'base_price_incl_tax': 'base_price_incl_tax',
        'base_row_total': 'base_row_total',
        'base_row_total_incl_tax': 'base_row_total_incl_tax',
        'base_tax_amount': 'base_tax_amount',
        'description': 'description',
        'discount_amount': 'discount_amount',
        'entity_id': 'entity_id',
        'discount_tax_compensation_amount': 'discount_tax_compensation_amount',
        'name': 'name',
        'parent_id': 'parent_id',
        'price': 'price',
        'price_incl_tax': 'price_incl_tax',
        'product_id': 'product_id',
        'row_total': 'row_total',
        'row_total_incl_tax': 'row_total_incl_tax',
        'sku': 'sku',
        'tax_amount': 'tax_amount',
        'extension_attributes': 'extension_attributes',
        'order_item_id': 'order_item_id',
        'qty': 'qty'
    }

    def __init__(self, additional_data=None, base_cost=None, base_discount_amount=None, base_discount_tax_compensation_amount=None, base_price=None, base_price_incl_tax=None, base_row_total=None, base_row_total_incl_tax=None, base_tax_amount=None, description=None, discount_amount=None, entity_id=None, discount_tax_compensation_amount=None, name=None, parent_id=None, price=None, price_incl_tax=None, product_id=None, row_total=None, row_total_incl_tax=None, sku=None, tax_amount=None, extension_attributes=None, order_item_id=None, qty=None):
        """
        SalesDataInvoiceItemInterface - a model defined in Swagger
        """

        self._additional_data = None
        self._base_cost = None
        self._base_discount_amount = None
        self._base_discount_tax_compensation_amount = None
        self._base_price = None
        self._base_price_incl_tax = None
        self._base_row_total = None
        self._base_row_total_incl_tax = None
        self._base_tax_amount = None
        self._description = None
        self._discount_amount = None
        self._entity_id = None
        self._discount_tax_compensation_amount = None
        self._name = None
        self._parent_id = None
        self._price = None
        self._price_incl_tax = None
        self._product_id = None
        self._row_total = None
        self._row_total_incl_tax = None
        self._sku = None
        self._tax_amount = None
        self._extension_attributes = None
        self._order_item_id = None
        self._qty = None

        if additional_data is not None:
          self.additional_data = additional_data
        if base_cost is not None:
          self.base_cost = base_cost
        if base_discount_amount is not None:
          self.base_discount_amount = base_discount_amount
        if base_discount_tax_compensation_amount is not None:
          self.base_discount_tax_compensation_amount = base_discount_tax_compensation_amount
        if base_price is not None:
          self.base_price = base_price
        if base_price_incl_tax is not None:
          self.base_price_incl_tax = base_price_incl_tax
        if base_row_total is not None:
          self.base_row_total = base_row_total
        if base_row_total_incl_tax is not None:
          self.base_row_total_incl_tax = base_row_total_incl_tax
        if base_tax_amount is not None:
          self.base_tax_amount = base_tax_amount
        if description is not None:
          self.description = description
        if discount_amount is not None:
          self.discount_amount = discount_amount
        if entity_id is not None:
          self.entity_id = entity_id
        if discount_tax_compensation_amount is not None:
          self.discount_tax_compensation_amount = discount_tax_compensation_amount
        if name is not None:
          self.name = name
        if parent_id is not None:
          self.parent_id = parent_id
        if price is not None:
          self.price = price
        if price_incl_tax is not None:
          self.price_incl_tax = price_incl_tax
        if product_id is not None:
          self.product_id = product_id
        if row_total is not None:
          self.row_total = row_total
        if row_total_incl_tax is not None:
          self.row_total_incl_tax = row_total_incl_tax
        self.sku = sku
        if tax_amount is not None:
          self.tax_amount = tax_amount
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes
        self.order_item_id = order_item_id
        self.qty = qty

    @property
    def additional_data(self):
        """
        Gets the additional_data of this SalesDataInvoiceItemInterface.
        Additional data.

        :return: The additional_data of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """
        Sets the additional_data of this SalesDataInvoiceItemInterface.
        Additional data.

        :param additional_data: The additional_data of this SalesDataInvoiceItemInterface.
        :type: str
        """

        self._additional_data = additional_data

    @property
    def base_cost(self):
        """
        Gets the base_cost of this SalesDataInvoiceItemInterface.
        Base cost.

        :return: The base_cost of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_cost

    @base_cost.setter
    def base_cost(self, base_cost):
        """
        Sets the base_cost of this SalesDataInvoiceItemInterface.
        Base cost.

        :param base_cost: The base_cost of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_cost = base_cost

    @property
    def base_discount_amount(self):
        """
        Gets the base_discount_amount of this SalesDataInvoiceItemInterface.
        Base discount amount.

        :return: The base_discount_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_discount_amount

    @base_discount_amount.setter
    def base_discount_amount(self, base_discount_amount):
        """
        Sets the base_discount_amount of this SalesDataInvoiceItemInterface.
        Base discount amount.

        :param base_discount_amount: The base_discount_amount of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_discount_amount = base_discount_amount

    @property
    def base_discount_tax_compensation_amount(self):
        """
        Gets the base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        Base discount tax compensation amount.

        :return: The base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_discount_tax_compensation_amount

    @base_discount_tax_compensation_amount.setter
    def base_discount_tax_compensation_amount(self, base_discount_tax_compensation_amount):
        """
        Sets the base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        Base discount tax compensation amount.

        :param base_discount_tax_compensation_amount: The base_discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_discount_tax_compensation_amount = base_discount_tax_compensation_amount

    @property
    def base_price(self):
        """
        Gets the base_price of this SalesDataInvoiceItemInterface.
        Base price.

        :return: The base_price of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_price

    @base_price.setter
    def base_price(self, base_price):
        """
        Sets the base_price of this SalesDataInvoiceItemInterface.
        Base price.

        :param base_price: The base_price of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_price = base_price

    @property
    def base_price_incl_tax(self):
        """
        Gets the base_price_incl_tax of this SalesDataInvoiceItemInterface.
        Base price including tax.

        :return: The base_price_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_price_incl_tax

    @base_price_incl_tax.setter
    def base_price_incl_tax(self, base_price_incl_tax):
        """
        Sets the base_price_incl_tax of this SalesDataInvoiceItemInterface.
        Base price including tax.

        :param base_price_incl_tax: The base_price_incl_tax of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_price_incl_tax = base_price_incl_tax

    @property
    def base_row_total(self):
        """
        Gets the base_row_total of this SalesDataInvoiceItemInterface.
        Base row total.

        :return: The base_row_total of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_row_total

    @base_row_total.setter
    def base_row_total(self, base_row_total):
        """
        Sets the base_row_total of this SalesDataInvoiceItemInterface.
        Base row total.

        :param base_row_total: The base_row_total of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_row_total = base_row_total

    @property
    def base_row_total_incl_tax(self):
        """
        Gets the base_row_total_incl_tax of this SalesDataInvoiceItemInterface.
        Base row total including tax.

        :return: The base_row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_row_total_incl_tax

    @base_row_total_incl_tax.setter
    def base_row_total_incl_tax(self, base_row_total_incl_tax):
        """
        Sets the base_row_total_incl_tax of this SalesDataInvoiceItemInterface.
        Base row total including tax.

        :param base_row_total_incl_tax: The base_row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_row_total_incl_tax = base_row_total_incl_tax

    @property
    def base_tax_amount(self):
        """
        Gets the base_tax_amount of this SalesDataInvoiceItemInterface.
        Base tax amount.

        :return: The base_tax_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._base_tax_amount

    @base_tax_amount.setter
    def base_tax_amount(self, base_tax_amount):
        """
        Sets the base_tax_amount of this SalesDataInvoiceItemInterface.
        Base tax amount.

        :param base_tax_amount: The base_tax_amount of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._base_tax_amount = base_tax_amount

    @property
    def description(self):
        """
        Gets the description of this SalesDataInvoiceItemInterface.
        Description.

        :return: The description of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SalesDataInvoiceItemInterface.
        Description.

        :param description: The description of this SalesDataInvoiceItemInterface.
        :type: str
        """

        self._description = description

    @property
    def discount_amount(self):
        """
        Gets the discount_amount of this SalesDataInvoiceItemInterface.
        Discount amount.

        :return: The discount_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """
        Sets the discount_amount of this SalesDataInvoiceItemInterface.
        Discount amount.

        :param discount_amount: The discount_amount of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def entity_id(self):
        """
        Gets the entity_id of this SalesDataInvoiceItemInterface.
        Invoice item ID.

        :return: The entity_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this SalesDataInvoiceItemInterface.
        Invoice item ID.

        :param entity_id: The entity_id of this SalesDataInvoiceItemInterface.
        :type: int
        """

        self._entity_id = entity_id

    @property
    def discount_tax_compensation_amount(self):
        """
        Gets the discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        Discount tax compensation amount.

        :return: The discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._discount_tax_compensation_amount

    @discount_tax_compensation_amount.setter
    def discount_tax_compensation_amount(self, discount_tax_compensation_amount):
        """
        Sets the discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        Discount tax compensation amount.

        :param discount_tax_compensation_amount: The discount_tax_compensation_amount of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._discount_tax_compensation_amount = discount_tax_compensation_amount

    @property
    def name(self):
        """
        Gets the name of this SalesDataInvoiceItemInterface.
        Name.

        :return: The name of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SalesDataInvoiceItemInterface.
        Name.

        :param name: The name of this SalesDataInvoiceItemInterface.
        :type: str
        """

        self._name = name

    @property
    def parent_id(self):
        """
        Gets the parent_id of this SalesDataInvoiceItemInterface.
        Parent ID.

        :return: The parent_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this SalesDataInvoiceItemInterface.
        Parent ID.

        :param parent_id: The parent_id of this SalesDataInvoiceItemInterface.
        :type: int
        """

        self._parent_id = parent_id

    @property
    def price(self):
        """
        Gets the price of this SalesDataInvoiceItemInterface.
        Price.

        :return: The price of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this SalesDataInvoiceItemInterface.
        Price.

        :param price: The price of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._price = price

    @property
    def price_incl_tax(self):
        """
        Gets the price_incl_tax of this SalesDataInvoiceItemInterface.
        Price including tax.

        :return: The price_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._price_incl_tax

    @price_incl_tax.setter
    def price_incl_tax(self, price_incl_tax):
        """
        Sets the price_incl_tax of this SalesDataInvoiceItemInterface.
        Price including tax.

        :param price_incl_tax: The price_incl_tax of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._price_incl_tax = price_incl_tax

    @property
    def product_id(self):
        """
        Gets the product_id of this SalesDataInvoiceItemInterface.
        Product ID.

        :return: The product_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this SalesDataInvoiceItemInterface.
        Product ID.

        :param product_id: The product_id of this SalesDataInvoiceItemInterface.
        :type: int
        """

        self._product_id = product_id

    @property
    def row_total(self):
        """
        Gets the row_total of this SalesDataInvoiceItemInterface.
        Row total.

        :return: The row_total of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._row_total

    @row_total.setter
    def row_total(self, row_total):
        """
        Sets the row_total of this SalesDataInvoiceItemInterface.
        Row total.

        :param row_total: The row_total of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._row_total = row_total

    @property
    def row_total_incl_tax(self):
        """
        Gets the row_total_incl_tax of this SalesDataInvoiceItemInterface.
        Row total including tax.

        :return: The row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._row_total_incl_tax

    @row_total_incl_tax.setter
    def row_total_incl_tax(self, row_total_incl_tax):
        """
        Sets the row_total_incl_tax of this SalesDataInvoiceItemInterface.
        Row total including tax.

        :param row_total_incl_tax: The row_total_incl_tax of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._row_total_incl_tax = row_total_incl_tax

    @property
    def sku(self):
        """
        Gets the sku of this SalesDataInvoiceItemInterface.
        SKU.

        :return: The sku of this SalesDataInvoiceItemInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this SalesDataInvoiceItemInterface.
        SKU.

        :param sku: The sku of this SalesDataInvoiceItemInterface.
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def tax_amount(self):
        """
        Gets the tax_amount of this SalesDataInvoiceItemInterface.
        Tax amount.

        :return: The tax_amount of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """
        Sets the tax_amount of this SalesDataInvoiceItemInterface.
        Tax amount.

        :param tax_amount: The tax_amount of this SalesDataInvoiceItemInterface.
        :type: float
        """

        self._tax_amount = tax_amount

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesDataInvoiceItemInterface.

        :return: The extension_attributes of this SalesDataInvoiceItemInterface.
        :rtype: SalesDataInvoiceItemExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesDataInvoiceItemInterface.

        :param extension_attributes: The extension_attributes of this SalesDataInvoiceItemInterface.
        :type: SalesDataInvoiceItemExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def order_item_id(self):
        """
        Gets the order_item_id of this SalesDataInvoiceItemInterface.
        Order item ID.

        :return: The order_item_id of this SalesDataInvoiceItemInterface.
        :rtype: int
        """
        return self._order_item_id

    @order_item_id.setter
    def order_item_id(self, order_item_id):
        """
        Sets the order_item_id of this SalesDataInvoiceItemInterface.
        Order item ID.

        :param order_item_id: The order_item_id of this SalesDataInvoiceItemInterface.
        :type: int
        """
        if order_item_id is None:
            raise ValueError("Invalid value for `order_item_id`, must not be `None`")

        self._order_item_id = order_item_id

    @property
    def qty(self):
        """
        Gets the qty of this SalesDataInvoiceItemInterface.
        Quantity.

        :return: The qty of this SalesDataInvoiceItemInterface.
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """
        Sets the qty of this SalesDataInvoiceItemInterface.
        Quantity.

        :param qty: The qty of this SalesDataInvoiceItemInterface.
        :type: float
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")

        self._qty = qty

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
        if not isinstance(other, SalesDataInvoiceItemInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
