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


class EavDataAttributeSetInterface(object):
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
        'attribute_set_id': 'int',
        'attribute_set_name': 'str',
        'sort_order': 'int',
        'entity_type_id': 'int',
        'extension_attributes': 'EavDataAttributeSetExtensionInterface'
    }

    attribute_map = {
        'attribute_set_id': 'attribute_set_id',
        'attribute_set_name': 'attribute_set_name',
        'sort_order': 'sort_order',
        'entity_type_id': 'entity_type_id',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, attribute_set_id=None, attribute_set_name=None, sort_order=None, entity_type_id=None, extension_attributes=None):
        """
        EavDataAttributeSetInterface - a model defined in Swagger
        """

        self._attribute_set_id = None
        self._attribute_set_name = None
        self._sort_order = None
        self._entity_type_id = None
        self._extension_attributes = None

        if attribute_set_id is not None:
          self.attribute_set_id = attribute_set_id
        self.attribute_set_name = attribute_set_name
        self.sort_order = sort_order
        if entity_type_id is not None:
          self.entity_type_id = entity_type_id
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def attribute_set_id(self):
        """
        Gets the attribute_set_id of this EavDataAttributeSetInterface.
        Attribute set ID

        :return: The attribute_set_id of this EavDataAttributeSetInterface.
        :rtype: int
        """
        return self._attribute_set_id

    @attribute_set_id.setter
    def attribute_set_id(self, attribute_set_id):
        """
        Sets the attribute_set_id of this EavDataAttributeSetInterface.
        Attribute set ID

        :param attribute_set_id: The attribute_set_id of this EavDataAttributeSetInterface.
        :type: int
        """

        self._attribute_set_id = attribute_set_id

    @property
    def attribute_set_name(self):
        """
        Gets the attribute_set_name of this EavDataAttributeSetInterface.
        Attribute set name

        :return: The attribute_set_name of this EavDataAttributeSetInterface.
        :rtype: str
        """
        return self._attribute_set_name

    @attribute_set_name.setter
    def attribute_set_name(self, attribute_set_name):
        """
        Sets the attribute_set_name of this EavDataAttributeSetInterface.
        Attribute set name

        :param attribute_set_name: The attribute_set_name of this EavDataAttributeSetInterface.
        :type: str
        """
        if attribute_set_name is None:
            raise ValueError("Invalid value for `attribute_set_name`, must not be `None`")

        self._attribute_set_name = attribute_set_name

    @property
    def sort_order(self):
        """
        Gets the sort_order of this EavDataAttributeSetInterface.
        Attribute set sort order index

        :return: The sort_order of this EavDataAttributeSetInterface.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this EavDataAttributeSetInterface.
        Attribute set sort order index

        :param sort_order: The sort_order of this EavDataAttributeSetInterface.
        :type: int
        """
        if sort_order is None:
            raise ValueError("Invalid value for `sort_order`, must not be `None`")

        self._sort_order = sort_order

    @property
    def entity_type_id(self):
        """
        Gets the entity_type_id of this EavDataAttributeSetInterface.
        Attribute set entity type id

        :return: The entity_type_id of this EavDataAttributeSetInterface.
        :rtype: int
        """
        return self._entity_type_id

    @entity_type_id.setter
    def entity_type_id(self, entity_type_id):
        """
        Sets the entity_type_id of this EavDataAttributeSetInterface.
        Attribute set entity type id

        :param entity_type_id: The entity_type_id of this EavDataAttributeSetInterface.
        :type: int
        """

        self._entity_type_id = entity_type_id

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this EavDataAttributeSetInterface.

        :return: The extension_attributes of this EavDataAttributeSetInterface.
        :rtype: EavDataAttributeSetExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this EavDataAttributeSetInterface.

        :param extension_attributes: The extension_attributes of this EavDataAttributeSetInterface.
        :type: EavDataAttributeSetExtensionInterface
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
        if not isinstance(other, EavDataAttributeSetInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other