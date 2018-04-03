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

from isi_sdk_8_0.models.snapshot_snapshot import SnapshotSnapshot  # noqa: F401,E501


class SnapshotSnapshotExtended(object):
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
        'alias': 'str',
        'expires': 'int',
        'name': 'str',
        'created': 'int',
        'has_locks': 'bool',
        'id': 'int',
        'path': 'str',
        'pct_filesystem': 'float',
        'pct_reserve': 'float',
        'schedule': 'str',
        'shadow_bytes': 'int',
        'size': 'int',
        'state': 'str',
        'target_id': 'int',
        'target_name': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'expires': 'expires',
        'name': 'name',
        'created': 'created',
        'has_locks': 'has_locks',
        'id': 'id',
        'path': 'path',
        'pct_filesystem': 'pct_filesystem',
        'pct_reserve': 'pct_reserve',
        'schedule': 'schedule',
        'shadow_bytes': 'shadow_bytes',
        'size': 'size',
        'state': 'state',
        'target_id': 'target_id',
        'target_name': 'target_name'
    }

    def __init__(self, alias=None, expires=None, name=None, created=None, has_locks=None, id=None, path=None, pct_filesystem=None, pct_reserve=None, schedule=None, shadow_bytes=None, size=None, state=None, target_id=None, target_name=None):  # noqa: E501
        """SnapshotSnapshotExtended - a model defined in Swagger"""  # noqa: E501

        self._alias = None
        self._expires = None
        self._name = None
        self._created = None
        self._has_locks = None
        self._id = None
        self._path = None
        self._pct_filesystem = None
        self._pct_reserve = None
        self._schedule = None
        self._shadow_bytes = None
        self._size = None
        self._state = None
        self._target_id = None
        self._target_name = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if expires is not None:
            self.expires = expires
        if name is not None:
            self.name = name
        self.created = created
        self.has_locks = has_locks
        self.id = id
        if path is not None:
            self.path = path
        self.pct_filesystem = pct_filesystem
        self.pct_reserve = pct_reserve
        if schedule is not None:
            self.schedule = schedule
        self.shadow_bytes = shadow_bytes
        self.size = size
        self.state = state
        if target_id is not None:
            self.target_id = target_id
        if target_name is not None:
            self.target_name = target_name

    @property
    def alias(self):
        """Gets the alias of this SnapshotSnapshotExtended.  # noqa: E501

        Alias name to create for this snapshot. If null, remove any alias.  # noqa: E501

        :return: The alias of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this SnapshotSnapshotExtended.

        Alias name to create for this snapshot. If null, remove any alias.  # noqa: E501

        :param alias: The alias of this SnapshotSnapshotExtended.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def expires(self):
        """Gets the expires of this SnapshotSnapshotExtended.  # noqa: E501

        The Unix Epoch time the snapshot will expire and be eligible for automatic deletion.  # noqa: E501

        :return: The expires of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: int
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """Sets the expires of this SnapshotSnapshotExtended.

        The Unix Epoch time the snapshot will expire and be eligible for automatic deletion.  # noqa: E501

        :param expires: The expires of this SnapshotSnapshotExtended.  # noqa: E501
        :type: int
        """

        self._expires = expires

    @property
    def name(self):
        """Gets the name of this SnapshotSnapshotExtended.  # noqa: E501

        The user or system supplied snapshot name. This will be null for snapshots pending delete.  # noqa: E501

        :return: The name of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotSnapshotExtended.

        The user or system supplied snapshot name. This will be null for snapshots pending delete.  # noqa: E501

        :param name: The name of this SnapshotSnapshotExtended.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created(self):
        """Gets the created of this SnapshotSnapshotExtended.  # noqa: E501

        The Unix Epoch time the snapshot was created.  # noqa: E501

        :return: The created of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SnapshotSnapshotExtended.

        The Unix Epoch time the snapshot was created.  # noqa: E501

        :param created: The created of this SnapshotSnapshotExtended.  # noqa: E501
        :type: int
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def has_locks(self):
        """Gets the has_locks of this SnapshotSnapshotExtended.  # noqa: E501

        True if the snapshot has one or more locks present see, see the locks subresource of a snapshot for a list of locks.  # noqa: E501

        :return: The has_locks of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: bool
        """
        return self._has_locks

    @has_locks.setter
    def has_locks(self, has_locks):
        """Sets the has_locks of this SnapshotSnapshotExtended.

        True if the snapshot has one or more locks present see, see the locks subresource of a snapshot for a list of locks.  # noqa: E501

        :param has_locks: The has_locks of this SnapshotSnapshotExtended.  # noqa: E501
        :type: bool
        """
        if has_locks is None:
            raise ValueError("Invalid value for `has_locks`, must not be `None`")  # noqa: E501

        self._has_locks = has_locks

    @property
    def id(self):
        """Gets the id of this SnapshotSnapshotExtended.  # noqa: E501

        The system ID given to the snapshot. This is useful for tracking the status of delete pending snapshots.  # noqa: E501

        :return: The id of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SnapshotSnapshotExtended.

        The system ID given to the snapshot. This is useful for tracking the status of delete pending snapshots.  # noqa: E501

        :param id: The id of this SnapshotSnapshotExtended.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def path(self):
        """Gets the path of this SnapshotSnapshotExtended.  # noqa: E501

        The /ifs path snapshotted.  # noqa: E501

        :return: The path of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this SnapshotSnapshotExtended.

        The /ifs path snapshotted.  # noqa: E501

        :param path: The path of this SnapshotSnapshotExtended.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def pct_filesystem(self):
        """Gets the pct_filesystem of this SnapshotSnapshotExtended.  # noqa: E501

        Percentage of /ifs used for storing this snapshot.  # noqa: E501

        :return: The pct_filesystem of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: float
        """
        return self._pct_filesystem

    @pct_filesystem.setter
    def pct_filesystem(self, pct_filesystem):
        """Sets the pct_filesystem of this SnapshotSnapshotExtended.

        Percentage of /ifs used for storing this snapshot.  # noqa: E501

        :param pct_filesystem: The pct_filesystem of this SnapshotSnapshotExtended.  # noqa: E501
        :type: float
        """
        if pct_filesystem is None:
            raise ValueError("Invalid value for `pct_filesystem`, must not be `None`")  # noqa: E501

        self._pct_filesystem = pct_filesystem

    @property
    def pct_reserve(self):
        """Gets the pct_reserve of this SnapshotSnapshotExtended.  # noqa: E501

        Percentage of configured snapshot reserved used for storing this snapshot.  # noqa: E501

        :return: The pct_reserve of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: float
        """
        return self._pct_reserve

    @pct_reserve.setter
    def pct_reserve(self, pct_reserve):
        """Sets the pct_reserve of this SnapshotSnapshotExtended.

        Percentage of configured snapshot reserved used for storing this snapshot.  # noqa: E501

        :param pct_reserve: The pct_reserve of this SnapshotSnapshotExtended.  # noqa: E501
        :type: float
        """
        if pct_reserve is None:
            raise ValueError("Invalid value for `pct_reserve`, must not be `None`")  # noqa: E501

        self._pct_reserve = pct_reserve

    @property
    def schedule(self):
        """Gets the schedule of this SnapshotSnapshotExtended.  # noqa: E501

        The name of the schedule used to create this snapshot, if applicable.  # noqa: E501

        :return: The schedule of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this SnapshotSnapshotExtended.

        The name of the schedule used to create this snapshot, if applicable.  # noqa: E501

        :param schedule: The schedule of this SnapshotSnapshotExtended.  # noqa: E501
        :type: str
        """

        self._schedule = schedule

    @property
    def shadow_bytes(self):
        """Gets the shadow_bytes of this SnapshotSnapshotExtended.  # noqa: E501

        The amount of shadow bytes referred to by this snapshot.  # noqa: E501

        :return: The shadow_bytes of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: int
        """
        return self._shadow_bytes

    @shadow_bytes.setter
    def shadow_bytes(self, shadow_bytes):
        """Sets the shadow_bytes of this SnapshotSnapshotExtended.

        The amount of shadow bytes referred to by this snapshot.  # noqa: E501

        :param shadow_bytes: The shadow_bytes of this SnapshotSnapshotExtended.  # noqa: E501
        :type: int
        """
        if shadow_bytes is None:
            raise ValueError("Invalid value for `shadow_bytes`, must not be `None`")  # noqa: E501

        self._shadow_bytes = shadow_bytes

    @property
    def size(self):
        """Gets the size of this SnapshotSnapshotExtended.  # noqa: E501

        The amount of storage in bytes used to store this snapshot.  # noqa: E501

        :return: The size of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SnapshotSnapshotExtended.

        The amount of storage in bytes used to store this snapshot.  # noqa: E501

        :param size: The size of this SnapshotSnapshotExtended.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def state(self):
        """Gets the state of this SnapshotSnapshotExtended.  # noqa: E501

        Snapshot state.  # noqa: E501

        :return: The state of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SnapshotSnapshotExtended.

        Snapshot state.  # noqa: E501

        :param state: The state of this SnapshotSnapshotExtended.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["active", "deleting"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def target_id(self):
        """Gets the target_id of this SnapshotSnapshotExtended.  # noqa: E501

        The ID of the snapshot pointed to if this is an alias.  # noqa: E501

        :return: The target_id of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: int
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """Sets the target_id of this SnapshotSnapshotExtended.

        The ID of the snapshot pointed to if this is an alias.  # noqa: E501

        :param target_id: The target_id of this SnapshotSnapshotExtended.  # noqa: E501
        :type: int
        """

        self._target_id = target_id

    @property
    def target_name(self):
        """Gets the target_name of this SnapshotSnapshotExtended.  # noqa: E501

        The name of the snapshot pointed to if this is an alias.  # noqa: E501

        :return: The target_name of this SnapshotSnapshotExtended.  # noqa: E501
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """Sets the target_name of this SnapshotSnapshotExtended.

        The name of the snapshot pointed to if this is an alias.  # noqa: E501

        :param target_name: The target_name of this SnapshotSnapshotExtended.  # noqa: E501
        :type: str
        """

        self._target_name = target_name

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
        if not isinstance(other, SnapshotSnapshotExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
