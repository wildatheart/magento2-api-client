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


class CatalogDataProductAttributeMediaGalleryEntryExtensionInterface(object):
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
        'video_content': 'FrameworkDataVideoContentInterface'
    }

    attribute_map = {
        'video_content': 'video_content'
    }

    def __init__(self, video_content=None):
        """
        CatalogDataProductAttributeMediaGalleryEntryExtensionInterface - a model defined in Swagger
        """

        self._video_content = None

        if video_content is not None:
          self.video_content = video_content

    @property
    def video_content(self):
        """
        Gets the video_content of this CatalogDataProductAttributeMediaGalleryEntryExtensionInterface.

        :return: The video_content of this CatalogDataProductAttributeMediaGalleryEntryExtensionInterface.
        :rtype: FrameworkDataVideoContentInterface
        """
        return self._video_content

    @video_content.setter
    def video_content(self, video_content):
        """
        Sets the video_content of this CatalogDataProductAttributeMediaGalleryEntryExtensionInterface.

        :param video_content: The video_content of this CatalogDataProductAttributeMediaGalleryEntryExtensionInterface.
        :type: FrameworkDataVideoContentInterface
        """

        self._video_content = video_content

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
        if not isinstance(other, CatalogDataProductAttributeMediaGalleryEntryExtensionInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
