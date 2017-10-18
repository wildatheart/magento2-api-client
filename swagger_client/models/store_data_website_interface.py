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


class StoreDataWebsiteInterface(object):
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
        'id': 'int',
        'code': 'str',
        'name': 'str',
        'default_group_id': 'int',
        'extension_attributes': 'StoreDataWebsiteExtensionInterface'
    }

    attribute_map = {
        'id': 'id',
        'code': 'code',
        'name': 'name',
        'default_group_id': 'default_group_id',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, id=None, code=None, name=None, default_group_id=None, extension_attributes=None):
        """
        StoreDataWebsiteInterface - a model defined in Swagger
        """

        self._id = None
        self._code = None
        self._name = None
        self._default_group_id = None
        self._extension_attributes = None

        self.id = id
        self.code = code
        self.name = name
        self.default_group_id = default_group_id
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def id(self):
        """
        Gets the id of this StoreDataWebsiteInterface.

        :return: The id of this StoreDataWebsiteInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StoreDataWebsiteInterface.

        :param id: The id of this StoreDataWebsiteInterface.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def code(self):
        """
        Gets the code of this StoreDataWebsiteInterface.

        :return: The code of this StoreDataWebsiteInterface.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this StoreDataWebsiteInterface.

        :param code: The code of this StoreDataWebsiteInterface.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def name(self):
        """
        Gets the name of this StoreDataWebsiteInterface.
        Website name

        :return: The name of this StoreDataWebsiteInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoreDataWebsiteInterface.
        Website name

        :param name: The name of this StoreDataWebsiteInterface.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def default_group_id(self):
        """
        Gets the default_group_id of this StoreDataWebsiteInterface.

        :return: The default_group_id of this StoreDataWebsiteInterface.
        :rtype: int
        """
        return self._default_group_id

    @default_group_id.setter
    def default_group_id(self, default_group_id):
        """
        Sets the default_group_id of this StoreDataWebsiteInterface.

        :param default_group_id: The default_group_id of this StoreDataWebsiteInterface.
        :type: int
        """
        if default_group_id is None:
            raise ValueError("Invalid value for `default_group_id`, must not be `None`")

        self._default_group_id = default_group_id

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this StoreDataWebsiteInterface.

        :return: The extension_attributes of this StoreDataWebsiteInterface.
        :rtype: StoreDataWebsiteExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this StoreDataWebsiteInterface.

        :param extension_attributes: The extension_attributes of this StoreDataWebsiteInterface.
        :type: StoreDataWebsiteExtensionInterface
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
        if not isinstance(other, StoreDataWebsiteInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other