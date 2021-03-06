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


class SalesRuleDataCouponGenerationSpecInterface(object):
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
        'rule_id': 'int',
        'format': 'str',
        'quantity': 'int',
        'length': 'int',
        'prefix': 'str',
        'suffix': 'str',
        'delimiter_at_every': 'int',
        'delimiter': 'str',
        'extension_attributes': 'SalesRuleDataCouponGenerationSpecExtensionInterface'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'format': 'format',
        'quantity': 'quantity',
        'length': 'length',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'delimiter_at_every': 'delimiter_at_every',
        'delimiter': 'delimiter',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, rule_id=None, format=None, quantity=None, length=None, prefix=None, suffix=None, delimiter_at_every=None, delimiter=None, extension_attributes=None):
        """
        SalesRuleDataCouponGenerationSpecInterface - a model defined in Swagger
        """

        self._rule_id = None
        self._format = None
        self._quantity = None
        self._length = None
        self._prefix = None
        self._suffix = None
        self._delimiter_at_every = None
        self._delimiter = None
        self._extension_attributes = None

        self.rule_id = rule_id
        self.format = format
        self.quantity = quantity
        self.length = length
        if prefix is not None:
          self.prefix = prefix
        if suffix is not None:
          self.suffix = suffix
        if delimiter_at_every is not None:
          self.delimiter_at_every = delimiter_at_every
        if delimiter is not None:
          self.delimiter = delimiter
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def rule_id(self):
        """
        Gets the rule_id of this SalesRuleDataCouponGenerationSpecInterface.
        The id of the rule associated with the coupon

        :return: The rule_id of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: int
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """
        Sets the rule_id of this SalesRuleDataCouponGenerationSpecInterface.
        The id of the rule associated with the coupon

        :param rule_id: The rule_id of this SalesRuleDataCouponGenerationSpecInterface.
        :type: int
        """
        if rule_id is None:
            raise ValueError("Invalid value for `rule_id`, must not be `None`")

        self._rule_id = rule_id

    @property
    def format(self):
        """
        Gets the format of this SalesRuleDataCouponGenerationSpecInterface.
        Format of generated coupon code

        :return: The format of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this SalesRuleDataCouponGenerationSpecInterface.
        Format of generated coupon code

        :param format: The format of this SalesRuleDataCouponGenerationSpecInterface.
        :type: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")

        self._format = format

    @property
    def quantity(self):
        """
        Gets the quantity of this SalesRuleDataCouponGenerationSpecInterface.
        Of coupons to generate

        :return: The quantity of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this SalesRuleDataCouponGenerationSpecInterface.
        Of coupons to generate

        :param quantity: The quantity of this SalesRuleDataCouponGenerationSpecInterface.
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity

    @property
    def length(self):
        """
        Gets the length of this SalesRuleDataCouponGenerationSpecInterface.
        Length of coupon code

        :return: The length of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this SalesRuleDataCouponGenerationSpecInterface.
        Length of coupon code

        :param length: The length of this SalesRuleDataCouponGenerationSpecInterface.
        :type: int
        """
        if length is None:
            raise ValueError("Invalid value for `length`, must not be `None`")

        self._length = length

    @property
    def prefix(self):
        """
        Gets the prefix of this SalesRuleDataCouponGenerationSpecInterface.
        The prefix

        :return: The prefix of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this SalesRuleDataCouponGenerationSpecInterface.
        The prefix

        :param prefix: The prefix of this SalesRuleDataCouponGenerationSpecInterface.
        :type: str
        """

        self._prefix = prefix

    @property
    def suffix(self):
        """
        Gets the suffix of this SalesRuleDataCouponGenerationSpecInterface.
        The suffix

        :return: The suffix of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this SalesRuleDataCouponGenerationSpecInterface.
        The suffix

        :param suffix: The suffix of this SalesRuleDataCouponGenerationSpecInterface.
        :type: str
        """

        self._suffix = suffix

    @property
    def delimiter_at_every(self):
        """
        Gets the delimiter_at_every of this SalesRuleDataCouponGenerationSpecInterface.
        The spacing where the delimiter should exist

        :return: The delimiter_at_every of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: int
        """
        return self._delimiter_at_every

    @delimiter_at_every.setter
    def delimiter_at_every(self, delimiter_at_every):
        """
        Sets the delimiter_at_every of this SalesRuleDataCouponGenerationSpecInterface.
        The spacing where the delimiter should exist

        :param delimiter_at_every: The delimiter_at_every of this SalesRuleDataCouponGenerationSpecInterface.
        :type: int
        """

        self._delimiter_at_every = delimiter_at_every

    @property
    def delimiter(self):
        """
        Gets the delimiter of this SalesRuleDataCouponGenerationSpecInterface.
        The delimiter

        :return: The delimiter of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: str
        """
        return self._delimiter

    @delimiter.setter
    def delimiter(self, delimiter):
        """
        Sets the delimiter of this SalesRuleDataCouponGenerationSpecInterface.
        The delimiter

        :param delimiter: The delimiter of this SalesRuleDataCouponGenerationSpecInterface.
        :type: str
        """

        self._delimiter = delimiter

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesRuleDataCouponGenerationSpecInterface.

        :return: The extension_attributes of this SalesRuleDataCouponGenerationSpecInterface.
        :rtype: SalesRuleDataCouponGenerationSpecExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesRuleDataCouponGenerationSpecInterface.

        :param extension_attributes: The extension_attributes of this SalesRuleDataCouponGenerationSpecInterface.
        :type: SalesRuleDataCouponGenerationSpecExtensionInterface
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
        if not isinstance(other, SalesRuleDataCouponGenerationSpecInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
