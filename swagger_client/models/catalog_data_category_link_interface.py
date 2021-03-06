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


class CatalogDataCategoryLinkInterface(object):
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
        'position': 'int',
        'category_id': 'str',
        'extension_attributes': 'CatalogDataCategoryLinkExtensionInterface'
    }

    attribute_map = {
        'position': 'position',
        'category_id': 'category_id',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, position=None, category_id=None, extension_attributes=None):
        """
        CatalogDataCategoryLinkInterface - a model defined in Swagger
        """

        self._position = None
        self._category_id = None
        self._extension_attributes = None

        if position is not None:
          self.position = position
        self.category_id = category_id
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def position(self):
        """
        Gets the position of this CatalogDataCategoryLinkInterface.

        :return: The position of this CatalogDataCategoryLinkInterface.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this CatalogDataCategoryLinkInterface.

        :param position: The position of this CatalogDataCategoryLinkInterface.
        :type: int
        """

        self._position = position

    @property
    def category_id(self):
        """
        Gets the category_id of this CatalogDataCategoryLinkInterface.
        Category id

        :return: The category_id of this CatalogDataCategoryLinkInterface.
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """
        Sets the category_id of this CatalogDataCategoryLinkInterface.
        Category id

        :param category_id: The category_id of this CatalogDataCategoryLinkInterface.
        :type: str
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")

        self._category_id = category_id

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CatalogDataCategoryLinkInterface.

        :return: The extension_attributes of this CatalogDataCategoryLinkInterface.
        :rtype: CatalogDataCategoryLinkExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CatalogDataCategoryLinkInterface.

        :param extension_attributes: The extension_attributes of this CatalogDataCategoryLinkInterface.
        :type: CatalogDataCategoryLinkExtensionInterface
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
        if not isinstance(other, CatalogDataCategoryLinkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
