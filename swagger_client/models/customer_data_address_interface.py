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


class CustomerDataAddressInterface(object):
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
        'customer_id': 'int',
        'region': 'CustomerDataRegionInterface',
        'region_id': 'int',
        'country_id': 'str',
        'street': 'list[str]',
        'company': 'str',
        'telephone': 'str',
        'fax': 'str',
        'postcode': 'str',
        'city': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'middlename': 'str',
        'prefix': 'str',
        'suffix': 'str',
        'vat_id': 'str',
        'default_shipping': 'bool',
        'default_billing': 'bool',
        'extension_attributes': 'CustomerDataAddressExtensionInterface',
        'custom_attributes': 'list[FrameworkAttributeInterface]'
    }

    attribute_map = {
        'id': 'id',
        'customer_id': 'customer_id',
        'region': 'region',
        'region_id': 'region_id',
        'country_id': 'country_id',
        'street': 'street',
        'company': 'company',
        'telephone': 'telephone',
        'fax': 'fax',
        'postcode': 'postcode',
        'city': 'city',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'middlename': 'middlename',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'vat_id': 'vat_id',
        'default_shipping': 'default_shipping',
        'default_billing': 'default_billing',
        'extension_attributes': 'extension_attributes',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, id=None, customer_id=None, region=None, region_id=None, country_id=None, street=None, company=None, telephone=None, fax=None, postcode=None, city=None, firstname=None, lastname=None, middlename=None, prefix=None, suffix=None, vat_id=None, default_shipping=None, default_billing=None, extension_attributes=None, custom_attributes=None):
        """
        CustomerDataAddressInterface - a model defined in Swagger
        """

        self._id = None
        self._customer_id = None
        self._region = None
        self._region_id = None
        self._country_id = None
        self._street = None
        self._company = None
        self._telephone = None
        self._fax = None
        self._postcode = None
        self._city = None
        self._firstname = None
        self._lastname = None
        self._middlename = None
        self._prefix = None
        self._suffix = None
        self._vat_id = None
        self._default_shipping = None
        self._default_billing = None
        self._extension_attributes = None
        self._custom_attributes = None

        if id is not None:
          self.id = id
        if customer_id is not None:
          self.customer_id = customer_id
        if region is not None:
          self.region = region
        if region_id is not None:
          self.region_id = region_id
        if country_id is not None:
          self.country_id = country_id
        if street is not None:
          self.street = street
        if company is not None:
          self.company = company
        if telephone is not None:
          self.telephone = telephone
        if fax is not None:
          self.fax = fax
        if postcode is not None:
          self.postcode = postcode
        if city is not None:
          self.city = city
        if firstname is not None:
          self.firstname = firstname
        if lastname is not None:
          self.lastname = lastname
        if middlename is not None:
          self.middlename = middlename
        if prefix is not None:
          self.prefix = prefix
        if suffix is not None:
          self.suffix = suffix
        if vat_id is not None:
          self.vat_id = vat_id
        if default_shipping is not None:
          self.default_shipping = default_shipping
        if default_billing is not None:
          self.default_billing = default_billing
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes
        if custom_attributes is not None:
          self.custom_attributes = custom_attributes

    @property
    def id(self):
        """
        Gets the id of this CustomerDataAddressInterface.
        ID

        :return: The id of this CustomerDataAddressInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomerDataAddressInterface.
        ID

        :param id: The id of this CustomerDataAddressInterface.
        :type: int
        """

        self._id = id

    @property
    def customer_id(self):
        """
        Gets the customer_id of this CustomerDataAddressInterface.
        Customer ID

        :return: The customer_id of this CustomerDataAddressInterface.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this CustomerDataAddressInterface.
        Customer ID

        :param customer_id: The customer_id of this CustomerDataAddressInterface.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def region(self):
        """
        Gets the region of this CustomerDataAddressInterface.

        :return: The region of this CustomerDataAddressInterface.
        :rtype: CustomerDataRegionInterface
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this CustomerDataAddressInterface.

        :param region: The region of this CustomerDataAddressInterface.
        :type: CustomerDataRegionInterface
        """

        self._region = region

    @property
    def region_id(self):
        """
        Gets the region_id of this CustomerDataAddressInterface.
        Region ID

        :return: The region_id of this CustomerDataAddressInterface.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this CustomerDataAddressInterface.
        Region ID

        :param region_id: The region_id of this CustomerDataAddressInterface.
        :type: int
        """

        self._region_id = region_id

    @property
    def country_id(self):
        """
        Gets the country_id of this CustomerDataAddressInterface.
        Country code in ISO_3166-2 format

        :return: The country_id of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """
        Sets the country_id of this CustomerDataAddressInterface.
        Country code in ISO_3166-2 format

        :param country_id: The country_id of this CustomerDataAddressInterface.
        :type: str
        """

        self._country_id = country_id

    @property
    def street(self):
        """
        Gets the street of this CustomerDataAddressInterface.
        Street

        :return: The street of this CustomerDataAddressInterface.
        :rtype: list[str]
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this CustomerDataAddressInterface.
        Street

        :param street: The street of this CustomerDataAddressInterface.
        :type: list[str]
        """

        self._street = street

    @property
    def company(self):
        """
        Gets the company of this CustomerDataAddressInterface.
        Company

        :return: The company of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this CustomerDataAddressInterface.
        Company

        :param company: The company of this CustomerDataAddressInterface.
        :type: str
        """

        self._company = company

    @property
    def telephone(self):
        """
        Gets the telephone of this CustomerDataAddressInterface.
        Telephone number

        :return: The telephone of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """
        Sets the telephone of this CustomerDataAddressInterface.
        Telephone number

        :param telephone: The telephone of this CustomerDataAddressInterface.
        :type: str
        """

        self._telephone = telephone

    @property
    def fax(self):
        """
        Gets the fax of this CustomerDataAddressInterface.
        Fax number

        :return: The fax of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this CustomerDataAddressInterface.
        Fax number

        :param fax: The fax of this CustomerDataAddressInterface.
        :type: str
        """

        self._fax = fax

    @property
    def postcode(self):
        """
        Gets the postcode of this CustomerDataAddressInterface.
        Postcode

        :return: The postcode of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this CustomerDataAddressInterface.
        Postcode

        :param postcode: The postcode of this CustomerDataAddressInterface.
        :type: str
        """

        self._postcode = postcode

    @property
    def city(self):
        """
        Gets the city of this CustomerDataAddressInterface.
        City name

        :return: The city of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this CustomerDataAddressInterface.
        City name

        :param city: The city of this CustomerDataAddressInterface.
        :type: str
        """

        self._city = city

    @property
    def firstname(self):
        """
        Gets the firstname of this CustomerDataAddressInterface.
        First name

        :return: The firstname of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this CustomerDataAddressInterface.
        First name

        :param firstname: The firstname of this CustomerDataAddressInterface.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this CustomerDataAddressInterface.
        Last name

        :return: The lastname of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this CustomerDataAddressInterface.
        Last name

        :param lastname: The lastname of this CustomerDataAddressInterface.
        :type: str
        """

        self._lastname = lastname

    @property
    def middlename(self):
        """
        Gets the middlename of this CustomerDataAddressInterface.
        Middle name

        :return: The middlename of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """
        Sets the middlename of this CustomerDataAddressInterface.
        Middle name

        :param middlename: The middlename of this CustomerDataAddressInterface.
        :type: str
        """

        self._middlename = middlename

    @property
    def prefix(self):
        """
        Gets the prefix of this CustomerDataAddressInterface.
        Prefix

        :return: The prefix of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this CustomerDataAddressInterface.
        Prefix

        :param prefix: The prefix of this CustomerDataAddressInterface.
        :type: str
        """

        self._prefix = prefix

    @property
    def suffix(self):
        """
        Gets the suffix of this CustomerDataAddressInterface.
        Suffix

        :return: The suffix of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this CustomerDataAddressInterface.
        Suffix

        :param suffix: The suffix of this CustomerDataAddressInterface.
        :type: str
        """

        self._suffix = suffix

    @property
    def vat_id(self):
        """
        Gets the vat_id of this CustomerDataAddressInterface.
        Vat id

        :return: The vat_id of this CustomerDataAddressInterface.
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """
        Sets the vat_id of this CustomerDataAddressInterface.
        Vat id

        :param vat_id: The vat_id of this CustomerDataAddressInterface.
        :type: str
        """

        self._vat_id = vat_id

    @property
    def default_shipping(self):
        """
        Gets the default_shipping of this CustomerDataAddressInterface.
        If this address is default shipping address.

        :return: The default_shipping of this CustomerDataAddressInterface.
        :rtype: bool
        """
        return self._default_shipping

    @default_shipping.setter
    def default_shipping(self, default_shipping):
        """
        Sets the default_shipping of this CustomerDataAddressInterface.
        If this address is default shipping address.

        :param default_shipping: The default_shipping of this CustomerDataAddressInterface.
        :type: bool
        """

        self._default_shipping = default_shipping

    @property
    def default_billing(self):
        """
        Gets the default_billing of this CustomerDataAddressInterface.
        If this address is default billing address

        :return: The default_billing of this CustomerDataAddressInterface.
        :rtype: bool
        """
        return self._default_billing

    @default_billing.setter
    def default_billing(self, default_billing):
        """
        Sets the default_billing of this CustomerDataAddressInterface.
        If this address is default billing address

        :param default_billing: The default_billing of this CustomerDataAddressInterface.
        :type: bool
        """

        self._default_billing = default_billing

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CustomerDataAddressInterface.

        :return: The extension_attributes of this CustomerDataAddressInterface.
        :rtype: CustomerDataAddressExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CustomerDataAddressInterface.

        :param extension_attributes: The extension_attributes of this CustomerDataAddressInterface.
        :type: CustomerDataAddressExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this CustomerDataAddressInterface.
        Custom attributes values.

        :return: The custom_attributes of this CustomerDataAddressInterface.
        :rtype: list[FrameworkAttributeInterface]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this CustomerDataAddressInterface.
        Custom attributes values.

        :param custom_attributes: The custom_attributes of this CustomerDataAddressInterface.
        :type: list[FrameworkAttributeInterface]
        """

        self._custom_attributes = custom_attributes

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
        if not isinstance(other, CustomerDataAddressInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
