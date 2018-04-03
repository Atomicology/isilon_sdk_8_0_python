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

from isi_sdk_8_0.models.cloud_account import CloudAccount  # noqa: F401,E501


class CloudAccountExtended(object):
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
        'account_id': 'str',
        'account_username': 'str',
        'birth_cluster_id': 'str',
        'enabled': 'bool',
        'key': 'str',
        'name': 'str',
        'skip_ssl_validation': 'bool',
        'storage_region': 'str',
        'telemetry_bucket': 'str',
        'uri': 'str',
        'bucket': 'str',
        'id': 'str',
        'metadata_bucket': 'str',
        'pool': 'str',
        'state': 'str',
        'state_details': 'str',
        'type': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_username': 'account_username',
        'birth_cluster_id': 'birth_cluster_id',
        'enabled': 'enabled',
        'key': 'key',
        'name': 'name',
        'skip_ssl_validation': 'skip_ssl_validation',
        'storage_region': 'storage_region',
        'telemetry_bucket': 'telemetry_bucket',
        'uri': 'uri',
        'bucket': 'bucket',
        'id': 'id',
        'metadata_bucket': 'metadata_bucket',
        'pool': 'pool',
        'state': 'state',
        'state_details': 'state_details',
        'type': 'type'
    }

    def __init__(self, account_id=None, account_username=None, birth_cluster_id=None, enabled=None, key=None, name=None, skip_ssl_validation=None, storage_region=None, telemetry_bucket=None, uri=None, bucket=None, id=None, metadata_bucket=None, pool=None, state=None, state_details=None, type=None):  # noqa: E501
        """CloudAccountExtended - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._account_username = None
        self._birth_cluster_id = None
        self._enabled = None
        self._key = None
        self._name = None
        self._skip_ssl_validation = None
        self._storage_region = None
        self._telemetry_bucket = None
        self._uri = None
        self._bucket = None
        self._id = None
        self._metadata_bucket = None
        self._pool = None
        self._state = None
        self._state_details = None
        self._type = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if account_username is not None:
            self.account_username = account_username
        if birth_cluster_id is not None:
            self.birth_cluster_id = birth_cluster_id
        if enabled is not None:
            self.enabled = enabled
        if key is not None:
            self.key = key
        if name is not None:
            self.name = name
        if skip_ssl_validation is not None:
            self.skip_ssl_validation = skip_ssl_validation
        if storage_region is not None:
            self.storage_region = storage_region
        if telemetry_bucket is not None:
            self.telemetry_bucket = telemetry_bucket
        if uri is not None:
            self.uri = uri
        if bucket is not None:
            self.bucket = bucket
        if id is not None:
            self.id = id
        if metadata_bucket is not None:
            self.metadata_bucket = metadata_bucket
        if pool is not None:
            self.pool = pool
        if state is not None:
            self.state = state
        if state_details is not None:
            self.state_details = state_details
        if type is not None:
            self.type = type

    @property
    def account_id(self):
        """Gets the account_id of this CloudAccountExtended.  # noqa: E501

        (S3 only) The user id of the S3 account  # noqa: E501

        :return: The account_id of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CloudAccountExtended.

        (S3 only) The user id of the S3 account  # noqa: E501

        :param account_id: The account_id of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def account_username(self):
        """Gets the account_username of this CloudAccountExtended.  # noqa: E501

        The username required to authenticate against the cloud service  # noqa: E501

        :return: The account_username of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._account_username

    @account_username.setter
    def account_username(self, account_username):
        """Sets the account_username of this CloudAccountExtended.

        The username required to authenticate against the cloud service  # noqa: E501

        :param account_username: The account_username of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._account_username = account_username

    @property
    def birth_cluster_id(self):
        """Gets the birth_cluster_id of this CloudAccountExtended.  # noqa: E501

        The guid of the cluster where this account was created  # noqa: E501

        :return: The birth_cluster_id of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._birth_cluster_id

    @birth_cluster_id.setter
    def birth_cluster_id(self, birth_cluster_id):
        """Sets the birth_cluster_id of this CloudAccountExtended.

        The guid of the cluster where this account was created  # noqa: E501

        :param birth_cluster_id: The birth_cluster_id of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._birth_cluster_id = birth_cluster_id

    @property
    def enabled(self):
        """Gets the enabled of this CloudAccountExtended.  # noqa: E501

        Whether this account is explicitly enabled or disabled by a user  # noqa: E501

        :return: The enabled of this CloudAccountExtended.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CloudAccountExtended.

        Whether this account is explicitly enabled or disabled by a user  # noqa: E501

        :param enabled: The enabled of this CloudAccountExtended.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def key(self):
        """Gets the key of this CloudAccountExtended.  # noqa: E501

        A valid authentication key for connecting to the cloud  # noqa: E501

        :return: The key of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CloudAccountExtended.

        A valid authentication key for connecting to the cloud  # noqa: E501

        :param key: The key of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def name(self):
        """Gets the name of this CloudAccountExtended.  # noqa: E501

        A unique name for this account  # noqa: E501

        :return: The name of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CloudAccountExtended.

        A unique name for this account  # noqa: E501

        :param name: The name of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def skip_ssl_validation(self):
        """Gets the skip_ssl_validation of this CloudAccountExtended.  # noqa: E501

        Indicates whether to skip SSL certificate validation when connecting to the cloud  # noqa: E501

        :return: The skip_ssl_validation of this CloudAccountExtended.  # noqa: E501
        :rtype: bool
        """
        return self._skip_ssl_validation

    @skip_ssl_validation.setter
    def skip_ssl_validation(self, skip_ssl_validation):
        """Sets the skip_ssl_validation of this CloudAccountExtended.

        Indicates whether to skip SSL certificate validation when connecting to the cloud  # noqa: E501

        :param skip_ssl_validation: The skip_ssl_validation of this CloudAccountExtended.  # noqa: E501
        :type: bool
        """

        self._skip_ssl_validation = skip_ssl_validation

    @property
    def storage_region(self):
        """Gets the storage_region of this CloudAccountExtended.  # noqa: E501

        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region  # noqa: E501

        :return: The storage_region of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._storage_region

    @storage_region.setter
    def storage_region(self, storage_region):
        """Sets the storage_region of this CloudAccountExtended.

        (S3 only) An appropriate region for the S3 account.  For example, faster access times may be gained by referencing a nearby region  # noqa: E501

        :param storage_region: The storage_region of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._storage_region = storage_region

    @property
    def telemetry_bucket(self):
        """Gets the telemetry_bucket of this CloudAccountExtended.  # noqa: E501

        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider  # noqa: E501

        :return: The telemetry_bucket of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._telemetry_bucket

    @telemetry_bucket.setter
    def telemetry_bucket(self, telemetry_bucket):
        """Sets the telemetry_bucket of this CloudAccountExtended.

        (S3 only) The name of the bucket into which generated metrics reports are placed by the cloud service provider  # noqa: E501

        :param telemetry_bucket: The telemetry_bucket of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._telemetry_bucket = telemetry_bucket

    @property
    def uri(self):
        """Gets the uri of this CloudAccountExtended.  # noqa: E501

        A valid URI pointing to the location of the cloud storage  # noqa: E501

        :return: The uri of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this CloudAccountExtended.

        A valid URI pointing to the location of the cloud storage  # noqa: E501

        :param uri: The uri of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def bucket(self):
        """Gets the bucket of this CloudAccountExtended.  # noqa: E501

        The machine generated name of the account bucket to store data  # noqa: E501

        :return: The bucket of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this CloudAccountExtended.

        The machine generated name of the account bucket to store data  # noqa: E501

        :param bucket: The bucket of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def id(self):
        """Gets the id of this CloudAccountExtended.  # noqa: E501

        A globally unique name for this account  # noqa: E501

        :return: The id of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudAccountExtended.

        A globally unique name for this account  # noqa: E501

        :param id: The id of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def metadata_bucket(self):
        """Gets the metadata_bucket of this CloudAccountExtended.  # noqa: E501

        The machine generated name of the account bucket to store metadata  # noqa: E501

        :return: The metadata_bucket of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._metadata_bucket

    @metadata_bucket.setter
    def metadata_bucket(self, metadata_bucket):
        """Sets the metadata_bucket of this CloudAccountExtended.

        The machine generated name of the account bucket to store metadata  # noqa: E501

        :param metadata_bucket: The metadata_bucket of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._metadata_bucket = metadata_bucket

    @property
    def pool(self):
        """Gets the pool of this CloudAccountExtended.  # noqa: E501

        Name of the pool referencing this account.  Empty if none.  # noqa: E501

        :return: The pool of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._pool

    @pool.setter
    def pool(self, pool):
        """Sets the pool of this CloudAccountExtended.

        Name of the pool referencing this account.  Empty if none.  # noqa: E501

        :param pool: The pool of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._pool = pool

    @property
    def state(self):
        """Gets the state of this CloudAccountExtended.  # noqa: E501

        Indicates whether this account is in a good state (\"OK\"), disabled (\"disabled\") or inaccessible via the network (\"unreachable\")  # noqa: E501

        :return: The state of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CloudAccountExtended.

        Indicates whether this account is in a good state (\"OK\"), disabled (\"disabled\") or inaccessible via the network (\"unreachable\")  # noqa: E501

        :param state: The state of this CloudAccountExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["OK", "disabled", "unreachable"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def state_details(self):
        """Gets the state_details of this CloudAccountExtended.  # noqa: E501

        Gives further information to describe the state of this account  # noqa: E501

        :return: The state_details of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._state_details

    @state_details.setter
    def state_details(self, state_details):
        """Sets the state_details of this CloudAccountExtended.

        Gives further information to describe the state of this account  # noqa: E501

        :param state_details: The state_details of this CloudAccountExtended.  # noqa: E501
        :type: str
        """

        self._state_details = state_details

    @property
    def type(self):
        """Gets the type of this CloudAccountExtended.  # noqa: E501

        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3  # noqa: E501

        :return: The type of this CloudAccountExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudAccountExtended.

        The type of cloud protocol required.  E.g., \"isilon\" for EMC Isilon, \"ecs\" for EMC ECS Appliance, \"virtustream\" for Virtustream Storage Cloud, \"azure\" for Microsoft Azure and \"s3\" for Amazon S3  # noqa: E501

        :param type: The type of this CloudAccountExtended.  # noqa: E501
        :type: str
        """
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
        if not isinstance(other, CloudAccountExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
