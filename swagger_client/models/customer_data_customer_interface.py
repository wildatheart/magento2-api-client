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


class CustomerDataCustomerInterface(object):
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
        'group_id': 'int',
        'default_billing': 'str',
        'default_shipping': 'str',
        'confirmation': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'created_in': 'str',
        'dob': 'str',
        'email': 'str',
        'firstname': 'str',
        'lastname': 'str',
        'middlename': 'str',
        'prefix': 'str',
        'suffix': 'str',
        'gender': 'int',
        'store_id': 'int',
        'taxvat': 'str',
        'website_id': 'int',
        'addresses': 'list[CustomerDataAddressInterface]',
        'disable_auto_group_change': 'int',
        'extension_attributes': 'CustomerDataCustomerExtensionInterface',
        'custom_attributes': 'list[FrameworkAttributeInterface]'
    }

    attribute_map = {
        'id': 'id',
        'group_id': 'group_id',
        'default_billing': 'default_billing',
        'default_shipping': 'default_shipping',
        'confirmation': 'confirmation',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'created_in': 'created_in',
        'dob': 'dob',
        'email': 'email',
        'firstname': 'firstname',
        'lastname': 'lastname',
        'middlename': 'middlename',
        'prefix': 'prefix',
        'suffix': 'suffix',
        'gender': 'gender',
        'store_id': 'store_id',
        'taxvat': 'taxvat',
        'website_id': 'website_id',
        'addresses': 'addresses',
        'disable_auto_group_change': 'disable_auto_group_change',
        'extension_attributes': 'extension_attributes',
        'custom_attributes': 'custom_attributes'
    }

    def __init__(self, id=None, group_id=None, default_billing=None, default_shipping=None, confirmation=None, created_at=None, updated_at=None, created_in=None, dob=None, email=None, firstname=None, lastname=None, middlename=None, prefix=None, suffix=None, gender=None, store_id=None, taxvat=None, website_id=None, addresses=None, disable_auto_group_change=None, extension_attributes=None, custom_attributes=None):
        """
        CustomerDataCustomerInterface - a model defined in Swagger
        """

        self._id = None
        self._group_id = None
        self._default_billing = None
        self._default_shipping = None
        self._confirmation = None
        self._created_at = None
        self._updated_at = None
        self._created_in = None
        self._dob = None
        self._email = None
        self._firstname = None
        self._lastname = None
        self._middlename = None
        self._prefix = None
        self._suffix = None
        self._gender = None
        self._store_id = None
        self._taxvat = None
        self._website_id = None
        self._addresses = None
        self._disable_auto_group_change = None
        self._extension_attributes = None
        self._custom_attributes = None

        if id is not None:
          self.id = id
        if group_id is not None:
          self.group_id = group_id
        if default_billing is not None:
          self.default_billing = default_billing
        if default_shipping is not None:
          self.default_shipping = default_shipping
        if confirmation is not None:
          self.confirmation = confirmation
        if created_at is not None:
          self.created_at = created_at
        if updated_at is not None:
          self.updated_at = updated_at
        if created_in is not None:
          self.created_in = created_in
        if dob is not None:
          self.dob = dob
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        if middlename is not None:
          self.middlename = middlename
        if prefix is not None:
          self.prefix = prefix
        if suffix is not None:
          self.suffix = suffix
        if gender is not None:
          self.gender = gender
        if store_id is not None:
          self.store_id = store_id
        if taxvat is not None:
          self.taxvat = taxvat
        if website_id is not None:
          self.website_id = website_id
        if addresses is not None:
          self.addresses = addresses
        if disable_auto_group_change is not None:
          self.disable_auto_group_change = disable_auto_group_change
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes
        if custom_attributes is not None:
          self.custom_attributes = custom_attributes

    @property
    def id(self):
        """
        Gets the id of this CustomerDataCustomerInterface.
        Customer id

        :return: The id of this CustomerDataCustomerInterface.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomerDataCustomerInterface.
        Customer id

        :param id: The id of this CustomerDataCustomerInterface.
        :type: int
        """

        self._id = id

    @property
    def group_id(self):
        """
        Gets the group_id of this CustomerDataCustomerInterface.
        Group id

        :return: The group_id of this CustomerDataCustomerInterface.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this CustomerDataCustomerInterface.
        Group id

        :param group_id: The group_id of this CustomerDataCustomerInterface.
        :type: int
        """

        self._group_id = group_id

    @property
    def default_billing(self):
        """
        Gets the default_billing of this CustomerDataCustomerInterface.
        Default billing address id

        :return: The default_billing of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._default_billing

    @default_billing.setter
    def default_billing(self, default_billing):
        """
        Sets the default_billing of this CustomerDataCustomerInterface.
        Default billing address id

        :param default_billing: The default_billing of this CustomerDataCustomerInterface.
        :type: str
        """

        self._default_billing = default_billing

    @property
    def default_shipping(self):
        """
        Gets the default_shipping of this CustomerDataCustomerInterface.
        Default shipping address id

        :return: The default_shipping of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._default_shipping

    @default_shipping.setter
    def default_shipping(self, default_shipping):
        """
        Sets the default_shipping of this CustomerDataCustomerInterface.
        Default shipping address id

        :param default_shipping: The default_shipping of this CustomerDataCustomerInterface.
        :type: str
        """

        self._default_shipping = default_shipping

    @property
    def confirmation(self):
        """
        Gets the confirmation of this CustomerDataCustomerInterface.
        Confirmation

        :return: The confirmation of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._confirmation

    @confirmation.setter
    def confirmation(self, confirmation):
        """
        Sets the confirmation of this CustomerDataCustomerInterface.
        Confirmation

        :param confirmation: The confirmation of this CustomerDataCustomerInterface.
        :type: str
        """

        self._confirmation = confirmation

    @property
    def created_at(self):
        """
        Gets the created_at of this CustomerDataCustomerInterface.
        Created at time

        :return: The created_at of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CustomerDataCustomerInterface.
        Created at time

        :param created_at: The created_at of this CustomerDataCustomerInterface.
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CustomerDataCustomerInterface.
        Updated at time

        :return: The updated_at of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CustomerDataCustomerInterface.
        Updated at time

        :param updated_at: The updated_at of this CustomerDataCustomerInterface.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def created_in(self):
        """
        Gets the created_in of this CustomerDataCustomerInterface.
        Created in area

        :return: The created_in of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._created_in

    @created_in.setter
    def created_in(self, created_in):
        """
        Sets the created_in of this CustomerDataCustomerInterface.
        Created in area

        :param created_in: The created_in of this CustomerDataCustomerInterface.
        :type: str
        """

        self._created_in = created_in

    @property
    def dob(self):
        """
        Gets the dob of this CustomerDataCustomerInterface.
        Date of birth

        :return: The dob of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """
        Sets the dob of this CustomerDataCustomerInterface.
        Date of birth

        :param dob: The dob of this CustomerDataCustomerInterface.
        :type: str
        """

        self._dob = dob

    @property
    def email(self):
        """
        Gets the email of this CustomerDataCustomerInterface.
        Email address

        :return: The email of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerDataCustomerInterface.
        Email address

        :param email: The email of this CustomerDataCustomerInterface.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def firstname(self):
        """
        Gets the firstname of this CustomerDataCustomerInterface.
        First name

        :return: The firstname of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this CustomerDataCustomerInterface.
        First name

        :param firstname: The firstname of this CustomerDataCustomerInterface.
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this CustomerDataCustomerInterface.
        Last name

        :return: The lastname of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this CustomerDataCustomerInterface.
        Last name

        :param lastname: The lastname of this CustomerDataCustomerInterface.
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def middlename(self):
        """
        Gets the middlename of this CustomerDataCustomerInterface.
        Middle name

        :return: The middlename of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._middlename

    @middlename.setter
    def middlename(self, middlename):
        """
        Sets the middlename of this CustomerDataCustomerInterface.
        Middle name

        :param middlename: The middlename of this CustomerDataCustomerInterface.
        :type: str
        """

        self._middlename = middlename

    @property
    def prefix(self):
        """
        Gets the prefix of this CustomerDataCustomerInterface.
        Prefix

        :return: The prefix of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this CustomerDataCustomerInterface.
        Prefix

        :param prefix: The prefix of this CustomerDataCustomerInterface.
        :type: str
        """

        self._prefix = prefix

    @property
    def suffix(self):
        """
        Gets the suffix of this CustomerDataCustomerInterface.
        Suffix

        :return: The suffix of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._suffix

    @suffix.setter
    def suffix(self, suffix):
        """
        Sets the suffix of this CustomerDataCustomerInterface.
        Suffix

        :param suffix: The suffix of this CustomerDataCustomerInterface.
        :type: str
        """

        self._suffix = suffix

    @property
    def gender(self):
        """
        Gets the gender of this CustomerDataCustomerInterface.
        Gender

        :return: The gender of this CustomerDataCustomerInterface.
        :rtype: int
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this CustomerDataCustomerInterface.
        Gender

        :param gender: The gender of this CustomerDataCustomerInterface.
        :type: int
        """

        self._gender = gender

    @property
    def store_id(self):
        """
        Gets the store_id of this CustomerDataCustomerInterface.
        Store id

        :return: The store_id of this CustomerDataCustomerInterface.
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """
        Sets the store_id of this CustomerDataCustomerInterface.
        Store id

        :param store_id: The store_id of this CustomerDataCustomerInterface.
        :type: int
        """

        self._store_id = store_id

    @property
    def taxvat(self):
        """
        Gets the taxvat of this CustomerDataCustomerInterface.
        Tax Vat

        :return: The taxvat of this CustomerDataCustomerInterface.
        :rtype: str
        """
        return self._taxvat

    @taxvat.setter
    def taxvat(self, taxvat):
        """
        Sets the taxvat of this CustomerDataCustomerInterface.
        Tax Vat

        :param taxvat: The taxvat of this CustomerDataCustomerInterface.
        :type: str
        """

        self._taxvat = taxvat

    @property
    def website_id(self):
        """
        Gets the website_id of this CustomerDataCustomerInterface.
        Website id

        :return: The website_id of this CustomerDataCustomerInterface.
        :rtype: int
        """
        return self._website_id

    @website_id.setter
    def website_id(self, website_id):
        """
        Sets the website_id of this CustomerDataCustomerInterface.
        Website id

        :param website_id: The website_id of this CustomerDataCustomerInterface.
        :type: int
        """

        self._website_id = website_id

    @property
    def addresses(self):
        """
        Gets the addresses of this CustomerDataCustomerInterface.
        Customer addresses.

        :return: The addresses of this CustomerDataCustomerInterface.
        :rtype: list[CustomerDataAddressInterface]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """
        Sets the addresses of this CustomerDataCustomerInterface.
        Customer addresses.

        :param addresses: The addresses of this CustomerDataCustomerInterface.
        :type: list[CustomerDataAddressInterface]
        """

        self._addresses = addresses

    @property
    def disable_auto_group_change(self):
        """
        Gets the disable_auto_group_change of this CustomerDataCustomerInterface.
        Disable auto group change flag.

        :return: The disable_auto_group_change of this CustomerDataCustomerInterface.
        :rtype: int
        """
        return self._disable_auto_group_change

    @disable_auto_group_change.setter
    def disable_auto_group_change(self, disable_auto_group_change):
        """
        Sets the disable_auto_group_change of this CustomerDataCustomerInterface.
        Disable auto group change flag.

        :param disable_auto_group_change: The disable_auto_group_change of this CustomerDataCustomerInterface.
        :type: int
        """

        self._disable_auto_group_change = disable_auto_group_change

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this CustomerDataCustomerInterface.

        :return: The extension_attributes of this CustomerDataCustomerInterface.
        :rtype: CustomerDataCustomerExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this CustomerDataCustomerInterface.

        :param extension_attributes: The extension_attributes of this CustomerDataCustomerInterface.
        :type: CustomerDataCustomerExtensionInterface
        """

        self._extension_attributes = extension_attributes

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this CustomerDataCustomerInterface.
        Custom attributes values.

        :return: The custom_attributes of this CustomerDataCustomerInterface.
        :rtype: list[FrameworkAttributeInterface]
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this CustomerDataCustomerInterface.
        Custom attributes values.

        :param custom_attributes: The custom_attributes of this CustomerDataCustomerInterface.
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
        if not isinstance(other, CustomerDataCustomerInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other