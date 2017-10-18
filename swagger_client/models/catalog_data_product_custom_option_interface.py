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


class CatalogDataProductCustomOptionInterface(object):
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
        'product_sku': 'str',
        'option_id': 'int',
        'title': 'str',
        'type': 'str',
        'sort_order': 'int',
        'is_require': 'bool',
        'price': 'float',
        'price_type': 'str',
        'sku': 'str',
        'file_extension': 'str',
        'max_characters': 'int',
        'image_size_x': 'int',
        'image_size_y': 'int',
        'values': 'list[CatalogDataProductCustomOptionValuesInterface]',
        'extension_attributes': 'CatalogDataProductCustomOptionExtensionInterface'
    }

    attribute_map = {
        'product_sku': 'product_sku',
        'option_id': 'option_id',
        'title': 'title',
        'type': 'type',
        'sort_order': 'sort_order',
        'is_require': 'is_require',
        'price': 'price',
        'price_type': 'price_type',
        'sku': 'sku',
        'file_extension': 'file_extension',
        'max_characters': 'max_characters',
        'image_size_x': 'image_size_x',
        'image_size_y': 'image_size_y',
        'values': 'values',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, product_sku=None, option_id=None, title=None, type=None, sort_order=None, is_require=None, price=None, price_type=None, sku=None, file_extension=None, max_characters=None, image_size_x=None, image_size_y=None, values=None, extension_attributes=None):
        """
        CatalogDataProductCustomOptionInterface - a model defined in Swagger
        """

        self._product_sku = None
        self._option_id = None
        self._title = None
        self._type = None
        self._sort_order = None
        self._is_require = None
        self._price = None
        self._price_type = None
        self._sku = None
        self._file_extension = None
        self._max_characters = None
        self._image_size_x = None
        self._image_size_y = None
        self._values = None
        self._extension_attributes = None

        self.product_sku = product_sku
        if option_id is not None:
          self.option_id = option_id
        self.title = title
        self.type = type
        self.sort_order = sort_order
        self.is_require = is_require
        if price is not None:
          self.price = price
        if price_type is not None:
          self.price_type = price_type
        if sku is not None:
          self.sku = sku
        if file_extension is not None:
          self.file_extension = file_extension
        if max_characters is not None:
          self.max_characters = max_characters
        if image_size_x is not None:
          self.image_size_x = image_size_x
        if image_size_y is not None:
          self.image_size_y = image_size_y
        if values is not None:
          self.values = values
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def product_sku(self):
        """
        Gets the product_sku of this CatalogDataProductCustomOptionInterface.
        Product SKU

        :return: The product_sku of this CatalogDataProductCustomOptionInterface.
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """
        Sets the product_sku of this CatalogDataProductCustomOptionInterface.
        Product SKU

        :param product_sku: The product_sku of this CatalogDataProductCustomOptionInterface.
        :type: str
        """
        if product_sku is None:
            raise ValueError("Invalid value for `product_sku`, must not be `None`")

        self._product_sku = product_sku

    @property
    def option_id(self):
        """
        Gets the option_id of this CatalogDataProductCustomOptionInterface.
        Option id

        :return: The option_id of this CatalogDataProductCustomOptionInterface.
        :rtype: int
        """
        return self._option_id

    @option_id.setter
    def option_id(self, option_id):
        """
        Sets the option_id of this CatalogDataProductCustomOptionInterface.
        Option id

        :param option_id: The option_id of this CatalogDataProductCustomOptionInterface.
        :type: int
        """

        self._option_id = option_id

    @property
    def title(self):
        """
        Gets the title of this CatalogDataProductCustomOptionInterface.
        Option title

        :return: The title of this CatalogDataProductCustomOptionInterface.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CatalogDataProductCustomOptionInterface.
        Option title

        :param title: The title of this CatalogDataProductCustomOptionInterface.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def type(self):
        """
        Gets the type of this CatalogDataProductCustomOptionInterface.
        Option type

        :return: The type of this CatalogDataProductCustomOptionInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CatalogDataProductCustomOptionInterface.
        Option type

        :param type: The type of this CatalogDataProductCustomOptionInterface.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def sort_order(self):
        """
        Gets the sort_order of this CatalogDataProductCustomOptionInterface.
        Sort order

        :return: The sort_order of this CatalogDataProductCustomOptionInterface.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """
        Sets the sort_order of this CatalogDataProductCustomOptionInterface.
        Sort order

        :param sort_order: The sort_order of this CatalogDataProductCustomOptionInterface.
        :type: int
        """
        if sort_order is None:
            raise ValueError("Invalid value for `sort_order`, must not be `None`")

        self._sort_order = sort_order

    @property
    def is_require(self):
        """
        Gets the is_require of this CatalogDataProductCustomOptionInterface.
        Is require

        :return: The is_require of this CatalogDataProductCustomOptionInterface.
        :rtype: bool
        """
        return self._is_require

    @is_require.setter
    def is_require(self, is_require):
        """
        Sets the is_require of this CatalogDataProductCustomOptionInterface.
        Is require

        :param is_require: The is_require of this CatalogDataProductCustomOptionInterface.
        :type: bool
        """
        if is_require is None:
            raise ValueError("Invalid value for `is_require`, must not be `None`")

        self._is_require = is_require

    @property
    def price(self):
        """
        Gets the price of this CatalogDataProductCustomOptionInterface.
        Price

        :return: The price of this CatalogDataProductCustomOptionInterface.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this CatalogDataProductCustomOptionInterface.
        Price

        :param price: The price of this CatalogDataProductCustomOptionInterface.
        :type: float
        """

        self._price = price

    @property
    def price_type(self):
        """
        Gets the price_type of this CatalogDataProductCustomOptionInterface.
        Price type

        :return: The price_type of this CatalogDataProductCustomOptionInterface.
        :rtype: str
        """
        return self._price_type

    @price_type.setter
    def price_type(self, price_type):
        """
        Sets the price_type of this CatalogDataProductCustomOptionInterface.
        Price type

        :param price_type: The price_type of this CatalogDataProductCustomOptionInterface.
        :type: str
        """

        self._price_type = price_type

    @property
    def sku(self):
        """
        Gets the sku of this CatalogDataProductCustomOptionInterface.
        Sku

        :return: The sku of this CatalogDataProductCustomOptionInterface.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """
        Sets the sku of this CatalogDataProductCustomOptionInterface.
        Sku

        :param sku: The sku of this CatalogDataProductCustomOptionInterface.
        :type: str
        """

        self._sku = sku

    @property
    def file_extension(self):
        """
        Gets the file_extension of this CatalogDataProductCustomOptionInterface.

        :return: The file_extension of this CatalogDataProductCustomOptionInterface.
        :rtype: str
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """
        Sets the file_extension of this CatalogDataProductCustomOptionInterface.

        :param file_extension: The file_extension of this CatalogDataProductCustomOptionInterface.
        :type: str
        """

        self._file_extension = file_extension

    @property
    def max_characters(self):
        """
        Gets the max_characters of this CatalogDataProductCustomOptionInterface.

        :return: The max_characters of this CatalogDataProductCustomOptionInterface.
        :rtype: int
        """
        return self._max_characters

    @max_characters.setter
    def max_characters(self, max_characters):
        """
        Sets the max_characters of this CatalogDataProductCustomOptionInterface.

        :param max_characters: The max_characters of this CatalogDataProductCustomOptionInterface.
        :type: int
        """

        self._max_characters = max_characters

    @property
    def image_size_x(self):
        """
        Gets the image_size_x of this CatalogDataProductCustomOptionInterface.

        :return: The image_size_x of this CatalogDataProductCustomOptionInterface.
        :rtype: int
        """
        return self._image_size_x

    @image_size_x.setter
    def image_size_x(self, image_size_x):
        """
        Sets the image_size_x of this CatalogDataProductCustomOptionInterface.

        :param image_size_x: The image_size_x of this CatalogDataProductCustomOptionInterface.
        :type: int
        """

        self._image_size_x = image_size_x

    @property
    def image_size_y(self):
        """
        Gets the image_size_y of this CatalogDataProductCustomOptionInterface.

        :return: The image_size_y of this CatalogDataProductCustomOptionInterface.
        :rtype: int
        """
        return self._image_size_y

    @image_size_y.setter
    def image_size_y(self, image_size_y):
        """
        Sets the image_size_y of this CatalogDataProductCustomOptionInterface.

        :param image_size_y: The image_size_y of this CatalogDataProductCustomOptionInterface.
        :type: int
        """

        self._image_size_y = image_size_y

    @property
    def values(self):
        """
        Gets the values of this CatalogDataProductCustomOptionInterface.

        :return: The values of this CatalogDataProductCustomOptionInterface.
        :rtype: list[CatalogDataProductCustomOptionValuesInterface]
        """
        return self._values

    @values.setter
    def values(self, values):
        """
        Sets the values of this CatalogDataProductCustomOptionInterface.

        :param values: The values of this CatalogDataProductCustomOptionInterface.
        :type: list[CatalogDataProductCustomOptionValuesInterface]
        """

        self._values = values

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CatalogDataProductCustomOptionInterface.

        :return: The extension_attributes of this CatalogDataProductCustomOptionInterface.
        :rtype: CatalogDataProductCustomOptionExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CatalogDataProductCustomOptionInterface.

        :param extension_attributes: The extension_attributes of this CatalogDataProductCustomOptionInterface.
        :type: CatalogDataProductCustomOptionExtensionInterface
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
        if not isinstance(other, CatalogDataProductCustomOptionInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other