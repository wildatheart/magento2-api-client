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


class DirectoryDataExchangeRateInterface(object):
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
        'currency_to': 'str',
        'rate': 'float',
        'extension_attributes': 'DirectoryDataExchangeRateExtensionInterface'
    }

    attribute_map = {
        'currency_to': 'currency_to',
        'rate': 'rate',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, currency_to=None, rate=None, extension_attributes=None):
        """
        DirectoryDataExchangeRateInterface - a model defined in Swagger
        """

        self._currency_to = None
        self._rate = None
        self._extension_attributes = None

        self.currency_to = currency_to
        self.rate = rate
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def currency_to(self):
        """
        Gets the currency_to of this DirectoryDataExchangeRateInterface.
        The currency code associated with the exchange rate.

        :return: The currency_to of this DirectoryDataExchangeRateInterface.
        :rtype: str
        """
        return self._currency_to

    @currency_to.setter
    def currency_to(self, currency_to):
        """
        Sets the currency_to of this DirectoryDataExchangeRateInterface.
        The currency code associated with the exchange rate.

        :param currency_to: The currency_to of this DirectoryDataExchangeRateInterface.
        :type: str
        """
        if currency_to is None:
            raise ValueError("Invalid value for `currency_to`, must not be `None`")

        self._currency_to = currency_to

    @property
    def rate(self):
        """
        Gets the rate of this DirectoryDataExchangeRateInterface.
        The exchange rate for the associated currency and the store's base currency.

        :return: The rate of this DirectoryDataExchangeRateInterface.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this DirectoryDataExchangeRateInterface.
        The exchange rate for the associated currency and the store's base currency.

        :param rate: The rate of this DirectoryDataExchangeRateInterface.
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")

        self._rate = rate

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this DirectoryDataExchangeRateInterface.

        :return: The extension_attributes of this DirectoryDataExchangeRateInterface.
        :rtype: DirectoryDataExchangeRateExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this DirectoryDataExchangeRateInterface.

        :param extension_attributes: The extension_attributes of this DirectoryDataExchangeRateInterface.
        :type: DirectoryDataExchangeRateExtensionInterface
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
        if not isinstance(other, DirectoryDataExchangeRateInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
