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


class SalesRuleDataRuleLabelInterface(object):
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
        'store_id': 'int',
        'store_label': 'str',
        'extension_attributes': 'SalesRuleDataRuleLabelExtensionInterface'
    }

    attribute_map = {
        'store_id': 'store_id',
        'store_label': 'store_label',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, store_id=None, store_label=None, extension_attributes=None):
        """
        SalesRuleDataRuleLabelInterface - a model defined in Swagger
        """

        self._store_id = None
        self._store_label = None
        self._extension_attributes = None

        self.store_id = store_id
        self.store_label = store_label
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def store_id(self):
        """
        Gets the store_id of this SalesRuleDataRuleLabelInterface.
        StoreId

        :return: The store_id of this SalesRuleDataRuleLabelInterface.
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """
        Sets the store_id of this SalesRuleDataRuleLabelInterface.
        StoreId

        :param store_id: The store_id of this SalesRuleDataRuleLabelInterface.
        :type: int
        """
        if store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")

        self._store_id = store_id

    @property
    def store_label(self):
        """
        Gets the store_label of this SalesRuleDataRuleLabelInterface.
        The label for the store

        :return: The store_label of this SalesRuleDataRuleLabelInterface.
        :rtype: str
        """
        return self._store_label

    @store_label.setter
    def store_label(self, store_label):
        """
        Sets the store_label of this SalesRuleDataRuleLabelInterface.
        The label for the store

        :param store_label: The store_label of this SalesRuleDataRuleLabelInterface.
        :type: str
        """
        if store_label is None:
            raise ValueError("Invalid value for `store_label`, must not be `None`")

        self._store_label = store_label

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesRuleDataRuleLabelInterface.

        :return: The extension_attributes of this SalesRuleDataRuleLabelInterface.
        :rtype: SalesRuleDataRuleLabelExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesRuleDataRuleLabelInterface.

        :param extension_attributes: The extension_attributes of this SalesRuleDataRuleLabelInterface.
        :type: SalesRuleDataRuleLabelExtensionInterface
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
        if not isinstance(other, SalesRuleDataRuleLabelInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
