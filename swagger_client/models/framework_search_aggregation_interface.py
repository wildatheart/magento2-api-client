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


class FrameworkSearchAggregationInterface(object):
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
        'buckets': 'list[FrameworkSearchBucketInterface]',
        'bucket_names': 'list[str]'
    }

    attribute_map = {
        'buckets': 'buckets',
        'bucket_names': 'bucket_names'
    }

    def __init__(self, buckets=None, bucket_names=None):
        """
        FrameworkSearchAggregationInterface - a model defined in Swagger
        """

        self._buckets = None
        self._bucket_names = None

        self.buckets = buckets
        self.bucket_names = bucket_names

    @property
    def buckets(self):
        """
        Gets the buckets of this FrameworkSearchAggregationInterface.
        All Document fields

        :return: The buckets of this FrameworkSearchAggregationInterface.
        :rtype: list[FrameworkSearchBucketInterface]
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """
        Sets the buckets of this FrameworkSearchAggregationInterface.
        All Document fields

        :param buckets: The buckets of this FrameworkSearchAggregationInterface.
        :type: list[FrameworkSearchBucketInterface]
        """
        if buckets is None:
            raise ValueError("Invalid value for `buckets`, must not be `None`")

        self._buckets = buckets

    @property
    def bucket_names(self):
        """
        Gets the bucket_names of this FrameworkSearchAggregationInterface.
        Document field names

        :return: The bucket_names of this FrameworkSearchAggregationInterface.
        :rtype: list[str]
        """
        return self._bucket_names

    @bucket_names.setter
    def bucket_names(self, bucket_names):
        """
        Sets the bucket_names of this FrameworkSearchAggregationInterface.
        Document field names

        :param bucket_names: The bucket_names of this FrameworkSearchAggregationInterface.
        :type: list[str]
        """
        if bucket_names is None:
            raise ValueError("Invalid value for `bucket_names`, must not be `None`")

        self._bucket_names = bucket_names

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
        if not isinstance(other, FrameworkSearchAggregationInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
