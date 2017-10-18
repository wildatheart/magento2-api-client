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


class StoreDataGroupInterface(object):
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
        'website_id': 'int',
        'root_category_id': 'int',
        'default_store_id': 'int',
        'name': 'str',
        'code': 'str',
        'extension_attributes': 'StoreDataGroupExtensionInterface'
    }

    attribute_map = {
        'id': 'id',
        'website_id': 'website_id',
        'root_category_id': 'root_category_id',
        'default_store_id': 'default_store_id',
        'name': 'name',
        'code': 'code',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, id=None, website_id=None, root_category_id=None, default_store_id=None, name=None, code=None, extension_attributes=None):
        """
        StoreDataGroupInterface - a model defined in Swagger
        """

        self._id = None
        self._website_id = None
        self._root_category_id = None
        self._default_store_id = None
        self._name = None
        self._code = None
        self._extension_attributes = None

        self.id = id
        self.website_id = website_id
        self.root_category_id = root_category_id
        self.default_store_id = default_store_id
        self.name = name
        self.code = code
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def id(self):
        """
        Gets the id of this StoreDataGroupInterface.

        :return: The id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this StoreDataGroupInterface.

        :param id: The id of this StoreDataGroupInterface.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def website_id(self):
        """
        Gets the website_id of this StoreDataGroupInterface.

        :return: The website_id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._website_id

    @website_id.setter
    def website_id(self, website_id):
        """
        Sets the website_id of this StoreDataGroupInterface.

        :param website_id: The website_id of this StoreDataGroupInterface.
        :type: int
        """
        if website_id is None:
            raise ValueError("Invalid value for `website_id`, must not be `None`")

        self._website_id = website_id

    @property
    def root_category_id(self):
        """
        Gets the root_category_id of this StoreDataGroupInterface.

        :return: The root_category_id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._root_category_id

    @root_category_id.setter
    def root_category_id(self, root_category_id):
        """
        Sets the root_category_id of this StoreDataGroupInterface.

        :param root_category_id: The root_category_id of this StoreDataGroupInterface.
        :type: int
        """
        if root_category_id is None:
            raise ValueError("Invalid value for `root_category_id`, must not be `None`")

        self._root_category_id = root_category_id

    @property
    def default_store_id(self):
        """
        Gets the default_store_id of this StoreDataGroupInterface.

        :return: The default_store_id of this StoreDataGroupInterface.
        :rtype: int
        """
        return self._default_store_id

    @default_store_id.setter
    def default_store_id(self, default_store_id):
        """
        Sets the default_store_id of this StoreDataGroupInterface.

        :param default_store_id: The default_store_id of this StoreDataGroupInterface.
        :type: int
        """
        if default_store_id is None:
            raise ValueError("Invalid value for `default_store_id`, must not be `None`")

        self._default_store_id = default_store_id

    @property
    def name(self):
        """
        Gets the name of this StoreDataGroupInterface.

        :return: The name of this StoreDataGroupInterface.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this StoreDataGroupInterface.

        :param name: The name of this StoreDataGroupInterface.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def code(self):
        """
        Gets the code of this StoreDataGroupInterface.
        Group code.

        :return: The code of this StoreDataGroupInterface.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this StoreDataGroupInterface.
        Group code.

        :param code: The code of this StoreDataGroupInterface.
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this StoreDataGroupInterface.

        :return: The extension_attributes of this StoreDataGroupInterface.
        :rtype: StoreDataGroupExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this StoreDataGroupInterface.

        :param extension_attributes: The extension_attributes of this StoreDataGroupInterface.
        :type: StoreDataGroupExtensionInterface
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
        if not isinstance(other, StoreDataGroupInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other