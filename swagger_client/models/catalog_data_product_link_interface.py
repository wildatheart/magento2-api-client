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


class CatalogDataProductLinkInterface(object):
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
        'sku': 'str',
        'link_type': 'str',
        'linked_product_sku': 'str',
        'linked_product_type': 'str',
        'position': 'int',
        'extension_attributes': 'CatalogDataProductLinkExtensionInterface'
    }

    attribute_map = {
        'sku': 'sku',
        'link_type': 'link_type',
        'linked_product_sku': 'linked_product_sku',
        'linked_product_type': 'linked_product_type',
        'position': 'position',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, sku=None, link_type=None, linked_product_sku=None, linked_product_type=None, position=None, extension_attributes=None):
        """
        CatalogDataProductLinkInterface - a model defined in Swagger
        """

        self._sku = None
        self._link_type = None
        self._linked_product_sku = None
        self._linked_product_type = None
        self._position = None
        self._extension_attributes = None

        self.sku = sku
        self.link_type = link_type
        self.linked_product_sku = linked_product_sku
        self.linked_product_type = linked_product_type
        self.position = position
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def sku(self):
        """
        Gets the sku of this CatalogDataProductLinkInterface.
        SKU

        :return: The sku of this CatalogDataProductLinkInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this CatalogDataProductLinkInterface.
        SKU

        :param sku: The sku of this CatalogDataProductLinkInterface.
        :type: str
        """
        if sku is None:
            raise ValueError("Invalid value for `sku`, must not be `None`")

        self._sku = sku

    @property
    def link_type(self):
        """
        Gets the link_type of this CatalogDataProductLinkInterface.
        Link type

        :return: The link_type of this CatalogDataProductLinkInterface.
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """
        Sets the link_type of this CatalogDataProductLinkInterface.
        Link type

        :param link_type: The link_type of this CatalogDataProductLinkInterface.
        :type: str
        """
        if link_type is None:
            raise ValueError("Invalid value for `link_type`, must not be `None`")

        self._link_type = link_type

    @property
    def linked_product_sku(self):
        """
        Gets the linked_product_sku of this CatalogDataProductLinkInterface.
        Linked product sku

        :return: The linked_product_sku of this CatalogDataProductLinkInterface.
        :rtype: str
        """
        return self._linked_product_sku

    @linked_product_sku.setter
    def linked_product_sku(self, linked_product_sku):
        """
        Sets the linked_product_sku of this CatalogDataProductLinkInterface.
        Linked product sku

        :param linked_product_sku: The linked_product_sku of this CatalogDataProductLinkInterface.
        :type: str
        """
        if linked_product_sku is None:
            raise ValueError("Invalid value for `linked_product_sku`, must not be `None`")

        self._linked_product_sku = linked_product_sku

    @property
    def linked_product_type(self):
        """
        Gets the linked_product_type of this CatalogDataProductLinkInterface.
        Linked product type (simple, virtual, etc)

        :return: The linked_product_type of this CatalogDataProductLinkInterface.
        :rtype: str
        """
        return self._linked_product_type

    @linked_product_type.setter
    def linked_product_type(self, linked_product_type):
        """
        Sets the linked_product_type of this CatalogDataProductLinkInterface.
        Linked product type (simple, virtual, etc)

        :param linked_product_type: The linked_product_type of this CatalogDataProductLinkInterface.
        :type: str
        """
        if linked_product_type is None:
            raise ValueError("Invalid value for `linked_product_type`, must not be `None`")

        self._linked_product_type = linked_product_type

    @property
    def position(self):
        """
        Gets the position of this CatalogDataProductLinkInterface.
        Linked item position

        :return: The position of this CatalogDataProductLinkInterface.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this CatalogDataProductLinkInterface.
        Linked item position

        :param position: The position of this CatalogDataProductLinkInterface.
        :type: int
        """
        if position is None:
            raise ValueError("Invalid value for `position`, must not be `None`")

        self._position = position

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CatalogDataProductLinkInterface.

        :return: The extension_attributes of this CatalogDataProductLinkInterface.
        :rtype: CatalogDataProductLinkExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CatalogDataProductLinkInterface.

        :param extension_attributes: The extension_attributes of this CatalogDataProductLinkInterface.
        :type: CatalogDataProductLinkExtensionInterface
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
        if not isinstance(other, CatalogDataProductLinkInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
