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

from isi_sdk_8_0.models.cloud_pool import CloudPool  # noqa: F401,E501


class CloudPoolCreateParams(object):
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
        'birth_cluster_id': 'str',
        'description': 'str',
        'name': 'str',
        'vendor': 'str',
        'type': 'str'
    }

    attribute_map = {
        'accounts': 'accounts',
        'birth_cluster_id': 'birth_cluster_id',
        'description': 'description',
        'name': 'name',
        'vendor': 'vendor',
        'type': 'type'
    }

    def __init__(self, accounts=None, birth_cluster_id=None, description=None, name=None, vendor=None, type=None):  # noqa: E501
        """CloudPoolCreateParams - a model defined in Swagger"""  # noqa: E501

        self._accounts = None
        self._birth_cluster_id = None
        self._description = None
        self._name = None
        self._vendor = None
        self._type = None
        self.discriminator = None

        self.accounts = accounts
        if birth_cluster_id is not None:
            self.birth_cluster_id = birth_cluster_id
        if description is not None:
            self.description = description
        self.name = name
        if vendor is not None:
            self.vendor = vendor
        self.type = type

    @property
    def accounts(self):
        """Gets the accounts of this CloudPoolCreateParams.  # noqa: E501

        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.  # noqa: E501

        :return: The accounts of this CloudPoolCreateParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this CloudPoolCreateParams.

        A list of valid names for the accounts in this pool.  There is currently only one account allowed per pool.  # noqa: E501

        :param accounts: The accounts of this CloudPoolCreateParams.  # noqa: E501
        :type: list[str]
        """
        if accounts is None:
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def birth_cluster_id(self):
        """Gets the birth_cluster_id of this CloudPoolCreateParams.  # noqa: E501

        The guid of the cluster where this pool was created  # noqa: E501

        :return: The birth_cluster_id of this CloudPoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """Sets the birth_cluster_id of this CloudPoolCreateParams.

        The guid of the cluster where this pool was created  # noqa: E501

        :param birth_cluster_id: The birth_cluster_id of this CloudPoolCreateParams.  # noqa: E501
        :type: str
        """

        self._birth_cluster_id = birth_cluster_id

    @property
    def description(self):
        """Gets the description of this CloudPoolCreateParams.  # noqa: E501

        A brief description of this pool  # noqa: E501

        :return: The description of this CloudPoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudPoolCreateParams.

        A brief description of this pool  # noqa: E501

        :param description: The description of this CloudPoolCreateParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this CloudPoolCreateParams.  # noqa: E501

        A unique name for this pool  # noqa: E501

        :return: The name of this CloudPoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudPoolCreateParams.

        A unique name for this pool  # noqa: E501

        :param name: The name of this CloudPoolCreateParams.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def vendor(self):
        """Gets the vendor of this CloudPoolCreateParams.  # noqa: E501

        A string identifier of the cloud services vendor  # noqa: E501

        :return: The vendor of this CloudPoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this CloudPoolCreateParams.

        A string identifier of the cloud services vendor  # noqa: E501

        :param vendor: The vendor of this CloudPoolCreateParams.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def type(self):
        """Gets the type of this CloudPoolCreateParams.  # noqa: E501

        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3  # noqa: E501

        :return: The type of this CloudPoolCreateParams.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudPoolCreateParams.

        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3  # noqa: E501

        :param type: The type of this CloudPoolCreateParams.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["isilon", "ecs", "virtustream", "azure", "s3", "ran", "ecs2"]  # noqa: E501
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
        if not isinstance(other, CloudPoolCreateParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
