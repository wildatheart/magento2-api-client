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


class CatalogDataSpecialPriceInterface(object):
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
        'price': 'float',
        'store_id': 'int',
        'sku': 'str',
        'price_from': 'str',
        'price_to': 'str',
        'extension_attributes': 'CatalogDataSpecialPriceExtensionInterface'
    }

    attribute_map = {
        'price': 'price',
        'store_id': 'store_id',
        'sku': 'sku',
        'price_from': 'price_from',
        'price_to': 'price_to',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, price=None, store_id=None, sku=None, price_from=None, price_to=None, extension_attributes=None):
        """
        CatalogDataSpecialPriceInterface - a model defined in Swagger
        """

        self._price = None
        self._store_id = None
        self._sku = None
        self._price_from = None
        self._price_to = None
        self._extension_attributes = None

        self.price = price
        self.store_id = store_id
        self.sku = sku
        self.price_from = price_from
        self.price_to = price_to
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def price(self):
        """
        Gets the price of this CatalogDataSpecialPriceInterface.
        Product special price value.

        :return: The price of this CatalogDataSpecialPriceInterface.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this CatalogDataSpecialPriceInterface.
        Product special price value.

        :param price: The price of this CatalogDataSpecialPriceInterface.
        :type: float
        """
        if price is None:
            raise ValueError("Invalid value for `price`, must not be `None`")

        self._price = price

    @property
    def store_id(self):
        """
        Gets the store_id of this CatalogDataSpecialPriceInterface.
        ID of store, that contains special price value.

        :return: The store_id of this CatalogDataSpecialPriceInterface.
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """
        Sets the store_id of this CatalogDataSpecialPriceInterface.
        ID of store, that contains special price value.

        :param store_id: The store_id of this CatalogDataSpecialPriceInterface.
        :type: int
        """
        if store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")

        self._store_id = store_id

    @property
    def sku(self):
        """
        Gets the sku of this CatalogDataSpecialPriceInterface.
        SKU of product, that contains special price value.

        :return: The sku of this CatalogDataSpecialPriceInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this CatalogDataSpecialPriceInterface.
        SKU of product, that contains special price value.

        :param sku: The sku of this CatalogDataSpecialPriceInterface.
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def price_from(self):
        """
        Gets the price_from of this CatalogDataSpecialPriceInterface.
        Start date for special price in Y-m-d H:i:s format.

        :return: The price_from of this CatalogDataSpecialPriceInterface.
        :rtype: str
        """
        return self._price_from

    @price_from.setter
    def price_from(self, price_from):
        """
        Sets the price_from of this CatalogDataSpecialPriceInterface.
        Start date for special price in Y-m-d H:i:s format.

        :param price_from: The price_from of this CatalogDataSpecialPriceInterface.
        :type: str
        """
        if price_from is None:
            raise ValueError("Invalid value for `price_from`, must not be `None`")

        self._price_from = price_from

    @property
    def price_to(self):
        """
        Gets the price_to of this CatalogDataSpecialPriceInterface.
        End date for special price in Y-m-d H:i:s format.

        :return: The price_to of this CatalogDataSpecialPriceInterface.
        :rtype: str
        """
        return self._price_to

    @price_to.setter
    def price_to(self, price_to):
        """
        Sets the price_to of this CatalogDataSpecialPriceInterface.
        End date for special price in Y-m-d H:i:s format.

        :param price_to: The price_to of this CatalogDataSpecialPriceInterface.
        :type: str
        """
        if price_to is None:
            raise ValueError("Invalid value for `price_to`, must not be `None`")

        self._price_to = price_to

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CatalogDataSpecialPriceInterface.

        :return: The extension_attributes of this CatalogDataSpecialPriceInterface.
        :rtype: CatalogDataSpecialPriceExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CatalogDataSpecialPriceInterface.

        :param extension_attributes: The extension_attributes of this CatalogDataSpecialPriceInterface.
        :type: CatalogDataSpecialPriceExtensionInterface
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
        if not isinstance(other, CatalogDataSpecialPriceInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other