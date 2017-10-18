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


class CustomerDataValidationResultsInterface(object):
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
        'valid': 'bool',
        'messages': 'list[str]'
    }

    attribute_map = {
        'valid': 'valid',
        'messages': 'messages'
    }

    def __init__(self, valid=None, messages=None):
        """
        CustomerDataValidationResultsInterface - a model defined in Swagger
        """

        self._valid = None
        self._messages = None

        self.valid = valid
        self.messages = messages

    @property
    def valid(self):
        """
        Gets the valid of this CustomerDataValidationResultsInterface.
        If the provided data is valid.

        :return: The valid of this CustomerDataValidationResultsInterface.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """
        Sets the valid of this CustomerDataValidationResultsInterface.
        If the provided data is valid.

        :param valid: The valid of this CustomerDataValidationResultsInterface.
        :type: bool
        """
        if valid is None:
            raise ValueError("Invalid value for `valid`, must not be `None`")

        self._valid = valid

    @property
    def messages(self):
        """
        Gets the messages of this CustomerDataValidationResultsInterface.
        Error messages as array in case of validation failure, else return empty array.

        :return: The messages of this CustomerDataValidationResultsInterface.
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """
        Sets the messages of this CustomerDataValidationResultsInterface.
        Error messages as array in case of validation failure, else return empty array.

        :param messages: The messages of this CustomerDataValidationResultsInterface.
        :type: list[str]
        """
        if messages is None:
            raise ValueError("Invalid value for `messages`, must not be `None`")

        self._messages = messages

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
        if not isinstance(other, CustomerDataValidationResultsInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other