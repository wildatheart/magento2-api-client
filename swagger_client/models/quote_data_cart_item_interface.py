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


class QuoteDataCartItemInterface(object):
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
        'item_id': 'int',
        'sku': 'str',
        'qty': 'float',
        'name': 'str',
        'price': 'float',
        'product_type': 'str',
        'quote_id': 'str',
        'product_option': 'QuoteDataProductOptionInterface',
        'extension_attributes': 'QuoteDataCartItemExtensionInterface'
    }

    attribute_map = {
        'item_id': 'item_id',
        'sku': 'sku',
        'qty': 'qty',
        'name': 'name',
        'price': 'price',
        'product_type': 'product_type',
        'quote_id': 'quote_id',
        'product_option': 'product_option',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, item_id=None, sku=None, qty=None, name=None, price=None, product_type=None, quote_id=None, product_option=None, extension_attributes=None):
        """
        QuoteDataCartItemInterface - a model defined in Swagger
        """

        self._item_id = None
        self._sku = None
        self._qty = None
        self._name = None
        self._price = None
        self._product_type = None
        self._quote_id = None
        self._product_option = None
        self._extension_attributes = None

        if item_id is not None:
          self.item_id = item_id
        if sku is not None:
          self.sku = sku
        self.qty = qty
        if name is not None:
          self.name = name
        if price is not None:
          self.price = price
        if product_type is not None:
          self.product_type = product_type
        self.quote_id = quote_id
        if product_option is not None:
          self.product_option = product_option
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def item_id(self):
        """
        Gets the item_id of this QuoteDataCartItemInterface.
        Item ID. Otherwise, null.

        :return: The item_id of this QuoteDataCartItemInterface.
        :rtype: int
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """
        Sets the item_id of this QuoteDataCartItemInterface.
        Item ID. Otherwise, null.

        :param item_id: The item_id of this QuoteDataCartItemInterface.
        :type: int
        """

        self._item_id = item_id

    @property
    def sku(self):
        """
        Gets the sku of this QuoteDataCartItemInterface.
        Product SKU. Otherwise, null.

        :return: The sku of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this QuoteDataCartItemInterface.
        Product SKU. Otherwise, null.

        :param sku: The sku of this QuoteDataCartItemInterface.
        :type: str
        """

        self._sku = sku

    @property
    def qty(self):
        """
        Gets the qty of this QuoteDataCartItemInterface.
        Product quantity.

        :return: The qty of this QuoteDataCartItemInterface.
        :rtype: float
        """
        return self._qty

    @qty.setter
    def qty(self, qty):
        """
        Sets the qty of this QuoteDataCartItemInterface.
        Product quantity.

        :param qty: The qty of this QuoteDataCartItemInterface.
        :type: float
        """
        if qty is None:
            raise ValueError("Invalid value for `qty`, must not be `None`")

        self._qty = qty

    @property
    def name(self):
        """
        Gets the name of this QuoteDataCartItemInterface.
        Product name. Otherwise, null.

        :return: The name of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this QuoteDataCartItemInterface.
        Product name. Otherwise, null.

        :param name: The name of this QuoteDataCartItemInterface.
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """
        Gets the price of this QuoteDataCartItemInterface.
        Product price. Otherwise, null.

        :return: The price of this QuoteDataCartItemInterface.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this QuoteDataCartItemInterface.
        Product price. Otherwise, null.

        :param price: The price of this QuoteDataCartItemInterface.
        :type: float
        """

        self._price = price

    @property
    def product_type(self):
        """
        Gets the product_type of this QuoteDataCartItemInterface.
        Product type. Otherwise, null.

        :return: The product_type of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """
        Sets the product_type of this QuoteDataCartItemInterface.
        Product type. Otherwise, null.

        :param product_type: The product_type of this QuoteDataCartItemInterface.
        :type: str
        """

        self._product_type = product_type

    @property
    def quote_id(self):
        """
        Gets the quote_id of this QuoteDataCartItemInterface.
        Quote id.

        :return: The quote_id of this QuoteDataCartItemInterface.
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """
        Sets the quote_id of this QuoteDataCartItemInterface.
        Quote id.

        :param quote_id: The quote_id of this QuoteDataCartItemInterface.
        :type: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")

        self._quote_id = quote_id

    @property
    def product_option(self):
        """
        Gets the product_option of this QuoteDataCartItemInterface.

        :return: The product_option of this QuoteDataCartItemInterface.
        :rtype: QuoteDataProductOptionInterface
        """
        return self._product_option

    @product_option.setter
    def product_option(self, product_option):
        """
        Sets the product_option of this QuoteDataCartItemInterface.

        :param product_option: The product_option of this QuoteDataCartItemInterface.
        :type: QuoteDataProductOptionInterface
        """

        self._product_option = product_option

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this QuoteDataCartItemInterface.

        :return: The extension_attributes of this QuoteDataCartItemInterface.
        :rtype: QuoteDataCartItemExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this QuoteDataCartItemInterface.

        :param extension_attributes: The extension_attributes of this QuoteDataCartItemInterface.
        :type: QuoteDataCartItemExtensionInterface
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
        if not isinstance(other, QuoteDataCartItemInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
