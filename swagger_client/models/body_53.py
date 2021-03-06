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


class Body53(object):
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
        'customer_id': 'int',
        'store_id': 'int'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'store_id': 'storeId'
    }

    def __init__(self, customer_id=None, store_id=None):
        """
        Body53 - a model defined in Swagger
        """

        self._customer_id = None
        self._store_id = None

        self.customer_id = customer_id
        self.store_id = store_id

    @property
    def customer_id(self):
        """
        Gets the customer_id of this Body53.
        The customer ID.

        :return: The customer_id of this Body53.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this Body53.
        The customer ID.

        :param customer_id: The customer_id of this Body53.
        :type: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")

        self._customer_id = customer_id

    @property
    def store_id(self):
        """
        Gets the store_id of this Body53.

        :return: The store_id of this Body53.
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """
        Sets the store_id of this Body53.

        :param store_id: The store_id of this Body53.
        :type: int
        """
        if store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")

        self._store_id = store_id

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
        if not isinstance(other, Body53):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
