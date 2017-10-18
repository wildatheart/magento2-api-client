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


class TaxDataTaxRateSearchResultsInterface(object):
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
        'items': 'list[TaxDataTaxRateInterface]',
        'search_criteria': 'FrameworkSearchCriteriaInterface',
        'total_count': 'int'
    }

    attribute_map = {
        'items': 'items',
        'search_criteria': 'search_criteria',
        'total_count': 'total_count'
    }

    def __init__(self, items=None, search_criteria=None, total_count=None):
        """
        TaxDataTaxRateSearchResultsInterface - a model defined in Swagger
        """

        self._items = None
        self._search_criteria = None
        self._total_count = None

        self.items = items
        self.search_criteria = search_criteria
        self.total_count = total_count

    @property
    def items(self):
        """
        Gets the items of this TaxDataTaxRateSearchResultsInterface.
        Items

        :return: The items of this TaxDataTaxRateSearchResultsInterface.
        :rtype: list[TaxDataTaxRateInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this TaxDataTaxRateSearchResultsInterface.
        Items

        :param items: The items of this TaxDataTaxRateSearchResultsInterface.
        :type: list[TaxDataTaxRateInterface]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def search_criteria(self):
        """
        Gets the search_criteria of this TaxDataTaxRateSearchResultsInterface.

        :return: The search_criteria of this TaxDataTaxRateSearchResultsInterface.
        :rtype: FrameworkSearchCriteriaInterface
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """
        Sets the search_criteria of this TaxDataTaxRateSearchResultsInterface.

        :param search_criteria: The search_criteria of this TaxDataTaxRateSearchResultsInterface.
        :type: FrameworkSearchCriteriaInterface
        """
        if search_criteria is None:
            raise ValueError("Invalid value for `search_criteria`, must not be `None`")

        self._search_criteria = search_criteria

    @property
    def total_count(self):
        """
        Gets the total_count of this TaxDataTaxRateSearchResultsInterface.
        Total count.

        :return: The total_count of this TaxDataTaxRateSearchResultsInterface.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this TaxDataTaxRateSearchResultsInterface.
        Total count.

        :param total_count: The total_count of this TaxDataTaxRateSearchResultsInterface.
        :type: int
        """
        if total_count is None:
            raise ValueError("Invalid value for `total_count`, must not be `None`")

        self._total_count = total_count

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
        if not isinstance(other, TaxDataTaxRateSearchResultsInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
