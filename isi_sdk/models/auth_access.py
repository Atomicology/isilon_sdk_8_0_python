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

from isi_sdk_8_0.models.auth_access_access_item import AuthAccessAccessItem  # noqa: F401,E501


class AuthAccess(object):
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
        'access': 'list[AuthAccessAccessItem]'
    }

    attribute_map = {
        'access': 'access'
    }

    def __init__(self, access=None):  # noqa: E501
        """AuthAccess - a model defined in Swagger"""  # noqa: E501

        self._access = None
        self.discriminator = None

        if access is not None:
            self.access = access

    @property
    def access(self):
        """Gets the access of this AuthAccess.  # noqa: E501


        :return: The access of this AuthAccess.  # noqa: E501
        :rtype: list[AuthAccessAccessItem]
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this AuthAccess.


        :param access: The access of this AuthAccess.  # noqa: E501
        :type: list[AuthAccessAccessItem]
        """

        self._access = access

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
        if not isinstance(other, AuthAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
