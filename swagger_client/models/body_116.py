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


class Body116(object):
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
        'email': 'str',
        'payment_method': 'QuoteDataPaymentInterface',
        'billing_address': 'QuoteDataAddressInterface'
    }

    attribute_map = {
        'email': 'email',
        'payment_method': 'paymentMethod',
        'billing_address': 'billingAddress'
    }

    def __init__(self, email=None, payment_method=None, billing_address=None):
        """
        Body116 - a model defined in Swagger
        """

        self._email = None
        self._payment_method = None
        self._billing_address = None

        self.email = email
        self.payment_method = payment_method
        if billing_address is not None:
          self.billing_address = billing_address

    @property
    def email(self):
        """
        Gets the email of this Body116.

        :return: The email of this Body116.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Body116.

        :param email: The email of this Body116.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def payment_method(self):
        """
        Gets the payment_method of this Body116.

        :return: The payment_method of this Body116.
        :rtype: QuoteDataPaymentInterface
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """
        Sets the payment_method of this Body116.

        :param payment_method: The payment_method of this Body116.
        :type: QuoteDataPaymentInterface
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")

        self._payment_method = payment_method

    @property
    def billing_address(self):
        """
        Gets the billing_address of this Body116.

        :return: The billing_address of this Body116.
        :rtype: QuoteDataAddressInterface
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """
        Sets the billing_address of this Body116.

        :param billing_address: The billing_address of this Body116.
        :type: QuoteDataAddressInterface
        """

        self._billing_address = billing_address

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
        if not isinstance(other, Body116):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
