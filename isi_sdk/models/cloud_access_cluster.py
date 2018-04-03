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


class CloudAccessCluster(object):
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
        'accounts': 'list[str]',
        'current': 'bool',
        'guid': 'str',
        'id': 'str',
        'name': 'str',
        'policies': 'list[str]',
        'state': 'str',
        'synced_from': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'current': 'current',
        'guid': 'guid',
        'id': 'id',
        'name': 'name',
        'policies': 'policies',
        'state': 'state',
        'synced_from': 'synced_from'
    }

    def __init__(self, accounts=None, current=None, guid=None, id=None, name=None, policies=None, state=None, synced_from=None):  # noqa: E501
        """CloudAccessCluster - a model defined in Swagger"""  # noqa: E501

        self._accounts = None
        self._current = None
        self._guid = None
        self._id = None
        self._name = None
        self._policies = None
        self._state = None
        self._synced_from = None
        self.discriminator = None

        if accounts is not None:
            self.accounts = accounts
        if current is not None:
            self.current = current
        if guid is not None:
            self.guid = guid
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if policies is not None:
            self.policies = policies
        if state is not None:
            self.state = state
        if synced_from is not None:
            self.synced_from = synced_from

    @property
    def accounts(self):
        """Gets the accounts of this CloudAccessCluster.  # noqa: E501

        A list of accounts created on the cluster with this guid  # noqa: E501

        :return: The accounts of this CloudAccessCluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this CloudAccessCluster.

        A list of accounts created on the cluster with this guid  # noqa: E501

        :param accounts: The accounts of this CloudAccessCluster.  # noqa: E501
        :type: list[str]
        """

        self._accounts = accounts

    @property
    def current(self):
        """Gets the current of this CloudAccessCluster.  # noqa: E501

        Whether the guid is that of the current (local) cluster  # noqa: E501

        :return: The current of this CloudAccessCluster.  # noqa: E501
        :rtype: bool
        """
        return self._current

    @current.setter
    def current(self, current):
        """Sets the current of this CloudAccessCluster.

        Whether the guid is that of the current (local) cluster  # noqa: E501

        :param current: The current of this CloudAccessCluster.  # noqa: E501
        :type: bool
        """

        self._current = current

    @property
    def guid(self):
        """Gets the guid of this CloudAccessCluster.  # noqa: E501

        A cluster guid indicating the birth place of one or more accounts or policies on this cluster  # noqa: E501

        :return: The guid of this CloudAccessCluster.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this CloudAccessCluster.

        A cluster guid indicating the birth place of one or more accounts or policies on this cluster  # noqa: E501

        :param guid: The guid of this CloudAccessCluster.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def id(self):
        """Gets the id of this CloudAccessCluster.  # noqa: E501

        A cluster guid indicating the birth place of one or more accounts or policies on this cluster  # noqa: E501

        :return: The id of this CloudAccessCluster.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudAccessCluster.

        A cluster guid indicating the birth place of one or more accounts or policies on this cluster  # noqa: E501

        :param id: The id of this CloudAccessCluster.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CloudAccessCluster.  # noqa: E501

        The name of the cluster from which the above guid originated  # noqa: E501

        :return: The name of this CloudAccessCluster.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccessCluster.

        The name of the cluster from which the above guid originated  # noqa: E501

        :param name: The name of this CloudAccessCluster.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def policies(self):
        """Gets the policies of this CloudAccessCluster.  # noqa: E501

        A list of policies created on the cluster with this guid  # noqa: E501

        :return: The policies of this CloudAccessCluster.  # noqa: E501
        :rtype: list[str]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this CloudAccessCluster.

        A list of policies created on the cluster with this guid  # noqa: E501

        :param policies: The policies of this CloudAccessCluster.  # noqa: E501
        :type: list[str]
        """

        self._policies = policies

    @property
    def state(self):
        """Gets the state of this CloudAccessCluster.  # noqa: E501

        Whether the guid has access to the cloud  # noqa: E501

        :return: The state of this CloudAccessCluster.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CloudAccessCluster.

        Whether the guid has access to the cloud  # noqa: E501

        :param state: The state of this CloudAccessCluster.  # noqa: E501
        :type: str
        """
        allowed_values = ["permitted", "pending enable", "pending disable", "not permitted"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def synced_from(self):
        """Gets the synced_from of this CloudAccessCluster.  # noqa: E501

        The name of the cluster from which the above guid was synced  # noqa: E501

        :return: The synced_from of this CloudAccessCluster.  # noqa: E501
        :rtype: str
        """
        return self._synced_from

    @synced_from.setter
    def synced_from(self, synced_from):
        """Sets the synced_from of this CloudAccessCluster.

        The name of the cluster from which the above guid was synced  # noqa: E501

        :param synced_from: The synced_from of this CloudAccessCluster.  # noqa: E501
        :type: str
        """

        self._synced_from = synced_from

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
        if not isinstance(other, CloudAccessCluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
