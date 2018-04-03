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

from isi_sdk_8_0.models.job_policy_interval import JobPolicyInterval  # noqa: F401,E501


class JobPoliciesType(object):
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
        'description': 'str',
        'id': 'str',
        'intervals': 'list[JobPolicyInterval]',
        'name': 'str',
        'system': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'id': 'id',
        'intervals': 'intervals',
        'name': 'name',
        'system': 'system'
    }

    def __init__(self, description=None, id=None, intervals=None, name=None, system=None):  # noqa: E501
        """JobPoliciesType - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._id = None
        self._intervals = None
        self._name = None
        self._system = None
        self.discriminator = None

        self.description = description
        self.id = id
        self.intervals = intervals
        self.name = name
        if system is not None:
            self.system = system

    @property
    def description(self):
        """Gets the description of this JobPoliciesType.  # noqa: E501

        A helpful human-readable description of the impact policy.  # noqa: E501

        :return: The description of this JobPoliciesType.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this JobPoliciesType.

        A helpful human-readable description of the impact policy.  # noqa: E501

        :param description: The description of this JobPoliciesType.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def id(self):
        """Gets the id of this JobPoliciesType.  # noqa: E501

        The ID of the impact policy.  # noqa: E501

        :return: The id of this JobPoliciesType.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this JobPoliciesType.

        The ID of the impact policy.  # noqa: E501

        :param id: The id of this JobPoliciesType.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def intervals(self):
        """Gets the intervals of this JobPoliciesType.  # noqa: E501


        :return: The intervals of this JobPoliciesType.  # noqa: E501
        :rtype: list[JobPolicyInterval]
        """
        return self._intervals

    @intervals.setter
    def intervals(self, intervals):
        """Sets the intervals of this JobPoliciesType.


        :param intervals: The intervals of this JobPoliciesType.  # noqa: E501
        :type: list[JobPolicyInterval]
        """
        if intervals is None:
            raise ValueError("Invalid value for `intervals`, must not be `None`")  # noqa: E501

        self._intervals = intervals

    @property
    def name(self):
        """Gets the name of this JobPoliciesType.  # noqa: E501

        The name of the impact policy.  # noqa: E501

        :return: The name of this JobPoliciesType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this JobPoliciesType.

        The name of the impact policy.  # noqa: E501

        :param name: The name of this JobPoliciesType.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def system(self):
        """Gets the system of this JobPoliciesType.  # noqa: E501

        Whether or not this is a read-only system impact policy.  # noqa: E501

        :return: The system of this JobPoliciesType.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this JobPoliciesType.

        Whether or not this is a read-only system impact policy.  # noqa: E501

        :param system: The system of this JobPoliciesType.  # noqa: E501
        :type: bool
        """

        self._system = system

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
        if not isinstance(other, JobPoliciesType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
