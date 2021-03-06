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


class Body97(object):
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
        'items': 'list[SalesDataCreditmemoItemCreationInterface]',
        'notify': 'bool',
        'append_comment': 'bool',
        'comment': 'SalesDataCreditmemoCommentCreationInterface',
        'arguments': 'SalesDataCreditmemoCreationArgumentsInterface'
    }

    attribute_map = {
        'items': 'items',
        'notify': 'notify',
        'append_comment': 'appendComment',
        'comment': 'comment',
        'arguments': 'arguments'
    }

    def __init__(self, items=None, notify=None, append_comment=None, comment=None, arguments=None):
        """
        Body97 - a model defined in Swagger
        """

        self._items = None
        self._notify = None
        self._append_comment = None
        self._comment = None
        self._arguments = None

        if items is not None:
          self.items = items
        if notify is not None:
          self.notify = notify
        if append_comment is not None:
          self.append_comment = append_comment
        if comment is not None:
          self.comment = comment
        if arguments is not None:
          self.arguments = arguments

    @property
    def items(self):
        """
        Gets the items of this Body97.

        :return: The items of this Body97.
        :rtype: list[SalesDataCreditmemoItemCreationInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this Body97.

        :param items: The items of this Body97.
        :type: list[SalesDataCreditmemoItemCreationInterface]
        """

        self._items = items

    @property
    def notify(self):
        """
        Gets the notify of this Body97.

        :return: The notify of this Body97.
        :rtype: bool
        """
        return self._notify

    @notify.setter
    def notify(self, notify):
        """
        Sets the notify of this Body97.

        :param notify: The notify of this Body97.
        :type: bool
        """

        self._notify = notify

    @property
    def append_comment(self):
        """
        Gets the append_comment of this Body97.

        :return: The append_comment of this Body97.
        :rtype: bool
        """
        return self._append_comment

    @append_comment.setter
    def append_comment(self, append_comment):
        """
        Sets the append_comment of this Body97.

        :param append_comment: The append_comment of this Body97.
        :type: bool
        """

        self._append_comment = append_comment

    @property
    def comment(self):
        """
        Gets the comment of this Body97.

        :return: The comment of this Body97.
        :rtype: SalesDataCreditmemoCommentCreationInterface
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Body97.

        :param comment: The comment of this Body97.
        :type: SalesDataCreditmemoCommentCreationInterface
        """

        self._comment = comment

    @property
    def arguments(self):
        """
        Gets the arguments of this Body97.

        :return: The arguments of this Body97.
        :rtype: SalesDataCreditmemoCreationArgumentsInterface
        """
        return self._arguments

    @arguments.setter
    def arguments(self, arguments):
        """
        Sets the arguments of this Body97.

        :param arguments: The arguments of this Body97.
        :type: SalesDataCreditmemoCreationArgumentsInterface
        """

        self._arguments = arguments

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
        if not isinstance(other, Body97):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
