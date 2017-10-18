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


class Body129(object):
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
        'codes': 'list[str]',
        'ignore_invalid_coupons': 'bool'
    }

    attribute_map = {
        'codes': 'codes',
        'ignore_invalid_coupons': 'ignoreInvalidCoupons'
    }

    def __init__(self, codes=None, ignore_invalid_coupons=None):
        """
        Body129 - a model defined in Swagger
        """

        self._codes = None
        self._ignore_invalid_coupons = None

        self.codes = codes
        if ignore_invalid_coupons is not None:
          self.ignore_invalid_coupons = ignore_invalid_coupons

    @property
    def codes(self):
        """
        Gets the codes of this Body129.

        :return: The codes of this Body129.
        :rtype: list[str]
        """
        return self._codes

    @codes.setter
    def codes(self, codes):
        """
        Sets the codes of this Body129.

        :param codes: The codes of this Body129.
        :type: list[str]
        """
        if codes is None:
            raise ValueError("Invalid value for `codes`, must not be `None`")

        self._codes = codes

    @property
    def ignore_invalid_coupons(self):
        """
        Gets the ignore_invalid_coupons of this Body129.

        :return: The ignore_invalid_coupons of this Body129.
        :rtype: bool
        """
        return self._ignore_invalid_coupons

    @ignore_invalid_coupons.setter
    def ignore_invalid_coupons(self, ignore_invalid_coupons):
        """
        Sets the ignore_invalid_coupons of this Body129.

        :param ignore_invalid_coupons: The ignore_invalid_coupons of this Body129.
        :type: bool
        """

        self._ignore_invalid_coupons = ignore_invalid_coupons

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
        if not isinstance(other, Body129):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
