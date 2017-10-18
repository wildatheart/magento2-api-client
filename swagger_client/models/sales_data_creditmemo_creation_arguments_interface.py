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


class SalesDataCreditmemoCreationArgumentsInterface(object):
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
        'shipping_amount': 'float',
        'adjustment_positive': 'float',
        'adjustment_negative': 'float',
        'extension_attributes': 'SalesDataCreditmemoCreationArgumentsExtensionInterface'
    }

    attribute_map = {
        'shipping_amount': 'shipping_amount',
        'adjustment_positive': 'adjustment_positive',
        'adjustment_negative': 'adjustment_negative',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, shipping_amount=None, adjustment_positive=None, adjustment_negative=None, extension_attributes=None):
        """
        SalesDataCreditmemoCreationArgumentsInterface - a model defined in Swagger
        """

        self._shipping_amount = None
        self._adjustment_positive = None
        self._adjustment_negative = None
        self._extension_attributes = None

        if shipping_amount is not None:
          self.shipping_amount = shipping_amount
        if adjustment_positive is not None:
          self.adjustment_positive = adjustment_positive
        if adjustment_negative is not None:
          self.adjustment_negative = adjustment_negative
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def shipping_amount(self):
        """
        Gets the shipping_amount of this SalesDataCreditmemoCreationArgumentsInterface.
        Credit memo shipping amount.

        :return: The shipping_amount of this SalesDataCreditmemoCreationArgumentsInterface.
        :rtype: float
        """
        return self._shipping_amount

    @shipping_amount.setter
    def shipping_amount(self, shipping_amount):
        """
        Sets the shipping_amount of this SalesDataCreditmemoCreationArgumentsInterface.
        Credit memo shipping amount.

        :param shipping_amount: The shipping_amount of this SalesDataCreditmemoCreationArgumentsInterface.
        :type: float
        """

        self._shipping_amount = shipping_amount

    @property
    def adjustment_positive(self):
        """
        Gets the adjustment_positive of this SalesDataCreditmemoCreationArgumentsInterface.
        Credit memo positive adjustment.

        :return: The adjustment_positive of this SalesDataCreditmemoCreationArgumentsInterface.
        :rtype: float
        """
        return self._adjustment_positive

    @adjustment_positive.setter
    def adjustment_positive(self, adjustment_positive):
        """
        Sets the adjustment_positive of this SalesDataCreditmemoCreationArgumentsInterface.
        Credit memo positive adjustment.

        :param adjustment_positive: The adjustment_positive of this SalesDataCreditmemoCreationArgumentsInterface.
        :type: float
        """

        self._adjustment_positive = adjustment_positive

    @property
    def adjustment_negative(self):
        """
        Gets the adjustment_negative of this SalesDataCreditmemoCreationArgumentsInterface.
        Credit memo negative adjustment.

        :return: The adjustment_negative of this SalesDataCreditmemoCreationArgumentsInterface.
        :rtype: float
        """
        return self._adjustment_negative

    @adjustment_negative.setter
    def adjustment_negative(self, adjustment_negative):
        """
        Sets the adjustment_negative of this SalesDataCreditmemoCreationArgumentsInterface.
        Credit memo negative adjustment.

        :param adjustment_negative: The adjustment_negative of this SalesDataCreditmemoCreationArgumentsInterface.
        :type: float
        """

        self._adjustment_negative = adjustment_negative

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesDataCreditmemoCreationArgumentsInterface.

        :return: The extension_attributes of this SalesDataCreditmemoCreationArgumentsInterface.
        :rtype: SalesDataCreditmemoCreationArgumentsExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesDataCreditmemoCreationArgumentsInterface.

        :param extension_attributes: The extension_attributes of this SalesDataCreditmemoCreationArgumentsInterface.
        :type: SalesDataCreditmemoCreationArgumentsExtensionInterface
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
        if not isinstance(other, SalesDataCreditmemoCreationArgumentsInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
