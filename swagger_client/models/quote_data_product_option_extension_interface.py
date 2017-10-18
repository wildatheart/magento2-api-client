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


class QuoteDataProductOptionExtensionInterface(object):
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
        'custom_options': 'list[CatalogDataCustomOptionInterface]',
        'bundle_options': 'list[BundleDataBundleOptionInterface]',
        'downloadable_option': 'DownloadableDataDownloadableOptionInterface',
        'configurable_item_options': 'list[ConfigurableProductDataConfigurableItemOptionValueInterface]'
    }

    attribute_map = {
        'custom_options': 'custom_options',
        'bundle_options': 'bundle_options',
        'downloadable_option': 'downloadable_option',
        'configurable_item_options': 'configurable_item_options'
    }

    def __init__(self, custom_options=None, bundle_options=None, downloadable_option=None, configurable_item_options=None):
        """
        QuoteDataProductOptionExtensionInterface - a model defined in Swagger
        """

        self._custom_options = None
        self._bundle_options = None
        self._downloadable_option = None
        self._configurable_item_options = None

        if custom_options is not None:
          self.custom_options = custom_options
        if bundle_options is not None:
          self.bundle_options = bundle_options
        if downloadable_option is not None:
          self.downloadable_option = downloadable_option
        if configurable_item_options is not None:
          self.configurable_item_options = configurable_item_options

    @property
    def custom_options(self):
        """
        Gets the custom_options of this QuoteDataProductOptionExtensionInterface.

        :return: The custom_options of this QuoteDataProductOptionExtensionInterface.
        :rtype: list[CatalogDataCustomOptionInterface]
        """
        return self._custom_options

    @custom_options.setter
    def custom_options(self, custom_options):
        """
        Sets the custom_options of this QuoteDataProductOptionExtensionInterface.

        :param custom_options: The custom_options of this QuoteDataProductOptionExtensionInterface.
        :type: list[CatalogDataCustomOptionInterface]
        """

        self._custom_options = custom_options

    @property
    def bundle_options(self):
        """
        Gets the bundle_options of this QuoteDataProductOptionExtensionInterface.

        :return: The bundle_options of this QuoteDataProductOptionExtensionInterface.
        :rtype: list[BundleDataBundleOptionInterface]
        """
        return self._bundle_options

    @bundle_options.setter
    def bundle_options(self, bundle_options):
        """
        Sets the bundle_options of this QuoteDataProductOptionExtensionInterface.

        :param bundle_options: The bundle_options of this QuoteDataProductOptionExtensionInterface.
        :type: list[BundleDataBundleOptionInterface]
        """

        self._bundle_options = bundle_options

    @property
    def downloadable_option(self):
        """
        Gets the downloadable_option of this QuoteDataProductOptionExtensionInterface.

        :return: The downloadable_option of this QuoteDataProductOptionExtensionInterface.
        :rtype: DownloadableDataDownloadableOptionInterface
        """
        return self._downloadable_option

    @downloadable_option.setter
    def downloadable_option(self, downloadable_option):
        """
        Sets the downloadable_option of this QuoteDataProductOptionExtensionInterface.

        :param downloadable_option: The downloadable_option of this QuoteDataProductOptionExtensionInterface.
        :type: DownloadableDataDownloadableOptionInterface
        """

        self._downloadable_option = downloadable_option

    @property
    def configurable_item_options(self):
        """
        Gets the configurable_item_options of this QuoteDataProductOptionExtensionInterface.

        :return: The configurable_item_options of this QuoteDataProductOptionExtensionInterface.
        :rtype: list[ConfigurableProductDataConfigurableItemOptionValueInterface]
        """
        return self._configurable_item_options

    @configurable_item_options.setter
    def configurable_item_options(self, configurable_item_options):
        """
        Sets the configurable_item_options of this QuoteDataProductOptionExtensionInterface.

        :param configurable_item_options: The configurable_item_options of this QuoteDataProductOptionExtensionInterface.
        :type: list[ConfigurableProductDataConfigurableItemOptionValueInterface]
        """

        self._configurable_item_options = configurable_item_options

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
        if not isinstance(other, QuoteDataProductOptionExtensionInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other