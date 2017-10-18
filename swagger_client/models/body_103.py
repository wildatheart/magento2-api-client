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


class Body103(object):
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
        'gift_message': 'GiftMessageDataMessageInterface'
    }

    attribute_map = {
        'gift_message': 'giftMessage'
    }

    def __init__(self, gift_message=None):
        """
        Body103 - a model defined in Swagger
        """

        self._gift_message = None

        self.gift_message = gift_message

    @property
    def gift_message(self):
        """
        Gets the gift_message of this Body103.

        :return: The gift_message of this Body103.
        :rtype: GiftMessageDataMessageInterface
        """
        return self._gift_message

    @gift_message.setter
    def gift_message(self, gift_message):
        """
        Sets the gift_message of this Body103.

        :param gift_message: The gift_message of this Body103.
        :type: GiftMessageDataMessageInterface
        """
        if gift_message is None:
            raise ValueError("Invalid value for `gift_message`, must not be `None`")

        self._gift_message = gift_message

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
        if not isinstance(other, Body103):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other