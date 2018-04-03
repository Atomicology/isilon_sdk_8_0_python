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

from isi_sdk_8_0.models.cloud_job_files import CloudJobFiles  # noqa: F401,E501
from isi_sdk_8_0.models.cloud_job_job_engine_job import CloudJobJobEngineJob  # noqa: F401,E501


class CloudJobExtended(object):
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
        'completion_time': 'int',
        'create_time': 'int',
        'description': 'str',
        'effective_state': 'str',
        'files': 'CloudJobFiles',
        'id': 'int',
        'job_engine_job': 'CloudJobJobEngineJob',
        'job_state': 'str',
        'operation_state': 'str',
        'state_change_time': 'int',
        'type': 'str'
    }

    attribute_map = {
        'completion_time': 'completion_time',
        'create_time': 'create_time',
        'description': 'description',
        'effective_state': 'effective_state',
        'files': 'files',
        'id': 'id',
        'job_engine_job': 'job_engine_job',
        'job_state': 'job_state',
        'operation_state': 'operation_state',
        'state_change_time': 'state_change_time',
        'type': 'type'
    }

    def __init__(self, completion_time=None, create_time=None, description=None, effective_state=None, files=None, id=None, job_engine_job=None, job_state=None, operation_state=None, state_change_time=None, type=None):  # noqa: E501
        """CloudJobExtended - a model defined in Swagger"""  # noqa: E501

        self._completion_time = None
        self._create_time = None
        self._description = None
        self._effective_state = None
        self._files = None
        self._id = None
        self._job_engine_job = None
        self._job_state = None
        self._operation_state = None
        self._state_change_time = None
        self._type = None
        self.discriminator = None

        if completion_time is not None:
            self.completion_time = completion_time
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if effective_state is not None:
            self.effective_state = effective_state
        if files is not None:
            self.files = files
        if id is not None:
            self.id = id
        if job_engine_job is not None:
            self.job_engine_job = job_engine_job
        if job_state is not None:
            self.job_state = job_state
        if operation_state is not None:
            self.operation_state = operation_state
        if state_change_time is not None:
            self.state_change_time = state_change_time
        if type is not None:
            self.type = type

    @property
    def completion_time(self):
        """Gets the completion_time of this CloudJobExtended.  # noqa: E501

        The time at which the job was completed (if applicable)  # noqa: E501

        :return: The completion_time of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this CloudJobExtended.

        The time at which the job was completed (if applicable)  # noqa: E501

        :param completion_time: The completion_time of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._completion_time = completion_time

    @property
    def create_time(self):
        """Gets the create_time of this CloudJobExtended.  # noqa: E501

        The time at which the job was created  # noqa: E501

        :return: The create_time of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this CloudJobExtended.

        The time at which the job was created  # noqa: E501

        :param create_time: The create_time of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this CloudJobExtended.  # noqa: E501

        A brief description of the job contents  # noqa: E501

        :return: The description of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CloudJobExtended.

        A brief description of the job contents  # noqa: E501

        :param description: The description of this CloudJobExtended.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def effective_state(self):
        """Gets the effective_state of this CloudJobExtended.  # noqa: E501

        The effective state of the job (e.g,. the combination of operation_state and job_state)  # noqa: E501

        :return: The effective_state of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._effective_state

    @effective_state.setter
    def effective_state(self, effective_state):
        """Sets the effective_state of this CloudJobExtended.

        The effective state of the job (e.g,. the combination of operation_state and job_state)  # noqa: E501

        :param effective_state: The effective_state of this CloudJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["running", "paused", "canceled", "completed", "failed"]  # noqa: E501
        if effective_state not in allowed_values:
            raise ValueError(
                "Invalid value for `effective_state` ({0}), must be one of {1}"  # noqa: E501
                .format(effective_state, allowed_values)
            )

        self._effective_state = effective_state

    @property
    def files(self):
        """Gets the files of this CloudJobExtended.  # noqa: E501

        The files and filters addressed by this job  # noqa: E501

        :return: The files of this CloudJobExtended.  # noqa: E501
        :rtype: CloudJobFiles
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this CloudJobExtended.

        The files and filters addressed by this job  # noqa: E501

        :param files: The files of this CloudJobExtended.  # noqa: E501
        :type: CloudJobFiles
        """

        self._files = files

    @property
    def id(self):
        """Gets the id of this CloudJobExtended.  # noqa: E501

        The job's ID  # noqa: E501

        :return: The id of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudJobExtended.

        The job's ID  # noqa: E501

        :param id: The id of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def job_engine_job(self):
        """Gets the job_engine_job of this CloudJobExtended.  # noqa: E501

        Information about the related job engine job if there is one  # noqa: E501

        :return: The job_engine_job of this CloudJobExtended.  # noqa: E501
        :rtype: CloudJobJobEngineJob
        """
        return self._job_engine_job

    @job_engine_job.setter
    def job_engine_job(self, job_engine_job):
        """Sets the job_engine_job of this CloudJobExtended.

        Information about the related job engine job if there is one  # noqa: E501

        :param job_engine_job: The job_engine_job of this CloudJobExtended.  # noqa: E501
        :type: CloudJobJobEngineJob
        """

        self._job_engine_job = job_engine_job

    @property
    def job_state(self):
        """Gets the job_state of this CloudJobExtended.  # noqa: E501

        The current state of the job  # noqa: E501

        :return: The job_state of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """Sets the job_state of this CloudJobExtended.

        The current state of the job  # noqa: E501

        :param job_state: The job_state of this CloudJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["running", "paused", "canceled", "completed", "failed"]  # noqa: E501
        if job_state not in allowed_values:
            raise ValueError(
                "Invalid value for `job_state` ({0}), must be one of {1}"  # noqa: E501
                .format(job_state, allowed_values)
            )

        self._job_state = job_state

    @property
    def operation_state(self):
        """Gets the operation_state of this CloudJobExtended.  # noqa: E501

        The current state of the operation associated with the job  # noqa: E501

        :return: The operation_state of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._operation_state

    @operation_state.setter
    def operation_state(self, operation_state):
        """Sets the operation_state of this CloudJobExtended.

        The current state of the operation associated with the job  # noqa: E501

        :param operation_state: The operation_state of this CloudJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["running", "paused"]  # noqa: E501
        if operation_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operation_state` ({0}), must be one of {1}"  # noqa: E501
                .format(operation_state, allowed_values)
            )

        self._operation_state = operation_state

    @property
    def state_change_time(self):
        """Gets the state_change_time of this CloudJobExtended.  # noqa: E501

        The last time at which the job state changed  # noqa: E501

        :return: The state_change_time of this CloudJobExtended.  # noqa: E501
        :rtype: int
        """
        return self._state_change_time

    @state_change_time.setter
    def state_change_time(self, state_change_time):
        """Sets the state_change_time of this CloudJobExtended.

        The last time at which the job state changed  # noqa: E501

        :param state_change_time: The state_change_time of this CloudJobExtended.  # noqa: E501
        :type: int
        """

        self._state_change_time = state_change_time

    @property
    def type(self):
        """Gets the type of this CloudJobExtended.  # noqa: E501

        The type of cloud action to be performed by this job.  # noqa: E501

        :return: The type of this CloudJobExtended.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudJobExtended.

        The type of cloud action to be performed by this job.  # noqa: E501

        :param type: The type of this CloudJobExtended.  # noqa: E501
        :type: str
        """
        allowed_values = ["archive", "recall", "local-garbage-collection", "cloud-garbage-collection", "cache-writeback", "cache-on-access", "cache-invalidation", "restore-coi"]  # noqa: E501
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
        if not isinstance(other, CloudJobExtended):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
