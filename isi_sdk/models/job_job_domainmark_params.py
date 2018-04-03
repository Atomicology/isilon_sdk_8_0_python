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


class JobJobDomainmarkParams(object):
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
        'delete': 'bool',
        'root': 'str',
        'type': 'str'
    }

    attribute_map = {
        'delete': 'delete',
        'root': 'root',
        'type': 'type'
    }

    def __init__(self, delete=None, root=None, type=None):  # noqa: E501
        """JobJobDomainmarkParams - a model defined in Swagger"""  # noqa: E501

        self._delete = None
        self._root = None
        self._type = None
        self.discriminator = None

        if delete is not None:
            self.delete = delete
        self.root = root
        self.type = type

    @property
    def delete(self):
        """Gets the delete of this JobJobDomainmarkParams.  # noqa: E501

        Whether this is a delete operation.  # noqa: E501

        :return: The delete of this JobJobDomainmarkParams.  # noqa: E501
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """Sets the delete of this JobJobDomainmarkParams.

        Whether this is a delete operation.  # noqa: E501

        :param delete: The delete of this JobJobDomainmarkParams.  # noqa: E501
        :type: bool
        """

        self._delete = delete

    @property
    def root(self):
        """Gets the root of this JobJobDomainmarkParams.  # noqa: E501

        Base IFS path to associate with the domain.  # noqa: E501

        :return: The root of this JobJobDomainmarkParams.  # noqa: E501
        :rtype: str
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this JobJobDomainmarkParams.

        Base IFS path to associate with the domain.  # noqa: E501

        :param root: The root of this JobJobDomainmarkParams.  # noqa: E501
        :type: str
        """
        if root is None:
            raise ValueError("Invalid value for `root`, must not be `None`")  # noqa: E501

        self._root = root

    @property
    def type(self):
        """Gets the type of this JobJobDomainmarkParams.  # noqa: E501

        The type of domain.  # noqa: E501

        :return: The type of this JobJobDomainmarkParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this JobJobDomainmarkParams.

        The type of domain.  # noqa: E501

        :param type: The type of this JobJobDomainmarkParams.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["SnapRevert", "SyncIQ", "Worm"]  # noqa: E501
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
        if not isinstance(other, JobJobDomainmarkParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
