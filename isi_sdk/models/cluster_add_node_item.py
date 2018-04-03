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


class ClusterAddNodeItem(object):
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
        'allow_down': 'bool',
        'serial_number': 'str',
        'skip_hardware_version_check': 'bool'
    }

    attribute_map = {
        'allow_down': 'allow_down',
        'serial_number': 'serial_number',
        'skip_hardware_version_check': 'skip_hardware_version_check'
    }

    def __init__(self, allow_down=None, serial_number=None, skip_hardware_version_check=None):  # noqa: E501
        """ClusterAddNodeItem - a model defined in Swagger"""  # noqa: E501

        self._allow_down = None
        self._serial_number = None
        self._skip_hardware_version_check = None
        self.discriminator = None

        if allow_down is not None:
            self.allow_down = allow_down
        self.serial_number = serial_number
        if skip_hardware_version_check is not None:
            self.skip_hardware_version_check = skip_hardware_version_check

    @property
    def allow_down(self):
        """Gets the allow_down of this ClusterAddNodeItem.  # noqa: E501

        Allow down nodes (Default false).  # noqa: E501

        :return: The allow_down of this ClusterAddNodeItem.  # noqa: E501
        :rtype: bool
        """
        return self._allow_down

    @allow_down.setter
    def allow_down(self, allow_down):
        """Sets the allow_down of this ClusterAddNodeItem.

        Allow down nodes (Default false).  # noqa: E501

        :param allow_down: The allow_down of this ClusterAddNodeItem.  # noqa: E501
        :type: bool
        """

        self._allow_down = allow_down

    @property
    def serial_number(self):
        """Gets the serial_number of this ClusterAddNodeItem.  # noqa: E501

        Serial number of this node.  # noqa: E501

        :return: The serial_number of this ClusterAddNodeItem.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this ClusterAddNodeItem.

        Serial number of this node.  # noqa: E501

        :param serial_number: The serial_number of this ClusterAddNodeItem.  # noqa: E501
        :type: str
        """
        if serial_number is None:
            raise ValueError("Invalid value for `serial_number`, must not be `None`")  # noqa: E501

        self._serial_number = serial_number

    @property
    def skip_hardware_version_check(self):
        """Gets the skip_hardware_version_check of this ClusterAddNodeItem.  # noqa: E501

        Bypass hardware version checks (Default false).  # noqa: E501

        :return: The skip_hardware_version_check of this ClusterAddNodeItem.  # noqa: E501
        :rtype: bool
        """
        return self._skip_hardware_version_check

    @skip_hardware_version_check.setter
    def skip_hardware_version_check(self, skip_hardware_version_check):
        """Sets the skip_hardware_version_check of this ClusterAddNodeItem.

        Bypass hardware version checks (Default false).  # noqa: E501

        :param skip_hardware_version_check: The skip_hardware_version_check of this ClusterAddNodeItem.  # noqa: E501
        :type: bool
        """

        self._skip_hardware_version_check = skip_hardware_version_check

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
        if not isinstance(other, ClusterAddNodeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
