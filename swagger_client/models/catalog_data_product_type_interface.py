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


class CatalogDataProductTypeInterface(object):
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
        'name': 'str',
        'label': 'str',
        'extension_attributes': 'CatalogDataProductTypeExtensionInterface'
    }

    attribute_map = {
        'name': 'name',
        'label': 'label',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, name=None, label=None, extension_attributes=None):
        """
        CatalogDataProductTypeInterface - a model defined in Swagger
        """

        self._name = None
        self._label = None
        self._extension_attributes = None

        self.name = name
        self.label = label
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def name(self):
        """
        Gets the name of this CatalogDataProductTypeInterface.
        Product type code

        :return: The name of this CatalogDataProductTypeInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CatalogDataProductTypeInterface.
        Product type code

        :param name: The name of this CatalogDataProductTypeInterface.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def label(self):
        """
        Gets the label of this CatalogDataProductTypeInterface.
        Product type label

        :return: The label of this CatalogDataProductTypeInterface.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this CatalogDataProductTypeInterface.
        Product type label

        :param label: The label of this CatalogDataProductTypeInterface.
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CatalogDataProductTypeInterface.

        :return: The extension_attributes of this CatalogDataProductTypeInterface.
        :rtype: CatalogDataProductTypeExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CatalogDataProductTypeInterface.

        :param extension_attributes: The extension_attributes of this CatalogDataProductTypeInterface.
        :type: CatalogDataProductTypeExtensionInterface
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
        if not isinstance(other, CatalogDataProductTypeInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
