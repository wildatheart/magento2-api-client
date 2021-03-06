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


class Body50(object):
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
        'product_link': 'CatalogDataCategoryProductLinkInterface'
    }

    attribute_map = {
        'product_link': 'productLink'
    }

    def __init__(self, product_link=None):
        """
        Body50 - a model defined in Swagger
        """

        self._product_link = None

        self.product_link = product_link

    @property
    def product_link(self):
        """
        Gets the product_link of this Body50.

        :return: The product_link of this Body50.
        :rtype: CatalogDataCategoryProductLinkInterface
        """
        return self._product_link

    @product_link.setter
    def product_link(self, product_link):
        """
        Sets the product_link of this Body50.

        :param product_link: The product_link of this Body50.
        :type: CatalogDataCategoryProductLinkInterface
        """
        if product_link is None:
            raise ValueError("Invalid value for `product_link`, must not be `None`")

        self._product_link = product_link

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
        if not isinstance(other, Body50):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
