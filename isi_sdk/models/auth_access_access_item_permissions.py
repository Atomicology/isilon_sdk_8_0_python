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


class AuthAccessAccessItemPermissions(object):
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
        'dacl': 'str',
        'delete_child': 'str',
        'expected': 'str',
        'ownership': 'str',
        'sticky': 'str'
    }

    attribute_map = {
        'dacl': 'dacl',
        'delete_child': 'delete_child',
        'expected': 'expected',
        'ownership': 'ownership',
        'sticky': 'sticky'
    }

    def __init__(self, dacl=None, delete_child=None, expected=None, ownership=None, sticky=None):  # noqa: E501
        """AuthAccessAccessItemPermissions - a model defined in Swagger"""  # noqa: E501

        self._dacl = None
        self._delete_child = None
        self._expected = None
        self._ownership = None
        self._sticky = None
        self.discriminator = None

        if dacl is not None:
            self.dacl = dacl
        if delete_child is not None:
            self.delete_child = delete_child
        if expected is not None:
            self.expected = expected
        if ownership is not None:
            self.ownership = ownership
        if sticky is not None:
            self.sticky = sticky

    @property
    def dacl(self):
        """Gets the dacl of this AuthAccessAccessItemPermissions.  # noqa: E501

        Returns a status message if the Null ACL is set.  # noqa: E501

        :return: The dacl of this AuthAccessAccessItemPermissions.  # noqa: E501
        :rtype: str
        """
        return self._dacl

    @dacl.setter
    def dacl(self, dacl):
        """Sets the dacl of this AuthAccessAccessItemPermissions.

        Returns a status message if the Null ACL is set.  # noqa: E501

        :param dacl: The dacl of this AuthAccessAccessItemPermissions.  # noqa: E501
        :type: str
        """

        self._dacl = dacl

    @property
    def delete_child(self):
        """Gets the delete_child of this AuthAccessAccessItemPermissions.  # noqa: E501

        Returns a status message if the parent directory has the delete_child property set for the user. If the delete_child property is set for a user, that user is able to delete the file.the delete_child for the user.  # noqa: E501

        :return: The delete_child of this AuthAccessAccessItemPermissions.  # noqa: E501
        :rtype: str
        """
        return self._delete_child

    @delete_child.setter
    def delete_child(self, delete_child):
        """Sets the delete_child of this AuthAccessAccessItemPermissions.

        Returns a status message if the parent directory has the delete_child property set for the user. If the delete_child property is set for a user, that user is able to delete the file.the delete_child for the user.  # noqa: E501

        :param delete_child: The delete_child of this AuthAccessAccessItemPermissions.  # noqa: E501
        :type: str
        """

        self._delete_child = delete_child

    @property
    def expected(self):
        """Gets the expected of this AuthAccessAccessItemPermissions.  # noqa: E501

        Specifies the Access Control Entity (ACE) for the user.  # noqa: E501

        :return: The expected of this AuthAccessAccessItemPermissions.  # noqa: E501
        :rtype: str
        """
        return self._expected

    @expected.setter
    def expected(self, expected):
        """Sets the expected of this AuthAccessAccessItemPermissions.

        Specifies the Access Control Entity (ACE) for the user.  # noqa: E501

        :param expected: The expected of this AuthAccessAccessItemPermissions.  # noqa: E501
        :type: str
        """

        self._expected = expected

    @property
    def ownership(self):
        """Gets the ownership of this AuthAccessAccessItemPermissions.  # noqa: E501

        Returns a status message if the user owns the file.  # noqa: E501

        :return: The ownership of this AuthAccessAccessItemPermissions.  # noqa: E501
        :rtype: str
        """
        return self._ownership

    @ownership.setter
    def ownership(self, ownership):
        """Sets the ownership of this AuthAccessAccessItemPermissions.

        Returns a status message if the user owns the file.  # noqa: E501

        :param ownership: The ownership of this AuthAccessAccessItemPermissions.  # noqa: E501
        :type: str
        """

        self._ownership = ownership

    @property
    def sticky(self):
        """Gets the sticky of this AuthAccessAccessItemPermissions.  # noqa: E501

        Returns a status message if the user owns the file.  # noqa: E501

        :return: The sticky of this AuthAccessAccessItemPermissions.  # noqa: E501
        :rtype: str
        """
        return self._sticky

    @sticky.setter
    def sticky(self, sticky):
        """Sets the sticky of this AuthAccessAccessItemPermissions.

        Returns a status message if the user owns the file.  # noqa: E501

        :param sticky: The sticky of this AuthAccessAccessItemPermissions.  # noqa: E501
        :type: str
        """

        self._sticky = sticky

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
        if not isinstance(other, AuthAccessAccessItemPermissions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
