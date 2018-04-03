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


class SummarySystemSystemItem(object):
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
        'cpu': 'float',
        'disk_in': 'float',
        'disk_out': 'float',
        'ftp': 'float',
        'hdfs': 'float',
        'http': 'float',
        'iscsi': 'float',
        'net_in': 'float',
        'net_out': 'float',
        'nfs': 'float',
        'node': 'str',
        'smb': 'float',
        'time': 'int',
        'total': 'float'
    }

    attribute_map = {
        'cpu': 'cpu',
        'disk_in': 'disk_in',
        'disk_out': 'disk_out',
        'ftp': 'ftp',
        'hdfs': 'hdfs',
        'http': 'http',
        'iscsi': 'iscsi',
        'net_in': 'net_in',
        'net_out': 'net_out',
        'nfs': 'nfs',
        'node': 'node',
        'smb': 'smb',
        'time': 'time',
        'total': 'total'
    }

    def __init__(self, cpu=None, disk_in=None, disk_out=None, ftp=None, hdfs=None, http=None, iscsi=None, net_in=None, net_out=None, nfs=None, node=None, smb=None, time=None, total=None):  # noqa: E501
        """SummarySystemSystemItem - a model defined in Swagger"""  # noqa: E501

        self._cpu = None
        self._disk_in = None
        self._disk_out = None
        self._ftp = None
        self._hdfs = None
        self._http = None
        self._iscsi = None
        self._net_in = None
        self._net_out = None
        self._nfs = None
        self._node = None
        self._smb = None
        self._time = None
        self._total = None
        self.discriminator = None

        self.cpu = cpu
        self.disk_in = disk_in
        self.disk_out = disk_out
        self.ftp = ftp
        self.hdfs = hdfs
        self.http = http
        if iscsi is not None:
            self.iscsi = iscsi
        self.net_in = net_in
        self.net_out = net_out
        self.nfs = nfs
        self.node = node
        self.smb = smb
        self.time = time
        self.total = total

    @property
    def cpu(self):
        """Gets the cpu of this SummarySystemSystemItem.  # noqa: E501

        The percentage CPU utilization.  # noqa: E501

        :return: The cpu of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._cpu

    @cpu.setter
    def cpu(self, cpu):
        """Sets the cpu of this SummarySystemSystemItem.

        The percentage CPU utilization.  # noqa: E501

        :param cpu: The cpu of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if cpu is None:
            raise ValueError("Invalid value for `cpu`, must not be `None`")  # noqa: E501

        self._cpu = cpu

    @property
    def disk_in(self):
        """Gets the disk_in of this SummarySystemSystemItem.  # noqa: E501

        Traffic to disk (in bytes/sec).  # noqa: E501

        :return: The disk_in of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._disk_in

    @disk_in.setter
    def disk_in(self, disk_in):
        """Sets the disk_in of this SummarySystemSystemItem.

        Traffic to disk (in bytes/sec).  # noqa: E501

        :param disk_in: The disk_in of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if disk_in is None:
            raise ValueError("Invalid value for `disk_in`, must not be `None`")  # noqa: E501

        self._disk_in = disk_in

    @property
    def disk_out(self):
        """Gets the disk_out of this SummarySystemSystemItem.  # noqa: E501

        Traffic from disk (in bytes/sec).  # noqa: E501

        :return: The disk_out of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._disk_out

    @disk_out.setter
    def disk_out(self, disk_out):
        """Sets the disk_out of this SummarySystemSystemItem.

        Traffic from disk (in bytes/sec).  # noqa: E501

        :param disk_out: The disk_out of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if disk_out is None:
            raise ValueError("Invalid value for `disk_out`, must not be `None`")  # noqa: E501

        self._disk_out = disk_out

    @property
    def ftp(self):
        """Gets the ftp of this SummarySystemSystemItem.  # noqa: E501

        The total throughput (in bytes/sec) for FTP operations.  # noqa: E501

        :return: The ftp of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._ftp

    @ftp.setter
    def ftp(self, ftp):
        """Sets the ftp of this SummarySystemSystemItem.

        The total throughput (in bytes/sec) for FTP operations.  # noqa: E501

        :param ftp: The ftp of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if ftp is None:
            raise ValueError("Invalid value for `ftp`, must not be `None`")  # noqa: E501

        self._ftp = ftp

    @property
    def hdfs(self):
        """Gets the hdfs of this SummarySystemSystemItem.  # noqa: E501

        The total throughput (in bytes/second) for HDFS operations.  # noqa: E501

        :return: The hdfs of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._hdfs

    @hdfs.setter
    def hdfs(self, hdfs):
        """Sets the hdfs of this SummarySystemSystemItem.

        The total throughput (in bytes/second) for HDFS operations.  # noqa: E501

        :param hdfs: The hdfs of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if hdfs is None:
            raise ValueError("Invalid value for `hdfs`, must not be `None`")  # noqa: E501

        self._hdfs = hdfs

    @property
    def http(self):
        """Gets the http of this SummarySystemSystemItem.  # noqa: E501

        The total throughput (in bytes/sec) for HTTP operations.  # noqa: E501

        :return: The http of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._http

    @http.setter
    def http(self, http):
        """Sets the http of this SummarySystemSystemItem.

        The total throughput (in bytes/sec) for HTTP operations.  # noqa: E501

        :param http: The http of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if http is None:
            raise ValueError("Invalid value for `http`, must not be `None`")  # noqa: E501

        self._http = http

    @property
    def iscsi(self):
        """Gets the iscsi of this SummarySystemSystemItem.  # noqa: E501

        The total throughput (in bytes/sec) for ISCSI operations.  # noqa: E501

        :return: The iscsi of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """Sets the iscsi of this SummarySystemSystemItem.

        The total throughput (in bytes/sec) for ISCSI operations.  # noqa: E501

        :param iscsi: The iscsi of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """

        self._iscsi = iscsi

    @property
    def net_in(self):
        """Gets the net_in of this SummarySystemSystemItem.  # noqa: E501

        Incoming network traffic (in bytes/sec) for all operations.  # noqa: E501

        :return: The net_in of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._net_in

    @net_in.setter
    def net_in(self, net_in):
        """Sets the net_in of this SummarySystemSystemItem.

        Incoming network traffic (in bytes/sec) for all operations.  # noqa: E501

        :param net_in: The net_in of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if net_in is None:
            raise ValueError("Invalid value for `net_in`, must not be `None`")  # noqa: E501

        self._net_in = net_in

    @property
    def net_out(self):
        """Gets the net_out of this SummarySystemSystemItem.  # noqa: E501

        Outgoing network traffic (in bytes/sec) for all operations.  # noqa: E501

        :return: The net_out of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._net_out

    @net_out.setter
    def net_out(self, net_out):
        """Sets the net_out of this SummarySystemSystemItem.

        Outgoing network traffic (in bytes/sec) for all operations.  # noqa: E501

        :param net_out: The net_out of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if net_out is None:
            raise ValueError("Invalid value for `net_out`, must not be `None`")  # noqa: E501

        self._net_out = net_out

    @property
    def nfs(self):
        """Gets the nfs of this SummarySystemSystemItem.  # noqa: E501

        The total throughput (in bytes/sec) for NFS (NFS3 & NFS4) operations.  # noqa: E501

        :return: The nfs of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._nfs

    @nfs.setter
    def nfs(self, nfs):
        """Sets the nfs of this SummarySystemSystemItem.

        The total throughput (in bytes/sec) for NFS (NFS3 & NFS4) operations.  # noqa: E501

        :param nfs: The nfs of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if nfs is None:
            raise ValueError("Invalid value for `nfs`, must not be `None`")  # noqa: E501

        self._nfs = nfs

    @property
    def node(self):
        """Gets the node of this SummarySystemSystemItem.  # noqa: E501

        Node ID/LNN, 'All' for cluster.  # noqa: E501

        :return: The node of this SummarySystemSystemItem.  # noqa: E501
        :rtype: str
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this SummarySystemSystemItem.

        Node ID/LNN, 'All' for cluster.  # noqa: E501

        :param node: The node of this SummarySystemSystemItem.  # noqa: E501
        :type: str
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def smb(self):
        """Gets the smb of this SummarySystemSystemItem.  # noqa: E501

        The total throughput (in bytes/sec) for SMB (SMB1 & SMB2) operations.  # noqa: E501

        :return: The smb of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._smb

    @smb.setter
    def smb(self, smb):
        """Sets the smb of this SummarySystemSystemItem.

        The total throughput (in bytes/sec) for SMB (SMB1 & SMB2) operations.  # noqa: E501

        :param smb: The smb of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if smb is None:
            raise ValueError("Invalid value for `smb`, must not be `None`")  # noqa: E501

        self._smb = smb

    @property
    def time(self):
        """Gets the time of this SummarySystemSystemItem.  # noqa: E501

        Unix Epoch time in seconds of the request.  # noqa: E501

        :return: The time of this SummarySystemSystemItem.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this SummarySystemSystemItem.

        Unix Epoch time in seconds of the request.  # noqa: E501

        :param time: The time of this SummarySystemSystemItem.  # noqa: E501
        :type: int
        """
        if time is None:
            raise ValueError("Invalid value for `time`, must not be `None`")  # noqa: E501

        self._time = time

    @property
    def total(self):
        """Gets the total of this SummarySystemSystemItem.  # noqa: E501

        The total throughput (in bytes/sec) for all protocols listed.  # noqa: E501

        :return: The total of this SummarySystemSystemItem.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SummarySystemSystemItem.

        The total throughput (in bytes/sec) for all protocols listed.  # noqa: E501

        :param total: The total of this SummarySystemSystemItem.  # noqa: E501
        :type: float
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if not isinstance(other, SummarySystemSystemItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
