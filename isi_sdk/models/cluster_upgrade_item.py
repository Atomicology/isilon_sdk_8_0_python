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


class ClusterUpgradeItem(object):
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
        'install_image_path': 'str',
        'nodes_to_rolling_upgrade': 'list[int]',
        'skip_optional': 'bool',
        'upgrade_type': 'str'
    }

    attribute_map = {
        'install_image_path': 'install_image_path',
        'nodes_to_rolling_upgrade': 'nodes_to_rolling_upgrade',
        'skip_optional': 'skip_optional',
        'upgrade_type': 'upgrade_type'
    }

    def __init__(self, install_image_path=None, nodes_to_rolling_upgrade=None, skip_optional=None, upgrade_type=None):  # noqa: E501
        """ClusterUpgradeItem - a model defined in Swagger"""  # noqa: E501

        self._install_image_path = None
        self._nodes_to_rolling_upgrade = None
        self._skip_optional = None
        self._upgrade_type = None
        self.discriminator = None

        if install_image_path is not None:
            self.install_image_path = install_image_path
        if nodes_to_rolling_upgrade is not None:
            self.nodes_to_rolling_upgrade = nodes_to_rolling_upgrade
        if skip_optional is not None:
            self.skip_optional = skip_optional
        if upgrade_type is not None:
            self.upgrade_type = upgrade_type

    @property
    def install_image_path(self):
        """Gets the install_image_path of this ClusterUpgradeItem.  # noqa: E501

        The location (path) of the upgrade image which must be within /ifs.  # noqa: E501

        :return: The install_image_path of this ClusterUpgradeItem.  # noqa: E501
        :rtype: str
        """
        return self._install_image_path

    @install_image_path.setter
    def install_image_path(self, install_image_path):
        """Sets the install_image_path of this ClusterUpgradeItem.

        The location (path) of the upgrade image which must be within /ifs.  # noqa: E501

        :param install_image_path: The install_image_path of this ClusterUpgradeItem.  # noqa: E501
        :type: str
        """

        self._install_image_path = install_image_path

    @property
    def nodes_to_rolling_upgrade(self):
        """Gets the nodes_to_rolling_upgrade of this ClusterUpgradeItem.  # noqa: E501

        The nodes (to be) scheduled for upgrade ordered by queue position number. Null if the cluster_state is 'partially upgraded' or upgrade_type is 'simultaneous'. One of the following values: [<lnn-1>, <lnn-2>, ... ], 'All', null  # noqa: E501

        :return: The nodes_to_rolling_upgrade of this ClusterUpgradeItem.  # noqa: E501
        :rtype: list[int]
        """
        return self._nodes_to_rolling_upgrade

    @nodes_to_rolling_upgrade.setter
    def nodes_to_rolling_upgrade(self, nodes_to_rolling_upgrade):
        """Sets the nodes_to_rolling_upgrade of this ClusterUpgradeItem.

        The nodes (to be) scheduled for upgrade ordered by queue position number. Null if the cluster_state is 'partially upgraded' or upgrade_type is 'simultaneous'. One of the following values: [<lnn-1>, <lnn-2>, ... ], 'All', null  # noqa: E501

        :param nodes_to_rolling_upgrade: The nodes_to_rolling_upgrade of this ClusterUpgradeItem.  # noqa: E501
        :type: list[int]
        """

        self._nodes_to_rolling_upgrade = nodes_to_rolling_upgrade

    @property
    def skip_optional(self):
        """Gets the skip_optional of this ClusterUpgradeItem.  # noqa: E501

        Used to indicate that the pre-upgrade check should be skipped  # noqa: E501

        :return: The skip_optional of this ClusterUpgradeItem.  # noqa: E501
        :rtype: bool
        """
        return self._skip_optional

    @skip_optional.setter
    def skip_optional(self, skip_optional):
        """Sets the skip_optional of this ClusterUpgradeItem.

        Used to indicate that the pre-upgrade check should be skipped  # noqa: E501

        :param skip_optional: The skip_optional of this ClusterUpgradeItem.  # noqa: E501
        :type: bool
        """

        self._skip_optional = skip_optional

    @property
    def upgrade_type(self):
        """Gets the upgrade_type of this ClusterUpgradeItem.  # noqa: E501

        The type of upgrade to perform. One of the following values: 'rolling', 'simultaneous'  # noqa: E501

        :return: The upgrade_type of this ClusterUpgradeItem.  # noqa: E501
        :rtype: str
        """
        return self._upgrade_type

    @upgrade_type.setter
    def upgrade_type(self, upgrade_type):
        """Sets the upgrade_type of this ClusterUpgradeItem.

        The type of upgrade to perform. One of the following values: 'rolling', 'simultaneous'  # noqa: E501

        :param upgrade_type: The upgrade_type of this ClusterUpgradeItem.  # noqa: E501
        :type: str
        """

        self._upgrade_type = upgrade_type

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
        if not isinstance(other, ClusterUpgradeItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
