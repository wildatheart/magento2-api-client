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


class QuoteDataShippingMethodInterface(object):
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
        'carrier_code': 'str',
        'method_code': 'str',
        'carrier_title': 'str',
        'method_title': 'str',
        'amount': 'float',
        'base_amount': 'float',
        'available': 'bool',
        'extension_attributes': 'QuoteDataShippingMethodExtensionInterface',
        'error_message': 'str',
        'price_excl_tax': 'float',
        'price_incl_tax': 'float'
    }

    attribute_map = {
        'carrier_code': 'carrier_code',
        'method_code': 'method_code',
        'carrier_title': 'carrier_title',
        'method_title': 'method_title',
        'amount': 'amount',
        'base_amount': 'base_amount',
        'available': 'available',
        'extension_attributes': 'extension_attributes',
        'error_message': 'error_message',
        'price_excl_tax': 'price_excl_tax',
        'price_incl_tax': 'price_incl_tax'
    }

    def __init__(self, carrier_code=None, method_code=None, carrier_title=None, method_title=None, amount=None, base_amount=None, available=None, extension_attributes=None, error_message=None, price_excl_tax=None, price_incl_tax=None):
        """
        QuoteDataShippingMethodInterface - a model defined in Swagger
        """

        self._carrier_code = None
        self._method_code = None
        self._carrier_title = None
        self._method_title = None
        self._amount = None
        self._base_amount = None
        self._available = None
        self._extension_attributes = None
        self._error_message = None
        self._price_excl_tax = None
        self._price_incl_tax = None

        self.carrier_code = carrier_code
        self.method_code = method_code
        if carrier_title is not None:
          self.carrier_title = carrier_title
        if method_title is not None:
          self.method_title = method_title
        self.amount = amount
        self.base_amount = base_amount
        self.available = available
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes
        self.error_message = error_message
        self.price_excl_tax = price_excl_tax
        self.price_incl_tax = price_incl_tax

    @property
    def carrier_code(self):
        """
        Gets the carrier_code of this QuoteDataShippingMethodInterface.
        Shipping carrier code.

        :return: The carrier_code of this QuoteDataShippingMethodInterface.
        :rtype: str
        """
        return self._carrier_code

    @carrier_code.setter
    def carrier_code(self, carrier_code):
        """
        Sets the carrier_code of this QuoteDataShippingMethodInterface.
        Shipping carrier code.

        :param carrier_code: The carrier_code of this QuoteDataShippingMethodInterface.
        :type: str
        """
        if carrier_code is None:
            raise ValueError("Invalid value for `carrier_code`, must not be `None`")

        self._carrier_code = carrier_code

    @property
    def method_code(self):
        """
        Gets the method_code of this QuoteDataShippingMethodInterface.
        Shipping method code.

        :return: The method_code of this QuoteDataShippingMethodInterface.
        :rtype: str
        """
        return self._method_code

    @method_code.setter
    def method_code(self, method_code):
        """
        Sets the method_code of this QuoteDataShippingMethodInterface.
        Shipping method code.

        :param method_code: The method_code of this QuoteDataShippingMethodInterface.
        :type: str
        """
        if method_code is None:
            raise ValueError("Invalid value for `method_code`, must not be `None`")

        self._method_code = method_code

    @property
    def carrier_title(self):
        """
        Gets the carrier_title of this QuoteDataShippingMethodInterface.
        Shipping carrier title. Otherwise, null.

        :return: The carrier_title of this QuoteDataShippingMethodInterface.
        :rtype: str
        """
        return self._carrier_title

    @carrier_title.setter
    def carrier_title(self, carrier_title):
        """
        Sets the carrier_title of this QuoteDataShippingMethodInterface.
        Shipping carrier title. Otherwise, null.

        :param carrier_title: The carrier_title of this QuoteDataShippingMethodInterface.
        :type: str
        """

        self._carrier_title = carrier_title

    @property
    def method_title(self):
        """
        Gets the method_title of this QuoteDataShippingMethodInterface.
        Shipping method title. Otherwise, null.

        :return: The method_title of this QuoteDataShippingMethodInterface.
        :rtype: str
        """
        return self._method_title

    @method_title.setter
    def method_title(self, method_title):
        """
        Sets the method_title of this QuoteDataShippingMethodInterface.
        Shipping method title. Otherwise, null.

        :param method_title: The method_title of this QuoteDataShippingMethodInterface.
        :type: str
        """

        self._method_title = method_title

    @property
    def amount(self):
        """
        Gets the amount of this QuoteDataShippingMethodInterface.
        Shipping amount in store currency.

        :return: The amount of this QuoteDataShippingMethodInterface.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this QuoteDataShippingMethodInterface.
        Shipping amount in store currency.

        :param amount: The amount of this QuoteDataShippingMethodInterface.
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")

        self._amount = amount

    @property
    def base_amount(self):
        """
        Gets the base_amount of this QuoteDataShippingMethodInterface.
        Shipping amount in base currency.

        :return: The base_amount of this QuoteDataShippingMethodInterface.
        :rtype: float
        """
        return self._base_amount

    @base_amount.setter
    def base_amount(self, base_amount):
        """
        Sets the base_amount of this QuoteDataShippingMethodInterface.
        Shipping amount in base currency.

        :param base_amount: The base_amount of this QuoteDataShippingMethodInterface.
        :type: float
        """
        if base_amount is None:
            raise ValueError("Invalid value for `base_amount`, must not be `None`")

        self._base_amount = base_amount

    @property
    def available(self):
        """
        Gets the available of this QuoteDataShippingMethodInterface.
        The value of the availability flag for the current shipping method.

        :return: The available of this QuoteDataShippingMethodInterface.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """
        Sets the available of this QuoteDataShippingMethodInterface.
        The value of the availability flag for the current shipping method.

        :param available: The available of this QuoteDataShippingMethodInterface.
        :type: bool
        """
        if available is None:
            raise ValueError("Invalid value for `available`, must not be `None`")

        self._available = available

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this QuoteDataShippingMethodInterface.

        :return: The extension_attributes of this QuoteDataShippingMethodInterface.
        :rtype: QuoteDataShippingMethodExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this QuoteDataShippingMethodInterface.

        :param extension_attributes: The extension_attributes of this QuoteDataShippingMethodInterface.
        :type: QuoteDataShippingMethodExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def error_message(self):
        """
        Gets the error_message of this QuoteDataShippingMethodInterface.
        Shipping Error message.

        :return: The error_message of this QuoteDataShippingMethodInterface.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """
        Sets the error_message of this QuoteDataShippingMethodInterface.
        Shipping Error message.

        :param error_message: The error_message of this QuoteDataShippingMethodInterface.
        :type: str
        """
        if error_message is None:
            raise ValueError("Invalid value for `error_message`, must not be `None`")

        self._error_message = error_message

    @property
    def price_excl_tax(self):
        """
        Gets the price_excl_tax of this QuoteDataShippingMethodInterface.
        Shipping price excl tax.

        :return: The price_excl_tax of this QuoteDataShippingMethodInterface.
        :rtype: float
        """
        return self._price_excl_tax

    @price_excl_tax.setter
    def price_excl_tax(self, price_excl_tax):
        """
        Sets the price_excl_tax of this QuoteDataShippingMethodInterface.
        Shipping price excl tax.

        :param price_excl_tax: The price_excl_tax of this QuoteDataShippingMethodInterface.
        :type: float
        """
        if price_excl_tax is None:
            raise ValueError("Invalid value for `price_excl_tax`, must not be `None`")

        self._price_excl_tax = price_excl_tax

    @property
    def price_incl_tax(self):
        """
        Gets the price_incl_tax of this QuoteDataShippingMethodInterface.
        Shipping price incl tax.

        :return: The price_incl_tax of this QuoteDataShippingMethodInterface.
        :rtype: float
        """
        return self._price_incl_tax

    @price_incl_tax.setter
    def price_incl_tax(self, price_incl_tax):
        """
        Sets the price_incl_tax of this QuoteDataShippingMethodInterface.
        Shipping price incl tax.

        :param price_incl_tax: The price_incl_tax of this QuoteDataShippingMethodInterface.
        :type: float
        """
        if price_incl_tax is None:
            raise ValueError("Invalid value for `price_incl_tax`, must not be `None`")

        self._price_incl_tax = price_incl_tax

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
        if not isinstance(other, QuoteDataShippingMethodInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other