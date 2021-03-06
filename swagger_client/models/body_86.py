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


class Body86(object):
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
        'sample': 'DownloadableDataSampleInterface',
        'is_global_scope_content': 'bool'
    }

    attribute_map = {
        'sample': 'sample',
        'is_global_scope_content': 'isGlobalScopeContent'
    }

    def __init__(self, sample=None, is_global_scope_content=None):
        """
        Body86 - a model defined in Swagger
        """

        self._sample = None
        self._is_global_scope_content = None

        self.sample = sample
        if is_global_scope_content is not None:
          self.is_global_scope_content = is_global_scope_content

    @property
    def sample(self):
        """
        Gets the sample of this Body86.

        :return: The sample of this Body86.
        :rtype: DownloadableDataSampleInterface
        """
        return self._sample

    @sample.setter
    def sample(self, sample):
        """
        Sets the sample of this Body86.

        :param sample: The sample of this Body86.
        :type: DownloadableDataSampleInterface
        """
        if sample is None:
            raise ValueError("Invalid value for `sample`, must not be `None`")

        self._sample = sample

    @property
    def is_global_scope_content(self):
        """
        Gets the is_global_scope_content of this Body86.

        :return: The is_global_scope_content of this Body86.
        :rtype: bool
        """
        return self._is_global_scope_content

    @is_global_scope_content.setter
    def is_global_scope_content(self, is_global_scope_content):
        """
        Sets the is_global_scope_content of this Body86.

        :param is_global_scope_content: The is_global_scope_content of this Body86.
        :type: bool
        """

        self._is_global_scope_content = is_global_scope_content

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
        if not isinstance(other, Body86):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
