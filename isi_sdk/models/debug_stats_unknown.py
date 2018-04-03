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


class DebugStatsUnknown(object):
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
        'calls': 'int',
        'errors': 'int',
        'time': 'float'
    }

    attribute_map = {
        'calls': 'calls',
        'errors': 'errors',
        'time': 'time'
    }

    def __init__(self, calls=None, errors=None, time=None):  # noqa: E501
        """DebugStatsUnknown - a model defined in Swagger"""  # noqa: E501

        self._calls = None
        self._errors = None
        self._time = None
        self.discriminator = None

        if calls is not None:
            self.calls = calls
        if errors is not None:
            self.errors = errors
        if time is not None:
            self.time = time

    @property
    def calls(self):
        """Gets the calls of this DebugStatsUnknown.  # noqa: E501

        The number of calls.  # noqa: E501

        :return: The calls of this DebugStatsUnknown.  # noqa: E501
        :rtype: int
        """
        return self._calls

    @calls.setter
    def calls(self, calls):
        """Sets the calls of this DebugStatsUnknown.

        The number of calls.  # noqa: E501

        :param calls: The calls of this DebugStatsUnknown.  # noqa: E501
        :type: int
        """

        self._calls = calls

    @property
    def errors(self):
        """Gets the errors of this DebugStatsUnknown.  # noqa: E501

        The number of errors.  # noqa: E501

        :return: The errors of this DebugStatsUnknown.  # noqa: E501
        :rtype: int
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this DebugStatsUnknown.

        The number of errors.  # noqa: E501

        :param errors: The errors of this DebugStatsUnknown.  # noqa: E501
        :type: int
        """

        self._errors = errors

    @property
    def time(self):
        """Gets the time of this DebugStatsUnknown.  # noqa: E501

        The total amount of time spent in this method.  # noqa: E501

        :return: The time of this DebugStatsUnknown.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this DebugStatsUnknown.

        The total amount of time spent in this method.  # noqa: E501

        :param time: The time of this DebugStatsUnknown.  # noqa: E501
        :type: float
        """

        self._time = time

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
        if not isinstance(other, DebugStatsUnknown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
