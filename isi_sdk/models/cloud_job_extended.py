# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class CloudJobExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        CloudJobExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
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

        self.attribute_map = {
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

    @property
    def completion_time(self):
        """
        Gets the completion_time of this CloudJobExtended.
        The time at which the job was completed (if applicable)

        :return: The completion_time of this CloudJobExtended.
        :rtype: int
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """
        Sets the completion_time of this CloudJobExtended.
        The time at which the job was completed (if applicable)

        :param completion_time: The completion_time of this CloudJobExtended.
        :type: int
        """
        
        self._completion_time = completion_time

    @property
    def create_time(self):
        """
        Gets the create_time of this CloudJobExtended.
        The time at which the job was created

        :return: The create_time of this CloudJobExtended.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """
        Sets the create_time of this CloudJobExtended.
        The time at which the job was created

        :param create_time: The create_time of this CloudJobExtended.
        :type: int
        """
        
        self._create_time = create_time

    @property
    def description(self):
        """
        Gets the description of this CloudJobExtended.
        A brief description of the job contents

        :return: The description of this CloudJobExtended.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CloudJobExtended.
        A brief description of the job contents

        :param description: The description of this CloudJobExtended.
        :type: str
        """
        
        self._description = description

    @property
    def effective_state(self):
        """
        Gets the effective_state of this CloudJobExtended.
        The effective state of the job (e.g,. the combination of operation_state and job_state)

        :return: The effective_state of this CloudJobExtended.
        :rtype: str
        """
        return self._effective_state

    @effective_state.setter
    def effective_state(self, effective_state):
        """
        Sets the effective_state of this CloudJobExtended.
        The effective state of the job (e.g,. the combination of operation_state and job_state)

        :param effective_state: The effective_state of this CloudJobExtended.
        :type: str
        """
        allowed_values = ["running", "paused", "canceled", "completed", "failed"]
        if effective_state not in allowed_values:
            raise ValueError(
                "Invalid value for `effective_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._effective_state = effective_state

    @property
    def files(self):
        """
        Gets the files of this CloudJobExtended.
        The files and filters addressed by this job

        :return: The files of this CloudJobExtended.
        :rtype: CloudJobFiles
        """
        return self._files

    @files.setter
    def files(self, files):
        """
        Sets the files of this CloudJobExtended.
        The files and filters addressed by this job

        :param files: The files of this CloudJobExtended.
        :type: CloudJobFiles
        """
        
        self._files = files

    @property
    def id(self):
        """
        Gets the id of this CloudJobExtended.
        The job's ID

        :return: The id of this CloudJobExtended.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CloudJobExtended.
        The job's ID

        :param id: The id of this CloudJobExtended.
        :type: int
        """
        
        self._id = id

    @property
    def job_engine_job(self):
        """
        Gets the job_engine_job of this CloudJobExtended.
        Information about the related job engine job if there is one

        :return: The job_engine_job of this CloudJobExtended.
        :rtype: CloudJobJobEngineJob
        """
        return self._job_engine_job

    @job_engine_job.setter
    def job_engine_job(self, job_engine_job):
        """
        Sets the job_engine_job of this CloudJobExtended.
        Information about the related job engine job if there is one

        :param job_engine_job: The job_engine_job of this CloudJobExtended.
        :type: CloudJobJobEngineJob
        """
        
        self._job_engine_job = job_engine_job

    @property
    def job_state(self):
        """
        Gets the job_state of this CloudJobExtended.
        The current state of the job

        :return: The job_state of this CloudJobExtended.
        :rtype: str
        """
        return self._job_state

    @job_state.setter
    def job_state(self, job_state):
        """
        Sets the job_state of this CloudJobExtended.
        The current state of the job

        :param job_state: The job_state of this CloudJobExtended.
        :type: str
        """
        allowed_values = ["running", "paused", "canceled", "completed", "failed"]
        if job_state not in allowed_values:
            raise ValueError(
                "Invalid value for `job_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._job_state = job_state

    @property
    def operation_state(self):
        """
        Gets the operation_state of this CloudJobExtended.
        The current state of the operation associated with the job

        :return: The operation_state of this CloudJobExtended.
        :rtype: str
        """
        return self._operation_state

    @operation_state.setter
    def operation_state(self, operation_state):
        """
        Sets the operation_state of this CloudJobExtended.
        The current state of the operation associated with the job

        :param operation_state: The operation_state of this CloudJobExtended.
        :type: str
        """
        allowed_values = ["running", "paused"]
        if operation_state not in allowed_values:
            raise ValueError(
                "Invalid value for `operation_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._operation_state = operation_state

    @property
    def state_change_time(self):
        """
        Gets the state_change_time of this CloudJobExtended.
        The last time at which the job state changed

        :return: The state_change_time of this CloudJobExtended.
        :rtype: int
        """
        return self._state_change_time

    @state_change_time.setter
    def state_change_time(self, state_change_time):
        """
        Sets the state_change_time of this CloudJobExtended.
        The last time at which the job state changed

        :param state_change_time: The state_change_time of this CloudJobExtended.
        :type: int
        """
        
        self._state_change_time = state_change_time

    @property
    def type(self):
        """
        Gets the type of this CloudJobExtended.
        The type of cloud action to be performed by this job.

        :return: The type of this CloudJobExtended.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CloudJobExtended.
        The type of cloud action to be performed by this job.

        :param type: The type of this CloudJobExtended.
        :type: str
        """
        allowed_values = ["archive", "recall", "local-garbage-collection", "cloud-garbage-collection", "cache-writeback", "cache-on-access", "cache-invalidation", "restore-coi"]
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type`, must be one of {0}"
                .format(allowed_values)
            )

        self._type = type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
