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


class WormDomain(object):
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
        'autocommit_offset': 'int',
        'default_retention': 'str',
        'max_retention': 'str',
        'min_retention': 'str',
        'override_date': 'int',
        'privileged_delete': 'str',
        'type': 'str'
    }

    attribute_map = {
        'autocommit_offset': 'autocommit_offset',
        'default_retention': 'default_retention',
        'max_retention': 'max_retention',
        'min_retention': 'min_retention',
        'override_date': 'override_date',
        'privileged_delete': 'privileged_delete',
        'type': 'type'
    }

    def __init__(self, autocommit_offset=None, default_retention=None, max_retention=None, min_retention=None, override_date=None, privileged_delete=None, type=None):  # noqa: E501
        """WormDomain - a model defined in Swagger"""  # noqa: E501

        self._autocommit_offset = None
        self._default_retention = None
        self._max_retention = None
        self._min_retention = None
        self._override_date = None
        self._privileged_delete = None
        self._type = None
        self.discriminator = None

        if autocommit_offset is not None:
            self.autocommit_offset = autocommit_offset
        if default_retention is not None:
            self.default_retention = default_retention
        if max_retention is not None:
            self.max_retention = max_retention
        if min_retention is not None:
            self.min_retention = min_retention
        if override_date is not None:
            self.override_date = override_date
        if privileged_delete is not None:
            self.privileged_delete = privileged_delete
        if type is not None:
            self.type = type

    @property
    def autocommit_offset(self):
        """Gets the autocommit_offset of this WormDomain.  # noqa: E501

        Specifies the autocommit time period for the domain in seconds.  After a file is in the domain without being modified for the specified time period, the file is automatically committed. If this parameter is set to null, there is no autocommit time, and files must be committed manually.  # noqa: E501

        :return: The autocommit_offset of this WormDomain.  # noqa: E501
        :rtype: int
        """
        return self._autocommit_offset

    @autocommit_offset.setter
    def autocommit_offset(self, autocommit_offset):
        """Sets the autocommit_offset of this WormDomain.

        Specifies the autocommit time period for the domain in seconds.  After a file is in the domain without being modified for the specified time period, the file is automatically committed. If this parameter is set to null, there is no autocommit time, and files must be committed manually.  # noqa: E501

        :param autocommit_offset: The autocommit_offset of this WormDomain.  # noqa: E501
        :type: int
        """
        if autocommit_offset is not None and autocommit_offset < 0:  # noqa: E501
            raise ValueError("Invalid value for `autocommit_offset`, must be a value greater than or equal to `0`")  # noqa: E501

        self._autocommit_offset = autocommit_offset

    @property
    def default_retention(self):
        """Gets the default_retention of this WormDomain.  # noqa: E501


        :return: The default_retention of this WormDomain.  # noqa: E501
        :rtype: str
        """
        return self._default_retention

    @default_retention.setter
    def default_retention(self, default_retention):
        """Sets the default_retention of this WormDomain.


        :param default_retention: The default_retention of this WormDomain.  # noqa: E501
        :type: str
        """

        self._default_retention = default_retention

    @property
    def max_retention(self):
        """Gets the max_retention of this WormDomain.  # noqa: E501


        :return: The max_retention of this WormDomain.  # noqa: E501
        :rtype: str
        """
        return self._max_retention

    @max_retention.setter
    def max_retention(self, max_retention):
        """Sets the max_retention of this WormDomain.


        :param max_retention: The max_retention of this WormDomain.  # noqa: E501
        :type: str
        """

        self._max_retention = max_retention

    @property
    def min_retention(self):
        """Gets the min_retention of this WormDomain.  # noqa: E501


        :return: The min_retention of this WormDomain.  # noqa: E501
        :rtype: str
        """
        return self._min_retention

    @min_retention.setter
    def min_retention(self, min_retention):
        """Sets the min_retention of this WormDomain.


        :param min_retention: The min_retention of this WormDomain.  # noqa: E501
        :type: str
        """

        self._min_retention = min_retention

    @property
    def override_date(self):
        """Gets the override_date of this WormDomain.  # noqa: E501

        Specifies the override retention date for the domain. If this date is later than the retention date for any committed file, the file will remain protected until the override retention date.  # noqa: E501

        :return: The override_date of this WormDomain.  # noqa: E501
        :rtype: int
        """
        return self._override_date

    @override_date.setter
    def override_date(self, override_date):
        """Sets the override_date of this WormDomain.

        Specifies the override retention date for the domain. If this date is later than the retention date for any committed file, the file will remain protected until the override retention date.  # noqa: E501

        :param override_date: The override_date of this WormDomain.  # noqa: E501
        :type: int
        """
        if override_date is not None and override_date < 0:  # noqa: E501
            raise ValueError("Invalid value for `override_date`, must be a value greater than or equal to `0`")  # noqa: E501

        self._override_date = override_date

    @property
    def privileged_delete(self):
        """Gets the privileged_delete of this WormDomain.  # noqa: E501

        When this value is set to 'on', files in this domain can be deleted through the privileged delete feature. If this value is set to 'disabled', privileged file deletes are permanently disabled and cannot be turned on again.  # noqa: E501

        :return: The privileged_delete of this WormDomain.  # noqa: E501
        :rtype: str
        """
        return self._privileged_delete

    @privileged_delete.setter
    def privileged_delete(self, privileged_delete):
        """Sets the privileged_delete of this WormDomain.

        When this value is set to 'on', files in this domain can be deleted through the privileged delete feature. If this value is set to 'disabled', privileged file deletes are permanently disabled and cannot be turned on again.  # noqa: E501

        :param privileged_delete: The privileged_delete of this WormDomain.  # noqa: E501
        :type: str
        """
        allowed_values = ["on", "off", "disabled"]  # noqa: E501
        if privileged_delete not in allowed_values:
            raise ValueError(
                "Invalid value for `privileged_delete` ({0}), must be one of {1}"  # noqa: E501
                .format(privileged_delete, allowed_values)
            )

        self._privileged_delete = privileged_delete

    @property
    def type(self):
        """Gets the type of this WormDomain.  # noqa: E501

        Specifies whether the domain is an enterprise domain or a compliance domain. Compliance domains can not be created on enterprise clusters. Enterprise and compliance domains can be created on compliance clusters.  # noqa: E501

        :return: The type of this WormDomain.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WormDomain.

        Specifies whether the domain is an enterprise domain or a compliance domain. Compliance domains can not be created on enterprise clusters. Enterprise and compliance domains can be created on compliance clusters.  # noqa: E501

        :param type: The type of this WormDomain.  # noqa: E501
        :type: str
        """
        allowed_values = ["enterprise", "compliance"]  # noqa: E501
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
        if not isinstance(other, WormDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
