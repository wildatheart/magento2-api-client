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


class QuoteDataCurrencyInterface(object):
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
        'global_currency_code': 'str',
        'base_currency_code': 'str',
        'store_currency_code': 'str',
        'quote_currency_code': 'str',
        'store_to_base_rate': 'float',
        'store_to_quote_rate': 'float',
        'base_to_global_rate': 'float',
        'base_to_quote_rate': 'float',
        'extension_attributes': 'QuoteDataCurrencyExtensionInterface'
    }

    attribute_map = {
        'global_currency_code': 'global_currency_code',
        'base_currency_code': 'base_currency_code',
        'store_currency_code': 'store_currency_code',
        'quote_currency_code': 'quote_currency_code',
        'store_to_base_rate': 'store_to_base_rate',
        'store_to_quote_rate': 'store_to_quote_rate',
        'base_to_global_rate': 'base_to_global_rate',
        'base_to_quote_rate': 'base_to_quote_rate',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, global_currency_code=None, base_currency_code=None, store_currency_code=None, quote_currency_code=None, store_to_base_rate=None, store_to_quote_rate=None, base_to_global_rate=None, base_to_quote_rate=None, extension_attributes=None):
        """
        QuoteDataCurrencyInterface - a model defined in Swagger
        """

        self._global_currency_code = None
        self._base_currency_code = None
        self._store_currency_code = None
        self._quote_currency_code = None
        self._store_to_base_rate = None
        self._store_to_quote_rate = None
        self._base_to_global_rate = None
        self._base_to_quote_rate = None
        self._extension_attributes = None

        if global_currency_code is not None:
          self.global_currency_code = global_currency_code
        if base_currency_code is not None:
          self.base_currency_code = base_currency_code
        if store_currency_code is not None:
          self.store_currency_code = store_currency_code
        if quote_currency_code is not None:
          self.quote_currency_code = quote_currency_code
        if store_to_base_rate is not None:
          self.store_to_base_rate = store_to_base_rate
        if store_to_quote_rate is not None:
          self.store_to_quote_rate = store_to_quote_rate
        if base_to_global_rate is not None:
          self.base_to_global_rate = base_to_global_rate
        if base_to_quote_rate is not None:
          self.base_to_quote_rate = base_to_quote_rate
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def global_currency_code(self):
        """
        Gets the global_currency_code of this QuoteDataCurrencyInterface.
        Global currency code

        :return: The global_currency_code of this QuoteDataCurrencyInterface.
        :rtype: str
        """
        return self._global_currency_code

    @global_currency_code.setter
    def global_currency_code(self, global_currency_code):
        """
        Sets the global_currency_code of this QuoteDataCurrencyInterface.
        Global currency code

        :param global_currency_code: The global_currency_code of this QuoteDataCurrencyInterface.
        :type: str
        """

        self._global_currency_code = global_currency_code

    @property
    def base_currency_code(self):
        """
        Gets the base_currency_code of this QuoteDataCurrencyInterface.
        Base currency code

        :return: The base_currency_code of this QuoteDataCurrencyInterface.
        :rtype: str
        """
        return self._base_currency_code

    @base_currency_code.setter
    def base_currency_code(self, base_currency_code):
        """
        Sets the base_currency_code of this QuoteDataCurrencyInterface.
        Base currency code

        :param base_currency_code: The base_currency_code of this QuoteDataCurrencyInterface.
        :type: str
        """

        self._base_currency_code = base_currency_code

    @property
    def store_currency_code(self):
        """
        Gets the store_currency_code of this QuoteDataCurrencyInterface.
        Store currency code

        :return: The store_currency_code of this QuoteDataCurrencyInterface.
        :rtype: str
        """
        return self._store_currency_code

    @store_currency_code.setter
    def store_currency_code(self, store_currency_code):
        """
        Sets the store_currency_code of this QuoteDataCurrencyInterface.
        Store currency code

        :param store_currency_code: The store_currency_code of this QuoteDataCurrencyInterface.
        :type: str
        """

        self._store_currency_code = store_currency_code

    @property
    def quote_currency_code(self):
        """
        Gets the quote_currency_code of this QuoteDataCurrencyInterface.
        Quote currency code

        :return: The quote_currency_code of this QuoteDataCurrencyInterface.
        :rtype: str
        """
        return self._quote_currency_code

    @quote_currency_code.setter
    def quote_currency_code(self, quote_currency_code):
        """
        Sets the quote_currency_code of this QuoteDataCurrencyInterface.
        Quote currency code

        :param quote_currency_code: The quote_currency_code of this QuoteDataCurrencyInterface.
        :type: str
        """

        self._quote_currency_code = quote_currency_code

    @property
    def store_to_base_rate(self):
        """
        Gets the store_to_base_rate of this QuoteDataCurrencyInterface.
        Store currency to base currency rate

        :return: The store_to_base_rate of this QuoteDataCurrencyInterface.
        :rtype: float
        """
        return self._store_to_base_rate

    @store_to_base_rate.setter
    def store_to_base_rate(self, store_to_base_rate):
        """
        Sets the store_to_base_rate of this QuoteDataCurrencyInterface.
        Store currency to base currency rate

        :param store_to_base_rate: The store_to_base_rate of this QuoteDataCurrencyInterface.
        :type: float
        """

        self._store_to_base_rate = store_to_base_rate

    @property
    def store_to_quote_rate(self):
        """
        Gets the store_to_quote_rate of this QuoteDataCurrencyInterface.
        Store currency to quote currency rate

        :return: The store_to_quote_rate of this QuoteDataCurrencyInterface.
        :rtype: float
        """
        return self._store_to_quote_rate

    @store_to_quote_rate.setter
    def store_to_quote_rate(self, store_to_quote_rate):
        """
        Sets the store_to_quote_rate of this QuoteDataCurrencyInterface.
        Store currency to quote currency rate

        :param store_to_quote_rate: The store_to_quote_rate of this QuoteDataCurrencyInterface.
        :type: float
        """

        self._store_to_quote_rate = store_to_quote_rate

    @property
    def base_to_global_rate(self):
        """
        Gets the base_to_global_rate of this QuoteDataCurrencyInterface.
        Base currency to global currency rate

        :return: The base_to_global_rate of this QuoteDataCurrencyInterface.
        :rtype: float
        """
        return self._base_to_global_rate

    @base_to_global_rate.setter
    def base_to_global_rate(self, base_to_global_rate):
        """
        Sets the base_to_global_rate of this QuoteDataCurrencyInterface.
        Base currency to global currency rate

        :param base_to_global_rate: The base_to_global_rate of this QuoteDataCurrencyInterface.
        :type: float
        """

        self._base_to_global_rate = base_to_global_rate

    @property
    def base_to_quote_rate(self):
        """
        Gets the base_to_quote_rate of this QuoteDataCurrencyInterface.
        Base currency to quote currency rate

        :return: The base_to_quote_rate of this QuoteDataCurrencyInterface.
        :rtype: float
        """
        return self._base_to_quote_rate

    @base_to_quote_rate.setter
    def base_to_quote_rate(self, base_to_quote_rate):
        """
        Sets the base_to_quote_rate of this QuoteDataCurrencyInterface.
        Base currency to quote currency rate

        :param base_to_quote_rate: The base_to_quote_rate of this QuoteDataCurrencyInterface.
        :type: float
        """

        self._base_to_quote_rate = base_to_quote_rate

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this QuoteDataCurrencyInterface.

        :return: The extension_attributes of this QuoteDataCurrencyInterface.
        :rtype: QuoteDataCurrencyExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this QuoteDataCurrencyInterface.

        :param extension_attributes: The extension_attributes of this QuoteDataCurrencyInterface.
        :type: QuoteDataCurrencyExtensionInterface
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
        if not isinstance(other, QuoteDataCurrencyInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other