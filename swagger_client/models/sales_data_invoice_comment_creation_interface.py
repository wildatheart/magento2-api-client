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


class SalesDataInvoiceCommentCreationInterface(object):
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
        'extension_attributes': 'SalesDataInvoiceCommentCreationExtensionInterface',
        'comment': 'str',
        'is_visible_on_front': 'int'
    }

    attribute_map = {
        'extension_attributes': 'extension_attributes',
        'comment': 'comment',
        'is_visible_on_front': 'is_visible_on_front'
    }

    def __init__(self, extension_attributes=None, comment=None, is_visible_on_front=None):
        """
        SalesDataInvoiceCommentCreationInterface - a model defined in Swagger
        """

        self._extension_attributes = None
        self._comment = None
        self._is_visible_on_front = None

        if extension_attributes is not None:
          self.extension_attributes = extension_attributes
        self.comment = comment
        self.is_visible_on_front = is_visible_on_front

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesDataInvoiceCommentCreationInterface.

        :return: The extension_attributes of this SalesDataInvoiceCommentCreationInterface.
        :rtype: SalesDataInvoiceCommentCreationExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesDataInvoiceCommentCreationInterface.

        :param extension_attributes: The extension_attributes of this SalesDataInvoiceCommentCreationInterface.
        :type: SalesDataInvoiceCommentCreationExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def comment(self):
        """
        Gets the comment of this SalesDataInvoiceCommentCreationInterface.
        Comment.

        :return: The comment of this SalesDataInvoiceCommentCreationInterface.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this SalesDataInvoiceCommentCreationInterface.
        Comment.

        :param comment: The comment of this SalesDataInvoiceCommentCreationInterface.
        :type: str
        """
        if comment is None:
            raise ValueError("Invalid value for `comment`, must not be `None`")

        self._comment = comment

    @property
    def is_visible_on_front(self):
        """
        Gets the is_visible_on_front of this SalesDataInvoiceCommentCreationInterface.
        Is-visible-on-storefront flag value.

        :return: The is_visible_on_front of this SalesDataInvoiceCommentCreationInterface.
        :rtype: int
        """
        return self._is_visible_on_front

    @is_visible_on_front.setter
    def is_visible_on_front(self, is_visible_on_front):
        """
        Sets the is_visible_on_front of this SalesDataInvoiceCommentCreationInterface.
        Is-visible-on-storefront flag value.

        :param is_visible_on_front: The is_visible_on_front of this SalesDataInvoiceCommentCreationInterface.
        :type: int
        """
        if is_visible_on_front is None:
            raise ValueError("Invalid value for `is_visible_on_front`, must not be `None`")

        self._is_visible_on_front = is_visible_on_front

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
        if not isinstance(other, SalesDataInvoiceCommentCreationInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
