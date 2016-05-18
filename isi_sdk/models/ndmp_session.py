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


class NdmpSession(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NdmpSession - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'data_bytes_transferred': 'int',
            'data_state': 'str',
            'dest_path': 'str',
            'dma_ip_addr': 'str',
            'elapsed_time': 'int',
            'id': 'str',
            'mover_bytes_transferred': 'int',
            'mover_state': 'str',
            'operation': 'str',
            'remote_ip_addr': 'str',
            'scsi_device': 'str',
            'session': 'str',
            'source_path': 'str',
            'start_time': 'int',
            'tape_device': 'str',
            'tape_open_mode': 'str',
            'throughput': 'int'
        }

        self.attribute_map = {
            'data_bytes_transferred': 'data_bytes_transferred',
            'data_state': 'data_state',
            'dest_path': 'dest_path',
            'dma_ip_addr': 'dma_ip_addr',
            'elapsed_time': 'elapsed_time',
            'id': 'id',
            'mover_bytes_transferred': 'mover_bytes_transferred',
            'mover_state': 'mover_state',
            'operation': 'operation',
            'remote_ip_addr': 'remote_ip_addr',
            'scsi_device': 'scsi_device',
            'session': 'session',
            'source_path': 'source_path',
            'start_time': 'start_time',
            'tape_device': 'tape_device',
            'tape_open_mode': 'tape_open_mode',
            'throughput': 'throughput'
        }

        self._data_bytes_transferred = None
        self._data_state = None
        self._dest_path = None
        self._dma_ip_addr = None
        self._elapsed_time = None
        self._id = None
        self._mover_bytes_transferred = None
        self._mover_state = None
        self._operation = None
        self._remote_ip_addr = None
        self._scsi_device = None
        self._session = None
        self._source_path = None
        self._start_time = None
        self._tape_device = None
        self._tape_open_mode = None
        self._throughput = None

    @property
    def data_bytes_transferred(self):
        """
        Gets the data_bytes_transferred of this NdmpSession.
        Bytes transferred to/from the filesystem

        :return: The data_bytes_transferred of this NdmpSession.
        :rtype: int
        """
        return self._data_bytes_transferred

    @data_bytes_transferred.setter
    def data_bytes_transferred(self, data_bytes_transferred):
        """
        Sets the data_bytes_transferred of this NdmpSession.
        Bytes transferred to/from the filesystem

        :param data_bytes_transferred: The data_bytes_transferred of this NdmpSession.
        :type: int
        """
        
        self._data_bytes_transferred = data_bytes_transferred

    @property
    def data_state(self):
        """
        Gets the data_state of this NdmpSession.
        State of the NDMP Data Service

        :return: The data_state of this NdmpSession.
        :rtype: str
        """
        return self._data_state

    @data_state.setter
    def data_state(self, data_state):
        """
        Sets the data_state of this NdmpSession.
        State of the NDMP Data Service

        :param data_state: The data_state of this NdmpSession.
        :type: str
        """
        allowed_values = ["IDLE", "LISTEN", "ACTIVE", "CONNECTED", "HALTED", "INVALID"]
        if data_state not in allowed_values:
            raise ValueError(
                "Invalid value for `data_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._data_state = data_state

    @property
    def dest_path(self):
        """
        Gets the dest_path of this NdmpSession.
        The path being recovered to

        :return: The dest_path of this NdmpSession.
        :rtype: str
        """
        return self._dest_path

    @dest_path.setter
    def dest_path(self, dest_path):
        """
        Sets the dest_path of this NdmpSession.
        The path being recovered to

        :param dest_path: The dest_path of this NdmpSession.
        :type: str
        """
        
        self._dest_path = dest_path

    @property
    def dma_ip_addr(self):
        """
        Gets the dma_ip_addr of this NdmpSession.
        IP address of the DMA

        :return: The dma_ip_addr of this NdmpSession.
        :rtype: str
        """
        return self._dma_ip_addr

    @dma_ip_addr.setter
    def dma_ip_addr(self, dma_ip_addr):
        """
        Sets the dma_ip_addr of this NdmpSession.
        IP address of the DMA

        :param dma_ip_addr: The dma_ip_addr of this NdmpSession.
        :type: str
        """
        
        self._dma_ip_addr = dma_ip_addr

    @property
    def elapsed_time(self):
        """
        Gets the elapsed_time of this NdmpSession.
        Number of seconds elapsed since the backup was started

        :return: The elapsed_time of this NdmpSession.
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """
        Sets the elapsed_time of this NdmpSession.
        Number of seconds elapsed since the backup was started

        :param elapsed_time: The elapsed_time of this NdmpSession.
        :type: int
        """
        
        self._elapsed_time = elapsed_time

    @property
    def id(self):
        """
        Gets the id of this NdmpSession.
        Unique display ID.

        :return: The id of this NdmpSession.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this NdmpSession.
        Unique display ID.

        :param id: The id of this NdmpSession.
        :type: str
        """
        
        self._id = id

    @property
    def mover_bytes_transferred(self):
        """
        Gets the mover_bytes_transferred of this NdmpSession.
        Bytes transferred to/from tape or remote writer

        :return: The mover_bytes_transferred of this NdmpSession.
        :rtype: int
        """
        return self._mover_bytes_transferred

    @mover_bytes_transferred.setter
    def mover_bytes_transferred(self, mover_bytes_transferred):
        """
        Sets the mover_bytes_transferred of this NdmpSession.
        Bytes transferred to/from tape or remote writer

        :param mover_bytes_transferred: The mover_bytes_transferred of this NdmpSession.
        :type: int
        """
        
        self._mover_bytes_transferred = mover_bytes_transferred

    @property
    def mover_state(self):
        """
        Gets the mover_state of this NdmpSession.
        State of the NDMP Mover Service

        :return: The mover_state of this NdmpSession.
        :rtype: str
        """
        return self._mover_state

    @mover_state.setter
    def mover_state(self, mover_state):
        """
        Sets the mover_state of this NdmpSession.
        State of the NDMP Mover Service

        :param mover_state: The mover_state of this NdmpSession.
        :type: str
        """
        allowed_values = ["IDLE", "LISTEN", "ACTIVE", "PAUSED", "HALTED", "INVALID"]
        if mover_state not in allowed_values:
            raise ValueError(
                "Invalid value for `mover_state`, must be one of {0}"
                .format(allowed_values)
            )

        self._mover_state = mover_state

    @property
    def operation(self):
        """
        Gets the operation of this NdmpSession.
        The type of backup session

        :return: The operation of this NdmpSession.
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """
        Sets the operation of this NdmpSession.
        The type of backup session

        :param operation: The operation of this NdmpSession.
        :type: str
        """
        allowed_values = ["None", "Backup", "Recover", "Recover file history"]
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation`, must be one of {0}"
                .format(allowed_values)
            )

        self._operation = operation

    @property
    def remote_ip_addr(self):
        """
        Gets the remote_ip_addr of this NdmpSession.
        IP address of the remote NDMP participant

        :return: The remote_ip_addr of this NdmpSession.
        :rtype: str
        """
        return self._remote_ip_addr

    @remote_ip_addr.setter
    def remote_ip_addr(self, remote_ip_addr):
        """
        Sets the remote_ip_addr of this NdmpSession.
        IP address of the remote NDMP participant

        :param remote_ip_addr: The remote_ip_addr of this NdmpSession.
        :type: str
        """
        
        self._remote_ip_addr = remote_ip_addr

    @property
    def scsi_device(self):
        """
        Gets the scsi_device of this NdmpSession.
        Name of the media changer device used if any

        :return: The scsi_device of this NdmpSession.
        :rtype: str
        """
        return self._scsi_device

    @scsi_device.setter
    def scsi_device(self, scsi_device):
        """
        Sets the scsi_device of this NdmpSession.
        Name of the media changer device used if any

        :param scsi_device: The scsi_device of this NdmpSession.
        :type: str
        """
        
        self._scsi_device = scsi_device

    @property
    def session(self):
        """
        Gets the session of this NdmpSession.
        Session ID in form <lnn>.<pid>.

        :return: The session of this NdmpSession.
        :rtype: str
        """
        return self._session

    @session.setter
    def session(self, session):
        """
        Sets the session of this NdmpSession.
        Session ID in form <lnn>.<pid>.

        :param session: The session of this NdmpSession.
        :type: str
        """
        
        self._session = session

    @property
    def source_path(self):
        """
        Gets the source_path of this NdmpSession.
        The path being backed up

        :return: The source_path of this NdmpSession.
        :rtype: str
        """
        return self._source_path

    @source_path.setter
    def source_path(self, source_path):
        """
        Sets the source_path of this NdmpSession.
        The path being backed up

        :param source_path: The source_path of this NdmpSession.
        :type: str
        """
        
        self._source_path = source_path

    @property
    def start_time(self):
        """
        Gets the start_time of this NdmpSession.
        Time backup was started in seconds since epoch

        :return: The start_time of this NdmpSession.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time of this NdmpSession.
        Time backup was started in seconds since epoch

        :param start_time: The start_time of this NdmpSession.
        :type: int
        """
        
        self._start_time = start_time

    @property
    def tape_device(self):
        """
        Gets the tape_device of this NdmpSession.
        Name of the tape device used if any

        :return: The tape_device of this NdmpSession.
        :rtype: str
        """
        return self._tape_device

    @tape_device.setter
    def tape_device(self, tape_device):
        """
        Sets the tape_device of this NdmpSession.
        Name of the tape device used if any

        :param tape_device: The tape_device of this NdmpSession.
        :type: str
        """
        
        self._tape_device = tape_device

    @property
    def tape_open_mode(self):
        """
        Gets the tape_open_mode of this NdmpSession.
        Describes the mode in which the tape is opened

        :return: The tape_open_mode of this NdmpSession.
        :rtype: str
        """
        return self._tape_open_mode

    @tape_open_mode.setter
    def tape_open_mode(self, tape_open_mode):
        """
        Sets the tape_open_mode of this NdmpSession.
        Describes the mode in which the tape is opened

        :param tape_open_mode: The tape_open_mode of this NdmpSession.
        :type: str
        """
        allowed_values = ["Read", "Read/Write", "Raw", "Invalid"]
        if tape_open_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `tape_open_mode`, must be one of {0}"
                .format(allowed_values)
            )

        self._tape_open_mode = tape_open_mode

    @property
    def throughput(self):
        """
        Gets the throughput of this NdmpSession.
        The throughput in MB/s

        :return: The throughput of this NdmpSession.
        :rtype: int
        """
        return self._throughput

    @throughput.setter
    def throughput(self, throughput):
        """
        Sets the throughput of this NdmpSession.
        The throughput in MB/s

        :param throughput: The throughput of this NdmpSession.
        :type: int
        """
        
        self._throughput = throughput

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
