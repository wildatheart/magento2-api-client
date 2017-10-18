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


class QuoteDataTotalSegmentExtensionInterface(object):
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
        'tax_grandtotal_details': 'list[TaxDataGrandTotalDetailsInterface]'
    }

    attribute_map = {
        'tax_grandtotal_details': 'tax_grandtotal_details'
    }

    def __init__(self, tax_grandtotal_details=None):
        """
        QuoteDataTotalSegmentExtensionInterface - a model defined in Swagger
        """

        self._tax_grandtotal_details = None

        if tax_grandtotal_details is not None:
          self.tax_grandtotal_details = tax_grandtotal_details

    @property
    def tax_grandtotal_details(self):
        """
        Gets the tax_grandtotal_details of this QuoteDataTotalSegmentExtensionInterface.

        :return: The tax_grandtotal_details of this QuoteDataTotalSegmentExtensionInterface.
        :rtype: list[TaxDataGrandTotalDetailsInterface]
        """
        return self._tax_grandtotal_details

    @tax_grandtotal_details.setter
    def tax_grandtotal_details(self, tax_grandtotal_details):
        """
        Sets the tax_grandtotal_details of this QuoteDataTotalSegmentExtensionInterface.

        :param tax_grandtotal_details: The tax_grandtotal_details of this QuoteDataTotalSegmentExtensionInterface.
        :type: list[TaxDataGrandTotalDetailsInterface]
        """

        self._tax_grandtotal_details = tax_grandtotal_details

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
        if not isinstance(other, QuoteDataTotalSegmentExtensionInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
