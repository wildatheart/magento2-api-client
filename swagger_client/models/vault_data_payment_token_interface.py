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


class VaultDataPaymentTokenInterface(object):
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
        'entity_id': 'int',
        'customer_id': 'int',
        'public_hash': 'str',
        'payment_method_code': 'str',
        'type': 'str',
        'created_at': 'str',
        'expires_at': 'str',
        'gateway_token': 'str',
        'token_details': 'str',
        'is_active': 'bool',
        'is_visible': 'bool'
    }

    attribute_map = {
        'entity_id': 'entity_id',
        'customer_id': 'customer_id',
        'public_hash': 'public_hash',
        'payment_method_code': 'payment_method_code',
        'type': 'type',
        'created_at': 'created_at',
        'expires_at': 'expires_at',
        'gateway_token': 'gateway_token',
        'token_details': 'token_details',
        'is_active': 'is_active',
        'is_visible': 'is_visible'
    }

    def __init__(self, entity_id=None, customer_id=None, public_hash=None, payment_method_code=None, type=None, created_at=None, expires_at=None, gateway_token=None, token_details=None, is_active=None, is_visible=None):
        """
        VaultDataPaymentTokenInterface - a model defined in Swagger
        """

        self._entity_id = None
        self._customer_id = None
        self._public_hash = None
        self._payment_method_code = None
        self._type = None
        self._created_at = None
        self._expires_at = None
        self._gateway_token = None
        self._token_details = None
        self._is_active = None
        self._is_visible = None

        if entity_id is not None:
          self.entity_id = entity_id
        if customer_id is not None:
          self.customer_id = customer_id
        self.public_hash = public_hash
        self.payment_method_code = payment_method_code
        self.type = type
        if created_at is not None:
          self.created_at = created_at
        if expires_at is not None:
          self.expires_at = expires_at
        self.gateway_token = gateway_token
        self.token_details = token_details
        self.is_active = is_active
        self.is_visible = is_visible

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VaultDataPaymentTokenInterface.
        Entity ID.

        :return: The entity_id of this VaultDataPaymentTokenInterface.
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VaultDataPaymentTokenInterface.
        Entity ID.

        :param entity_id: The entity_id of this VaultDataPaymentTokenInterface.
        :type: int
        """

        self._entity_id = entity_id

    @property
    def customer_id(self):
        """
        Gets the customer_id of this VaultDataPaymentTokenInterface.
        Customer ID.

        :return: The customer_id of this VaultDataPaymentTokenInterface.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this VaultDataPaymentTokenInterface.
        Customer ID.

        :param customer_id: The customer_id of this VaultDataPaymentTokenInterface.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def public_hash(self):
        """
        Gets the public_hash of this VaultDataPaymentTokenInterface.
        Public hash

        :return: The public_hash of this VaultDataPaymentTokenInterface.
        :rtype: str
        """
        return self._public_hash

    @public_hash.setter
    def public_hash(self, public_hash):
        """
        Sets the public_hash of this VaultDataPaymentTokenInterface.
        Public hash

        :param public_hash: The public_hash of this VaultDataPaymentTokenInterface.
        :type: str
        """
        if public_hash is None:
            raise ValueError("Invalid value for `public_hash`, must not be `None`")

        self._public_hash = public_hash

    @property
    def payment_method_code(self):
        """
        Gets the payment_method_code of this VaultDataPaymentTokenInterface.
        Payment method code

        :return: The payment_method_code of this VaultDataPaymentTokenInterface.
        :rtype: str
        """
        return self._payment_method_code

    @payment_method_code.setter
    def payment_method_code(self, payment_method_code):
        """
        Sets the payment_method_code of this VaultDataPaymentTokenInterface.
        Payment method code

        :param payment_method_code: The payment_method_code of this VaultDataPaymentTokenInterface.
        :type: str
        """
        if payment_method_code is None:
            raise ValueError("Invalid value for `payment_method_code`, must not be `None`")

        self._payment_method_code = payment_method_code

    @property
    def type(self):
        """
        Gets the type of this VaultDataPaymentTokenInterface.
        Type

        :return: The type of this VaultDataPaymentTokenInterface.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this VaultDataPaymentTokenInterface.
        Type

        :param type: The type of this VaultDataPaymentTokenInterface.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def created_at(self):
        """
        Gets the created_at of this VaultDataPaymentTokenInterface.
        Token creation timestamp

        :return: The created_at of this VaultDataPaymentTokenInterface.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this VaultDataPaymentTokenInterface.
        Token creation timestamp

        :param created_at: The created_at of this VaultDataPaymentTokenInterface.
        :type: str
        """

        self._created_at = created_at

    @property
    def expires_at(self):
        """
        Gets the expires_at of this VaultDataPaymentTokenInterface.
        Token expiration timestamp

        :return: The expires_at of this VaultDataPaymentTokenInterface.
        :rtype: str
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """
        Sets the expires_at of this VaultDataPaymentTokenInterface.
        Token expiration timestamp

        :param expires_at: The expires_at of this VaultDataPaymentTokenInterface.
        :type: str
        """

        self._expires_at = expires_at

    @property
    def gateway_token(self):
        """
        Gets the gateway_token of this VaultDataPaymentTokenInterface.
        Gateway token ID

        :return: The gateway_token of this VaultDataPaymentTokenInterface.
        :rtype: str
        """
        return self._gateway_token

    @gateway_token.setter
    def gateway_token(self, gateway_token):
        """
        Sets the gateway_token of this VaultDataPaymentTokenInterface.
        Gateway token ID

        :param gateway_token: The gateway_token of this VaultDataPaymentTokenInterface.
        :type: str
        """
        if gateway_token is None:
            raise ValueError("Invalid value for `gateway_token`, must not be `None`")

        self._gateway_token = gateway_token

    @property
    def token_details(self):
        """
        Gets the token_details of this VaultDataPaymentTokenInterface.
        Token details

        :return: The token_details of this VaultDataPaymentTokenInterface.
        :rtype: str
        """
        return self._token_details

    @token_details.setter
    def token_details(self, token_details):
        """
        Sets the token_details of this VaultDataPaymentTokenInterface.
        Token details

        :param token_details: The token_details of this VaultDataPaymentTokenInterface.
        :type: str
        """
        if token_details is None:
            raise ValueError("Invalid value for `token_details`, must not be `None`")

        self._token_details = token_details

    @property
    def is_active(self):
        """
        Gets the is_active of this VaultDataPaymentTokenInterface.
        Is active.

        :return: The is_active of this VaultDataPaymentTokenInterface.
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this VaultDataPaymentTokenInterface.
        Is active.

        :param is_active: The is_active of this VaultDataPaymentTokenInterface.
        :type: bool
        """
        if is_active is None:
            raise ValueError("Invalid value for `is_active`, must not be `None`")

        self._is_active = is_active

    @property
    def is_visible(self):
        """
        Gets the is_visible of this VaultDataPaymentTokenInterface.
        Is visible.

        :return: The is_visible of this VaultDataPaymentTokenInterface.
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this VaultDataPaymentTokenInterface.
        Is visible.

        :param is_visible: The is_visible of this VaultDataPaymentTokenInterface.
        :type: bool
        """
        if is_visible is None:
            raise ValueError("Invalid value for `is_visible`, must not be `None`")

        self._is_visible = is_visible

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
        if not isinstance(other, VaultDataPaymentTokenInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other