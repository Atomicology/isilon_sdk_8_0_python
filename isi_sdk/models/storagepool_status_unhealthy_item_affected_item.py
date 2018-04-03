# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8.0
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from isi_sdk_8_0.models.storagepool_status_unprovisioned_item import StoragepoolStatusUnprovisionedItem  # noqa: F401,E501


class StoragepoolStatusUnhealthyItemAffectedItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'device': 'StoragepoolStatusUnprovisionedItem',
        'down': 'bool',
        'restriping': 'bool',
        'smartfailed': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'device': 'device',
        'down': 'down',
        'restriping': 'restriping',
        'smartfailed': 'smartfailed',
        'type': 'type'
    }

    def __init__(self, device=None, down=None, restriping=None, smartfailed=None, type=None):  # noqa: E501
        """StoragepoolStatusUnhealthyItemAffectedItem - a model defined in Swagger"""  # noqa: E501

        self._device = None
        self._down = None
        self._restriping = None
        self._smartfailed = None
        self._type = None
        self.discriminator = None

        if device is not None:
            self.device = device
        self.down = down
        self.restriping = restriping
        self.smartfailed = smartfailed
        self.type = type

    @property
    def device(self):
        """Gets the device of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501

          # noqa: E501

        :return: The device of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :rtype: StoragepoolStatusUnprovisionedItem
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this StoragepoolStatusUnhealthyItemAffectedItem.

          # noqa: E501

        :param device: The device of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :type: StoragepoolStatusUnprovisionedItem
        """

        self._device = device

    @property
    def down(self):
        """Gets the down of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501

        Whether or not the device is currently down.  # noqa: E501

        :return: The down of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :rtype: bool
        """
        return self._down

    @down.setter
    def down(self, down):
        """Sets the down of this StoragepoolStatusUnhealthyItemAffectedItem.

        Whether or not the device is currently down.  # noqa: E501

        :param down: The down of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :type: bool
        """
        if down is None:
            raise ValueError("Invalid value for `down`, must not be `None`")  # noqa: E501

        self._down = down

    @property
    def restriping(self):
        """Gets the restriping of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501

        Whether or not the device is currently being repaired.  # noqa: E501

        :return: The restriping of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :rtype: bool
        """
        return self._restriping

    @restriping.setter
    def restriping(self, restriping):
        """Sets the restriping of this StoragepoolStatusUnhealthyItemAffectedItem.

        Whether or not the device is currently being repaired.  # noqa: E501

        :param restriping: The restriping of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :type: bool
        """
        if restriping is None:
            raise ValueError("Invalid value for `restriping`, must not be `None`")  # noqa: E501

        self._restriping = restriping

    @property
    def smartfailed(self):
        """Gets the smartfailed of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501

        Whether or not the device is currently smartfailed.  # noqa: E501

        :return: The smartfailed of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :rtype: bool
        """
        return self._smartfailed

    @smartfailed.setter
    def smartfailed(self, smartfailed):
        """Sets the smartfailed of this StoragepoolStatusUnhealthyItemAffectedItem.

        Whether or not the device is currently smartfailed.  # noqa: E501

        :param smartfailed: The smartfailed of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :type: bool
        """
        if smartfailed is None:
            raise ValueError("Invalid value for `smartfailed`, must not be `None`")  # noqa: E501

        self._smartfailed = smartfailed

    @property
    def type(self):
        """Gets the type of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501

        The type of affected device.  # noqa: E501

        :return: The type of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StoragepoolStatusUnhealthyItemAffectedItem.

        The type of affected device.  # noqa: E501

        :param type: The type of this StoragepoolStatusUnhealthyItemAffectedItem.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["node", "drive"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StoragepoolStatusUnhealthyItemAffectedItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
