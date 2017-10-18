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


class Body78(object):
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
        'stock_item': 'CatalogInventoryDataStockItemInterface'
    }

    attribute_map = {
        'stock_item': 'stockItem'
    }

    def __init__(self, stock_item=None):
        """
        Body78 - a model defined in Swagger
        """

        self._stock_item = None

        self.stock_item = stock_item

    @property
    def stock_item(self):
        """
        Gets the stock_item of this Body78.

        :return: The stock_item of this Body78.
        :rtype: CatalogInventoryDataStockItemInterface
        """
        return self._stock_item

    @stock_item.setter
    def stock_item(self, stock_item):
        """
        Sets the stock_item of this Body78.

        :param stock_item: The stock_item of this Body78.
        :type: CatalogInventoryDataStockItemInterface
        """
        if stock_item is None:
            raise ValueError("Invalid value for `stock_item`, must not be `None`")

        self._stock_item = stock_item

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
        if not isinstance(other, Body78):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
