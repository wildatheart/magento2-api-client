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


class Body74(object):
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
        'address': 'QuoteDataAddressInterface',
        'use_for_shipping': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'use_for_shipping': 'useForShipping'
    }

    def __init__(self, address=None, use_for_shipping=None):
        """
        Body74 - a model defined in Swagger
        """

        self._address = None
        self._use_for_shipping = None

        self.address = address
        if use_for_shipping is not None:
          self.use_for_shipping = use_for_shipping

    @property
    def address(self):
        """
        Gets the address of this Body74.

        :return: The address of this Body74.
        :rtype: QuoteDataAddressInterface
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Body74.

        :param address: The address of this Body74.
        :type: QuoteDataAddressInterface
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")

        self._address = address

    @property
    def use_for_shipping(self):
        """
        Gets the use_for_shipping of this Body74.

        :return: The use_for_shipping of this Body74.
        :rtype: bool
        """
        return self._use_for_shipping

    @use_for_shipping.setter
    def use_for_shipping(self, use_for_shipping):
        """
        Sets the use_for_shipping of this Body74.

        :param use_for_shipping: The use_for_shipping of this Body74.
        :type: bool
        """

        self._use_for_shipping = use_for_shipping

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
        if not isinstance(other, Body74):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
