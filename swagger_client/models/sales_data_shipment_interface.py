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


class SalesDataShipmentInterface(object):
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
        'billing_address_id': 'int',
        'created_at': 'str',
        'customer_id': 'int',
        'email_sent': 'int',
        'entity_id': 'int',
        'increment_id': 'str',
        'order_id': 'int',
        'packages': 'list[SalesDataShipmentPackageInterface]',
        'shipment_status': 'int',
        'shipping_address_id': 'int',
        'shipping_label': 'str',
        'store_id': 'int',
        'total_qty': 'float',
        'total_weight': 'float',
        'updated_at': 'str',
        'items': 'list[SalesDataShipmentItemInterface]',
        'tracks': 'list[SalesDataShipmentTrackInterface]',
        'comments': 'list[SalesDataShipmentCommentInterface]',
        'extension_attributes': 'SalesDataShipmentExtensionInterface'
    }

    attribute_map = {
        'billing_address_id': 'billing_address_id',
        'created_at': 'created_at',
        'customer_id': 'customer_id',
        'email_sent': 'email_sent',
        'entity_id': 'entity_id',
        'increment_id': 'increment_id',
        'order_id': 'order_id',
        'packages': 'packages',
        'shipment_status': 'shipment_status',
        'shipping_address_id': 'shipping_address_id',
        'shipping_label': 'shipping_label',
        'store_id': 'store_id',
        'total_qty': 'total_qty',
        'total_weight': 'total_weight',
        'updated_at': 'updated_at',
        'items': 'items',
        'tracks': 'tracks',
        'comments': 'comments',
        'extension_attributes': 'extension_attributes'
    }

    def __init__(self, billing_address_id=None, created_at=None, customer_id=None, email_sent=None, entity_id=None, increment_id=None, order_id=None, packages=None, shipment_status=None, shipping_address_id=None, shipping_label=None, store_id=None, total_qty=None, total_weight=None, updated_at=None, items=None, tracks=None, comments=None, extension_attributes=None):
        """
        SalesDataShipmentInterface - a model defined in Swagger
        """

        self._billing_address_id = None
        self._created_at = None
        self._customer_id = None
        self._email_sent = None
        self._entity_id = None
        self._increment_id = None
        self._order_id = None
        self._packages = None
        self._shipment_status = None
        self._shipping_address_id = None
        self._shipping_label = None
        self._store_id = None
        self._total_qty = None
        self._total_weight = None
        self._updated_at = None
        self._items = None
        self._tracks = None
        self._comments = None
        self._extension_attributes = None

        if billing_address_id is not None:
          self.billing_address_id = billing_address_id
        if created_at is not None:
          self.created_at = created_at
        if customer_id is not None:
          self.customer_id = customer_id
        if email_sent is not None:
          self.email_sent = email_sent
        if entity_id is not None:
          self.entity_id = entity_id
        if increment_id is not None:
          self.increment_id = increment_id
        self.order_id = order_id
        if packages is not None:
          self.packages = packages
        if shipment_status is not None:
          self.shipment_status = shipment_status
        if shipping_address_id is not None:
          self.shipping_address_id = shipping_address_id
        if shipping_label is not None:
          self.shipping_label = shipping_label
        if store_id is not None:
          self.store_id = store_id
        if total_qty is not None:
          self.total_qty = total_qty
        if total_weight is not None:
          self.total_weight = total_weight
        if updated_at is not None:
          self.updated_at = updated_at
        self.items = items
        self.tracks = tracks
        self.comments = comments
        if extension_attributes is not None:
          self.extension_attributes = extension_attributes

    @property
    def billing_address_id(self):
        """
        Gets the billing_address_id of this SalesDataShipmentInterface.
        Billing address ID.

        :return: The billing_address_id of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._billing_address_id

    @billing_address_id.setter
    def billing_address_id(self, billing_address_id):
        """
        Sets the billing_address_id of this SalesDataShipmentInterface.
        Billing address ID.

        :param billing_address_id: The billing_address_id of this SalesDataShipmentInterface.
        :type: int
        """

        self._billing_address_id = billing_address_id

    @property
    def created_at(self):
        """
        Gets the created_at of this SalesDataShipmentInterface.
        Created-at timestamp.

        :return: The created_at of this SalesDataShipmentInterface.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this SalesDataShipmentInterface.
        Created-at timestamp.

        :param created_at: The created_at of this SalesDataShipmentInterface.
        :type: str
        """

        self._created_at = created_at

    @property
    def customer_id(self):
        """
        Gets the customer_id of this SalesDataShipmentInterface.
        Customer ID.

        :return: The customer_id of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this SalesDataShipmentInterface.
        Customer ID.

        :param customer_id: The customer_id of this SalesDataShipmentInterface.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def email_sent(self):
        """
        Gets the email_sent of this SalesDataShipmentInterface.
        Email-sent flag value.

        :return: The email_sent of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._email_sent

    @email_sent.setter
    def email_sent(self, email_sent):
        """
        Sets the email_sent of this SalesDataShipmentInterface.
        Email-sent flag value.

        :param email_sent: The email_sent of this SalesDataShipmentInterface.
        :type: int
        """

        self._email_sent = email_sent

    @property
    def entity_id(self):
        """
        Gets the entity_id of this SalesDataShipmentInterface.
        Shipment ID.

        :return: The entity_id of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this SalesDataShipmentInterface.
        Shipment ID.

        :param entity_id: The entity_id of this SalesDataShipmentInterface.
        :type: int
        """

        self._entity_id = entity_id

    @property
    def increment_id(self):
        """
        Gets the increment_id of this SalesDataShipmentInterface.
        Increment ID.

        :return: The increment_id of this SalesDataShipmentInterface.
        :rtype: str
        """
        return self._increment_id

    @increment_id.setter
    def increment_id(self, increment_id):
        """
        Sets the increment_id of this SalesDataShipmentInterface.
        Increment ID.

        :param increment_id: The increment_id of this SalesDataShipmentInterface.
        :type: str
        """

        self._increment_id = increment_id

    @property
    def order_id(self):
        """
        Gets the order_id of this SalesDataShipmentInterface.
        Order ID.

        :return: The order_id of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """
        Sets the order_id of this SalesDataShipmentInterface.
        Order ID.

        :param order_id: The order_id of this SalesDataShipmentInterface.
        :type: int
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")

        self._order_id = order_id

    @property
    def packages(self):
        """
        Gets the packages of this SalesDataShipmentInterface.
        Array of packages, if any. Otherwise, null.

        :return: The packages of this SalesDataShipmentInterface.
        :rtype: list[SalesDataShipmentPackageInterface]
        """
        return self._packages

    @packages.setter
    def packages(self, packages):
        """
        Sets the packages of this SalesDataShipmentInterface.
        Array of packages, if any. Otherwise, null.

        :param packages: The packages of this SalesDataShipmentInterface.
        :type: list[SalesDataShipmentPackageInterface]
        """

        self._packages = packages

    @property
    def shipment_status(self):
        """
        Gets the shipment_status of this SalesDataShipmentInterface.
        Shipment status.

        :return: The shipment_status of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._shipment_status

    @shipment_status.setter
    def shipment_status(self, shipment_status):
        """
        Sets the shipment_status of this SalesDataShipmentInterface.
        Shipment status.

        :param shipment_status: The shipment_status of this SalesDataShipmentInterface.
        :type: int
        """

        self._shipment_status = shipment_status

    @property
    def shipping_address_id(self):
        """
        Gets the shipping_address_id of this SalesDataShipmentInterface.
        Shipping address ID.

        :return: The shipping_address_id of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._shipping_address_id

    @shipping_address_id.setter
    def shipping_address_id(self, shipping_address_id):
        """
        Sets the shipping_address_id of this SalesDataShipmentInterface.
        Shipping address ID.

        :param shipping_address_id: The shipping_address_id of this SalesDataShipmentInterface.
        :type: int
        """

        self._shipping_address_id = shipping_address_id

    @property
    def shipping_label(self):
        """
        Gets the shipping_label of this SalesDataShipmentInterface.
        Shipping label.

        :return: The shipping_label of this SalesDataShipmentInterface.
        :rtype: str
        """
        return self._shipping_label

    @shipping_label.setter
    def shipping_label(self, shipping_label):
        """
        Sets the shipping_label of this SalesDataShipmentInterface.
        Shipping label.

        :param shipping_label: The shipping_label of this SalesDataShipmentInterface.
        :type: str
        """

        self._shipping_label = shipping_label

    @property
    def store_id(self):
        """
        Gets the store_id of this SalesDataShipmentInterface.
        Store ID.

        :return: The store_id of this SalesDataShipmentInterface.
        :rtype: int
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """
        Sets the store_id of this SalesDataShipmentInterface.
        Store ID.

        :param store_id: The store_id of this SalesDataShipmentInterface.
        :type: int
        """

        self._store_id = store_id

    @property
    def total_qty(self):
        """
        Gets the total_qty of this SalesDataShipmentInterface.
        Total quantity.

        :return: The total_qty of this SalesDataShipmentInterface.
        :rtype: float
        """
        return self._total_qty

    @total_qty.setter
    def total_qty(self, total_qty):
        """
        Sets the total_qty of this SalesDataShipmentInterface.
        Total quantity.

        :param total_qty: The total_qty of this SalesDataShipmentInterface.
        :type: float
        """

        self._total_qty = total_qty

    @property
    def total_weight(self):
        """
        Gets the total_weight of this SalesDataShipmentInterface.
        Total weight.

        :return: The total_weight of this SalesDataShipmentInterface.
        :rtype: float
        """
        return self._total_weight

    @total_weight.setter
    def total_weight(self, total_weight):
        """
        Sets the total_weight of this SalesDataShipmentInterface.
        Total weight.

        :param total_weight: The total_weight of this SalesDataShipmentInterface.
        :type: float
        """

        self._total_weight = total_weight

    @property
    def updated_at(self):
        """
        Gets the updated_at of this SalesDataShipmentInterface.
        Updated-at timestamp.

        :return: The updated_at of this SalesDataShipmentInterface.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this SalesDataShipmentInterface.
        Updated-at timestamp.

        :param updated_at: The updated_at of this SalesDataShipmentInterface.
        :type: str
        """

        self._updated_at = updated_at

    @property
    def items(self):
        """
        Gets the items of this SalesDataShipmentInterface.
        Array of items.

        :return: The items of this SalesDataShipmentInterface.
        :rtype: list[SalesDataShipmentItemInterface]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this SalesDataShipmentInterface.
        Array of items.

        :param items: The items of this SalesDataShipmentInterface.
        :type: list[SalesDataShipmentItemInterface]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items

    @property
    def tracks(self):
        """
        Gets the tracks of this SalesDataShipmentInterface.
        Array of tracks.

        :return: The tracks of this SalesDataShipmentInterface.
        :rtype: list[SalesDataShipmentTrackInterface]
        """
        return self._tracks

    @tracks.setter
    def tracks(self, tracks):
        """
        Sets the tracks of this SalesDataShipmentInterface.
        Array of tracks.

        :param tracks: The tracks of this SalesDataShipmentInterface.
        :type: list[SalesDataShipmentTrackInterface]
        """
        if tracks is None:
            raise ValueError("Invalid value for `tracks`, must not be `None`")

        self._tracks = tracks

    @property
    def comments(self):
        """
        Gets the comments of this SalesDataShipmentInterface.
        Array of comments.

        :return: The comments of this SalesDataShipmentInterface.
        :rtype: list[SalesDataShipmentCommentInterface]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this SalesDataShipmentInterface.
        Array of comments.

        :param comments: The comments of this SalesDataShipmentInterface.
        :type: list[SalesDataShipmentCommentInterface]
        """
        if comments is None:
            raise ValueError("Invalid value for `comments`, must not be `None`")

        self._comments = comments

    @property
    def extension_attributes(self):
        """
        Gets the extension_attributes of this SalesDataShipmentInterface.

        :return: The extension_attributes of this SalesDataShipmentInterface.
        :rtype: SalesDataShipmentExtensionInterface
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """
        Sets the extension_attributes of this SalesDataShipmentInterface.

        :param extension_attributes: The extension_attributes of this SalesDataShipmentInterface.
        :type: SalesDataShipmentExtensionInterface
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
        if not isinstance(other, SalesDataShipmentInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
