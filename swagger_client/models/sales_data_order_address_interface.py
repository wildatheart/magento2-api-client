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


class SalesDataOrderAddressInterface(object):
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
        'address_type': 'str',
        'city': 'str',
        'company': 'str',
        'country_id': 'str',
        'customer_address_id': 'int',
        'customer_id': 'int',
        'email': 'str',
        'entity_id': 'int',
        'fax': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'middlename': 'str',
        'parent_id': 'int',
        'postcode': 'str',
        'prefix': 'str',
        'region': 'str',
        'region_code': 'str',
        'region_id': 'int',
        'street': 'list[str]',
        'suffix': 'str',
        'telephone': 'str',
        'vat_id': 'str',
        'vat_is_valid': 'int',
        'vat_request_date': 'str',
        'vat_request_id': 'str',
        'vat_request_success': 'int',
        'extension_attributes': 'SalesDataOrderAddressExtensionInterface'
    }

    attribute_map = {
        'address_type': 'address_type',
        'city': 'city',
        'company': 'company',
        'country_id': 'country_id',
        'customer_address_id': 'customer_address_id',
        'customer_id': 'customer_id',
        'email': 'email',
        'entity_id': 'entity_id',
        'fax': 'fax',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'middlename': 'middlename',
        'parent_id': 'parent_id',
        'postcode': 'postcode',
        'prefix': 'prefix',
        'region': 'region',
        'region_code': 'region_code',
        'region_id': 'region_id',
        'street': 'street',
        'suffix': 'suffix',
        'telephone': 'telephone',
        'vat_id': 'vat_id',
        'vat_is_valid': 'vat_is_valid',
        'vat_request_date': 'vat_request_date',
        'vat_request_id': 'vat_request_id',
        'vat_request_success': 'vat_request_success',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, address_type=None, city=None, company=None, country_id=None, customer_address_id=None, customer_id=None, email=None, entity_id=None, fax=None, firstname=None, lastname=None, middlename=None, parent_id=None, postcode=None, prefix=None, region=None, region_code=None, region_id=None, street=None, suffix=None, telephone=None, vat_id=None, vat_is_valid=None, vat_request_date=None, vat_request_id=None, vat_request_success=None, extension_attributes=None):
        """
        SalesDataOrderAddressInterface - a model defined in Swagger
        """

        self._address_type = None
        self._city = None
        self._company = None
        self._country_id = None
        self._customer_address_id = None
        self._customer_id = None
        self._email = None
        self._entity_id = None
        self._fax = None
        self._firstname = None
        self._lastname = None
        self._middlename = None
        self._parent_id = None
        self._postcode = None
        self._prefix = None
        self._region = None
        self._region_code = None
        self._region_id = None
        self._street = None
        self._suffix = None
        self._telephone = None
        self._vat_id = None
        self._vat_is_valid = None
        self._vat_request_date = None
        self._vat_request_id = None
        self._vat_request_success = None
        self._extension_attributes = None

        self.address_type = address_type
        self.city = city
        if company is not None:
          self.company = company
        self.country_id = country_id
        if customer_address_id is not None:
          self.customer_address_id = customer_address_id
        if customer_id is not None:
          self.customer_id = customer_id
        if email is not None:
          self.email = email
        if entity_id is not None:
          self.entity_id = entity_id
        if fax is not None:
          self.fax = fax
        self.firstname = firstname
        self.lastname = lastname
        if middlename is not None:
          self.middlename = middlename
        if parent_id is not None:
          self.parent_id = parent_id
        self.postcode = postcode
        if prefix is not None:
          self.prefix = prefix
        if region is not None:
          self.region = region
        if region_code is not None:
          self.region_code = region_code
        if region_id is not None:
          self.region_id = region_id
        if street is not None:
          self.street = street
        if suffix is not None:
          self.suffix = suffix
        self.telephone = telephone
        if vat_id is not None:
          self.vat_id = vat_id
        if vat_is_valid is not None:
          self.vat_is_valid = vat_is_valid
        if vat_request_date is not None:
          self.vat_request_date = vat_request_date
        if vat_request_id is not None:
          self.vat_request_id = vat_request_id
        if vat_request_success is not None:
          self.vat_request_success = vat_request_success
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def address_type(self):
        """
        Gets the address_type of this SalesDataOrderAddressInterface.
        Address type.

        :return: The address_type of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """
        Sets the address_type of this SalesDataOrderAddressInterface.
        Address type.

        :param address_type: The address_type of this SalesDataOrderAddressInterface.
        :type: str
        """
        if address_type is None:
            raise ValueError("Invalid value for `address_type`, must not be `None`")

        self._address_type = address_type

    @property
    def city(self):
        """
        Gets the city of this SalesDataOrderAddressInterface.
        City.

        :return: The city of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this SalesDataOrderAddressInterface.
        City.

        :param city: The city of this SalesDataOrderAddressInterface.
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")

        self._city = city

    @property
    def company(self):
        """
        Gets the company of this SalesDataOrderAddressInterface.
        Company.

        :return: The company of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this SalesDataOrderAddressInterface.
        Company.

        :param company: The company of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._company = company

    @property
    def country_id(self):
        """
        Gets the country_id of this SalesDataOrderAddressInterface.
        Country ID.

        :return: The country_id of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """
        Sets the country_id of this SalesDataOrderAddressInterface.
        Country ID.

        :param country_id: The country_id of this SalesDataOrderAddressInterface.
        :type: str
        """
        if country_id is None:
            raise ValueError("Invalid value for `country_id`, must not be `None`")

        self._country_id = country_id

    @property
    def customer_address_id(self):
        """
        Gets the customer_address_id of this SalesDataOrderAddressInterface.
        Country address ID.

        :return: The customer_address_id of this SalesDataOrderAddressInterface.
        :rtype: int
        """
        return self._customer_address_id

    @customer_address_id.setter
    def customer_address_id(self, customer_address_id):
        """
        Sets the customer_address_id of this SalesDataOrderAddressInterface.
        Country address ID.

        :param customer_address_id: The customer_address_id of this SalesDataOrderAddressInterface.
        :type: int
        """

        self._customer_address_id = customer_address_id

    @property
    def customer_id(self):
        """
        Gets the customer_id of this SalesDataOrderAddressInterface.
        Customer ID.

        :return: The customer_id of this SalesDataOrderAddressInterface.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this SalesDataOrderAddressInterface.
        Customer ID.

        :param customer_id: The customer_id of this SalesDataOrderAddressInterface.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def email(self):
        """
        Gets the email of this SalesDataOrderAddressInterface.
        Email address.

        :return: The email of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this SalesDataOrderAddressInterface.
        Email address.

        :param email: The email of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._email = email

    @property
    def entity_id(self):
        """
        Gets the entity_id of this SalesDataOrderAddressInterface.
        Order address ID.

        :return: The entity_id of this SalesDataOrderAddressInterface.
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this SalesDataOrderAddressInterface.
        Order address ID.

        :param entity_id: The entity_id of this SalesDataOrderAddressInterface.
        :type: int
        """

        self._entity_id = entity_id

    @property
    def fax(self):
        """
        Gets the fax of this SalesDataOrderAddressInterface.
        Fax number.

        :return: The fax of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this SalesDataOrderAddressInterface.
        Fax number.

        :param fax: The fax of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._fax = fax

    @property
    def firstname(self):
        """
        Gets the firstname of this SalesDataOrderAddressInterface.
        First name.

        :return: The firstname of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this SalesDataOrderAddressInterface.
        First name.

        :param firstname: The firstname of this SalesDataOrderAddressInterface.
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this SalesDataOrderAddressInterface.
        Last name.

        :return: The lastname of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this SalesDataOrderAddressInterface.
        Last name.

        :param lastname: The lastname of this SalesDataOrderAddressInterface.
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def middlename(self):
        """
        Gets the middlename of this SalesDataOrderAddressInterface.
        Middle name.

        :return: The middlename of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """
        Sets the middlename of this SalesDataOrderAddressInterface.
        Middle name.

        :param middlename: The middlename of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._middlename = middlename

    @property
    def parent_id(self):
        """
        Gets the parent_id of this SalesDataOrderAddressInterface.
        Parent ID.

        :return: The parent_id of this SalesDataOrderAddressInterface.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this SalesDataOrderAddressInterface.
        Parent ID.

        :param parent_id: The parent_id of this SalesDataOrderAddressInterface.
        :type: int
        """

        self._parent_id = parent_id

    @property
    def postcode(self):
        """
        Gets the postcode of this SalesDataOrderAddressInterface.
        Postal code.

        :return: The postcode of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this SalesDataOrderAddressInterface.
        Postal code.

        :param postcode: The postcode of this SalesDataOrderAddressInterface.
        :type: str
        """
        if postcode is None:
            raise ValueError("Invalid value for `postcode`, must not be `None`")

        self._postcode = postcode

    @property
    def prefix(self):
        """
        Gets the prefix of this SalesDataOrderAddressInterface.
        Prefix.

        :return: The prefix of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this SalesDataOrderAddressInterface.
        Prefix.

        :param prefix: The prefix of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._prefix = prefix

    @property
    def region(self):
        """
        Gets the region of this SalesDataOrderAddressInterface.
        Region.

        :return: The region of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this SalesDataOrderAddressInterface.
        Region.

        :param region: The region of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._region = region

    @property
    def region_code(self):
        """
        Gets the region_code of this SalesDataOrderAddressInterface.
        Region code.

        :return: The region_code of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """
        Sets the region_code of this SalesDataOrderAddressInterface.
        Region code.

        :param region_code: The region_code of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._region_code = region_code

    @property
    def region_id(self):
        """
        Gets the region_id of this SalesDataOrderAddressInterface.
        Region ID.

        :return: The region_id of this SalesDataOrderAddressInterface.
        :rtype: int
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """
        Sets the region_id of this SalesDataOrderAddressInterface.
        Region ID.

        :param region_id: The region_id of this SalesDataOrderAddressInterface.
        :type: int
        """

        self._region_id = region_id

    @property
    def street(self):
        """
        Gets the street of this SalesDataOrderAddressInterface.
        Array of any street values. Otherwise, null.

        :return: The street of this SalesDataOrderAddressInterface.
        :rtype: list[str]
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this SalesDataOrderAddressInterface.
        Array of any street values. Otherwise, null.

        :param street: The street of this SalesDataOrderAddressInterface.
        :type: list[str]
        """

        self._street = street

    @property
    def suffix(self):
        """
        Gets the suffix of this SalesDataOrderAddressInterface.
        Suffix.

        :return: The suffix of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this SalesDataOrderAddressInterface.
        Suffix.

        :param suffix: The suffix of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._suffix = suffix

    @property
    def telephone(self):
        """
        Gets the telephone of this SalesDataOrderAddressInterface.
        Telephone number.

        :return: The telephone of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """
        Sets the telephone of this SalesDataOrderAddressInterface.
        Telephone number.

        :param telephone: The telephone of this SalesDataOrderAddressInterface.
        :type: str
        """
        if telephone is None:
            raise ValueError("Invalid value for `telephone`, must not be `None`")

        self._telephone = telephone

    @property
    def vat_id(self):
        """
        Gets the vat_id of this SalesDataOrderAddressInterface.
        VAT ID.

        :return: The vat_id of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._vat_id

    @vat_id.setter
    def vat_id(self, vat_id):
        """
        Sets the vat_id of this SalesDataOrderAddressInterface.
        VAT ID.

        :param vat_id: The vat_id of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._vat_id = vat_id

    @property
    def vat_is_valid(self):
        """
        Gets the vat_is_valid of this SalesDataOrderAddressInterface.
        VAT-is-valid flag value.

        :return: The vat_is_valid of this SalesDataOrderAddressInterface.
        :rtype: int
        """
        return self._vat_is_valid

    @vat_is_valid.setter
    def vat_is_valid(self, vat_is_valid):
        """
        Sets the vat_is_valid of this SalesDataOrderAddressInterface.
        VAT-is-valid flag value.

        :param vat_is_valid: The vat_is_valid of this SalesDataOrderAddressInterface.
        :type: int
        """

        self._vat_is_valid = vat_is_valid

    @property
    def vat_request_date(self):
        """
        Gets the vat_request_date of this SalesDataOrderAddressInterface.
        VAT request date.

        :return: The vat_request_date of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._vat_request_date

    @vat_request_date.setter
    def vat_request_date(self, vat_request_date):
        """
        Sets the vat_request_date of this SalesDataOrderAddressInterface.
        VAT request date.

        :param vat_request_date: The vat_request_date of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._vat_request_date = vat_request_date

    @property
    def vat_request_id(self):
        """
        Gets the vat_request_id of this SalesDataOrderAddressInterface.
        VAT request ID.

        :return: The vat_request_id of this SalesDataOrderAddressInterface.
        :rtype: str
        """
        return self._vat_request_id

    @vat_request_id.setter
    def vat_request_id(self, vat_request_id):
        """
        Sets the vat_request_id of this SalesDataOrderAddressInterface.
        VAT request ID.

        :param vat_request_id: The vat_request_id of this SalesDataOrderAddressInterface.
        :type: str
        """

        self._vat_request_id = vat_request_id

    @property
    def vat_request_success(self):
        """
        Gets the vat_request_success of this SalesDataOrderAddressInterface.
        VAT-request-success flag value.

        :return: The vat_request_success of this SalesDataOrderAddressInterface.
        :rtype: int
        """
        return self._vat_request_success

    @vat_request_success.setter
    def vat_request_success(self, vat_request_success):
        """
        Sets the vat_request_success of this SalesDataOrderAddressInterface.
        VAT-request-success flag value.

        :param vat_request_success: The vat_request_success of this SalesDataOrderAddressInterface.
        :type: int
        """

        self._vat_request_success = vat_request_success

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesDataOrderAddressInterface.

        :return: The extension_attributes of this SalesDataOrderAddressInterface.
        :rtype: SalesDataOrderAddressExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesDataOrderAddressInterface.

        :param extension_attributes: The extension_attributes of this SalesDataOrderAddressInterface.
        :type: SalesDataOrderAddressExtensionInterface
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
        if not isinstance(other, SalesDataOrderAddressInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
