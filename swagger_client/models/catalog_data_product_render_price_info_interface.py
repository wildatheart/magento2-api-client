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


class CatalogDataProductRenderPriceInfoInterface(object):
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
        'final_price': 'float',
        'max_price': 'float',
        'max_regular_price': 'float',
        'minimal_regular_price': 'float',
        'special_price': 'float',
        'minimal_price': 'float',
        'regular_price': 'float',
        'formatted_prices': 'CatalogDataProductRenderFormattedPriceInfoInterface',
        'extension_attributes': 'CatalogDataProductRenderPriceInfoExtensionInterface'
    }

    attribute_map = {
        'final_price': 'final_price',
        'max_price': 'max_price',
        'max_regular_price': 'max_regular_price',
        'minimal_regular_price': 'minimal_regular_price',
        'special_price': 'special_price',
        'minimal_price': 'minimal_price',
        'regular_price': 'regular_price',
        'formatted_prices': 'formatted_prices',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, final_price=None, max_price=None, max_regular_price=None, minimal_regular_price=None, special_price=None, minimal_price=None, regular_price=None, formatted_prices=None, extension_attributes=None):
        """
        CatalogDataProductRenderPriceInfoInterface - a model defined in Swagger
        """

        self._final_price = None
        self._max_price = None
        self._max_regular_price = None
        self._minimal_regular_price = None
        self._special_price = None
        self._minimal_price = None
        self._regular_price = None
        self._formatted_prices = None
        self._extension_attributes = None

        self.final_price = final_price
        self.max_price = max_price
        self.max_regular_price = max_regular_price
        self.minimal_regular_price = minimal_regular_price
        self.special_price = special_price
        self.minimal_price = minimal_price
        self.regular_price = regular_price
        self.formatted_prices = formatted_prices
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def final_price(self):
        """
        Gets the final_price of this CatalogDataProductRenderPriceInfoInterface.
        Final price

        :return: The final_price of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: float
        """
        return self._final_price

    @final_price.setter
    def final_price(self, final_price):
        """
        Sets the final_price of this CatalogDataProductRenderPriceInfoInterface.
        Final price

        :param final_price: The final_price of this CatalogDataProductRenderPriceInfoInterface.
        :type: float
        """
        if final_price is None:
            raise ValueError("Invalid value for `final_price`, must not be `None`")

        self._final_price = final_price

    @property
    def max_price(self):
        """
        Gets the max_price of this CatalogDataProductRenderPriceInfoInterface.
        Max price of a product

        :return: The max_price of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: float
        """
        return self._max_price

    @max_price.setter
    def max_price(self, max_price):
        """
        Sets the max_price of this CatalogDataProductRenderPriceInfoInterface.
        Max price of a product

        :param max_price: The max_price of this CatalogDataProductRenderPriceInfoInterface.
        :type: float
        """
        if max_price is None:
            raise ValueError("Invalid value for `max_price`, must not be `None`")

        self._max_price = max_price

    @property
    def max_regular_price(self):
        """
        Gets the max_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        Max regular price

        :return: The max_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: float
        """
        return self._max_regular_price

    @max_regular_price.setter
    def max_regular_price(self, max_regular_price):
        """
        Sets the max_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        Max regular price

        :param max_regular_price: The max_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        :type: float
        """
        if max_regular_price is None:
            raise ValueError("Invalid value for `max_regular_price`, must not be `None`")

        self._max_regular_price = max_regular_price

    @property
    def minimal_regular_price(self):
        """
        Gets the minimal_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        Minimal regular price

        :return: The minimal_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: float
        """
        return self._minimal_regular_price

    @minimal_regular_price.setter
    def minimal_regular_price(self, minimal_regular_price):
        """
        Sets the minimal_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        Minimal regular price

        :param minimal_regular_price: The minimal_regular_price of this CatalogDataProductRenderPriceInfoInterface.
        :type: float
        """
        if minimal_regular_price is None:
            raise ValueError("Invalid value for `minimal_regular_price`, must not be `None`")

        self._minimal_regular_price = minimal_regular_price

    @property
    def special_price(self):
        """
        Gets the special_price of this CatalogDataProductRenderPriceInfoInterface.
        Special price

        :return: The special_price of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: float
        """
        return self._special_price

    @special_price.setter
    def special_price(self, special_price):
        """
        Sets the special_price of this CatalogDataProductRenderPriceInfoInterface.
        Special price

        :param special_price: The special_price of this CatalogDataProductRenderPriceInfoInterface.
        :type: float
        """
        if special_price is None:
            raise ValueError("Invalid value for `special_price`, must not be `None`")

        self._special_price = special_price

    @property
    def minimal_price(self):
        """
        Gets the minimal_price of this CatalogDataProductRenderPriceInfoInterface.

        :return: The minimal_price of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: float
        """
        return self._minimal_price

    @minimal_price.setter
    def minimal_price(self, minimal_price):
        """
        Sets the minimal_price of this CatalogDataProductRenderPriceInfoInterface.

        :param minimal_price: The minimal_price of this CatalogDataProductRenderPriceInfoInterface.
        :type: float
        """
        if minimal_price is None:
            raise ValueError("Invalid value for `minimal_price`, must not be `None`")

        self._minimal_price = minimal_price

    @property
    def regular_price(self):
        """
        Gets the regular_price of this CatalogDataProductRenderPriceInfoInterface.
        Regular price

        :return: The regular_price of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: float
        """
        return self._regular_price

    @regular_price.setter
    def regular_price(self, regular_price):
        """
        Sets the regular_price of this CatalogDataProductRenderPriceInfoInterface.
        Regular price

        :param regular_price: The regular_price of this CatalogDataProductRenderPriceInfoInterface.
        :type: float
        """
        if regular_price is None:
            raise ValueError("Invalid value for `regular_price`, must not be `None`")

        self._regular_price = regular_price

    @property
    def formatted_prices(self):
        """
        Gets the formatted_prices of this CatalogDataProductRenderPriceInfoInterface.

        :return: The formatted_prices of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: CatalogDataProductRenderFormattedPriceInfoInterface
        """
        return self._formatted_prices

    @formatted_prices.setter
    def formatted_prices(self, formatted_prices):
        """
        Sets the formatted_prices of this CatalogDataProductRenderPriceInfoInterface.

        :param formatted_prices: The formatted_prices of this CatalogDataProductRenderPriceInfoInterface.
        :type: CatalogDataProductRenderFormattedPriceInfoInterface
        """
        if formatted_prices is None:
            raise ValueError("Invalid value for `formatted_prices`, must not be `None`")

        self._formatted_prices = formatted_prices

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CatalogDataProductRenderPriceInfoInterface.

        :return: The extension_attributes of this CatalogDataProductRenderPriceInfoInterface.
        :rtype: CatalogDataProductRenderPriceInfoExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CatalogDataProductRenderPriceInfoInterface.

        :param extension_attributes: The extension_attributes of this CatalogDataProductRenderPriceInfoInterface.
        :type: CatalogDataProductRenderPriceInfoExtensionInterface
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
        if not isinstance(other, CatalogDataProductRenderPriceInfoInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
