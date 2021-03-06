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


class CheckoutDataPaymentDetailsInterface(object):
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
        'payment_methods': 'list[QuoteDataPaymentMethodInterface]',
        'totals': 'QuoteDataTotalsInterface',
        'extension_attributes': 'CheckoutDataPaymentDetailsExtensionInterface'
    }

    attribute_map = {
        'payment_methods': 'payment_methods',
        'totals': 'totals',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, payment_methods=None, totals=None, extension_attributes=None):
        """
        CheckoutDataPaymentDetailsInterface - a model defined in Swagger
        """

        self._payment_methods = None
        self._totals = None
        self._extension_attributes = None

        self.payment_methods = payment_methods
        self.totals = totals
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def payment_methods(self):
        """
        Gets the payment_methods of this CheckoutDataPaymentDetailsInterface.

        :return: The payment_methods of this CheckoutDataPaymentDetailsInterface.
        :rtype: list[QuoteDataPaymentMethodInterface]
        """
        return self._payment_methods

    @payment_methods.setter
    def payment_methods(self, payment_methods):
        """
        Sets the payment_methods of this CheckoutDataPaymentDetailsInterface.

        :param payment_methods: The payment_methods of this CheckoutDataPaymentDetailsInterface.
        :type: list[QuoteDataPaymentMethodInterface]
        """
        if payment_methods is None:
            raise ValueError("Invalid value for `payment_methods`, must not be `None`")

        self._payment_methods = payment_methods

    @property
    def totals(self):
        """
        Gets the totals of this CheckoutDataPaymentDetailsInterface.

        :return: The totals of this CheckoutDataPaymentDetailsInterface.
        :rtype: QuoteDataTotalsInterface
        """
        return self._totals

    @totals.setter
    def totals(self, totals):
        """
        Sets the totals of this CheckoutDataPaymentDetailsInterface.

        :param totals: The totals of this CheckoutDataPaymentDetailsInterface.
        :type: QuoteDataTotalsInterface
        """
        if totals is None:
            raise ValueError("Invalid value for `totals`, must not be `None`")

        self._totals = totals

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CheckoutDataPaymentDetailsInterface.

        :return: The extension_attributes of this CheckoutDataPaymentDetailsInterface.
        :rtype: CheckoutDataPaymentDetailsExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CheckoutDataPaymentDetailsInterface.

        :param extension_attributes: The extension_attributes of this CheckoutDataPaymentDetailsInterface.
        :type: CheckoutDataPaymentDetailsExtensionInterface
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
        if not isinstance(other, CheckoutDataPaymentDetailsInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
