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


class AntivirusQuarantine(object):
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
        'file': 'str',
        'last_istag': 'str',
        'last_scan': 'int',
        'quarantined': 'bool',
        'scan_result': 'str',
        'scan_status': 'str'
    }

    attribute_map = {
        'file': 'file',
        'last_istag': 'last_istag',
        'last_scan': 'last_scan',
        'quarantined': 'quarantined',
        'scan_result': 'scan_result',
        'scan_status': 'scan_status'
    }

    def __init__(self, file=None, last_istag=None, last_scan=None, quarantined=None, scan_result=None, scan_status=None):  # noqa: E501
        """AntivirusQuarantine - a model defined in Swagger"""  # noqa: E501

        self._file = None
        self._last_istag = None
        self._last_scan = None
        self._quarantined = None
        self._scan_result = None
        self._scan_status = None
        self.discriminator = None

        self.file = file
        if last_istag is not None:
            self.last_istag = last_istag
        if last_scan is not None:
            self.last_scan = last_scan
        self.quarantined = quarantined
        self.scan_result = scan_result
        self.scan_status = scan_status

    @property
    def file(self):
        """Gets the file of this AntivirusQuarantine.  # noqa: E501

        Path of this file, starting with /ifs.  # noqa: E501

        :return: The file of this AntivirusQuarantine.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this AntivirusQuarantine.

        Path of this file, starting with /ifs.  # noqa: E501

        :param file: The file of this AntivirusQuarantine.  # noqa: E501
        :type: str
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def last_istag(self):
        """Gets the last_istag of this AntivirusQuarantine.  # noqa: E501

        The ICAP Service Tag (ISTag) recorded for this file during the last scan, or null if no tag was recorded.  For more information about ISTags, see https://tools.ietf.org/html/rfc3507.  # noqa: E501

        :return: The last_istag of this AntivirusQuarantine.  # noqa: E501
        :rtype: str
        """
        return self._last_istag

    @last_istag.setter
    def last_istag(self, last_istag):
        """Sets the last_istag of this AntivirusQuarantine.

        The ICAP Service Tag (ISTag) recorded for this file during the last scan, or null if no tag was recorded.  For more information about ISTags, see https://tools.ietf.org/html/rfc3507.  # noqa: E501

        :param last_istag: The last_istag of this AntivirusQuarantine.  # noqa: E501
        :type: str
        """

        self._last_istag = last_istag

    @property
    def last_scan(self):
        """Gets the last_scan of this AntivirusQuarantine.  # noqa: E501

        The date and time this file was last scanned for viruses, as a UNIX timestamp.  If null, the file has never been scanned.  # noqa: E501

        :return: The last_scan of this AntivirusQuarantine.  # noqa: E501
        :rtype: int
        """
        return self._last_scan

    @last_scan.setter
    def last_scan(self, last_scan):
        """Sets the last_scan of this AntivirusQuarantine.

        The date and time this file was last scanned for viruses, as a UNIX timestamp.  If null, the file has never been scanned.  # noqa: E501

        :param last_scan: The last_scan of this AntivirusQuarantine.  # noqa: E501
        :type: int
        """

        self._last_scan = last_scan

    @property
    def quarantined(self):
        """Gets the quarantined of this AntivirusQuarantine.  # noqa: E501

        If true, this file is quarantined.  If false, the file is not quarantined.  # noqa: E501

        :return: The quarantined of this AntivirusQuarantine.  # noqa: E501
        :rtype: bool
        """
        return self._quarantined

    @quarantined.setter
    def quarantined(self, quarantined):
        """Sets the quarantined of this AntivirusQuarantine.

        If true, this file is quarantined.  If false, the file is not quarantined.  # noqa: E501

        :param quarantined: The quarantined of this AntivirusQuarantine.  # noqa: E501
        :type: bool
        """
        if quarantined is None:
            raise ValueError("Invalid value for `quarantined`, must not be `None`")  # noqa: E501

        self._quarantined = quarantined

    @property
    def scan_result(self):
        """Gets the scan_result of this AntivirusQuarantine.  # noqa: E501

        The result of the last scan on this file.  This string is usually one of: never_scanned, clean, quarantined, repaired, truncated, infected_no_action_taken, skipped_per_settings.  However, a longer string starting with 'unknown_status' and describing the details can also appear in uncommon edge cases.  # noqa: E501

        :return: The scan_result of this AntivirusQuarantine.  # noqa: E501
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        """Sets the scan_result of this AntivirusQuarantine.

        The result of the last scan on this file.  This string is usually one of: never_scanned, clean, quarantined, repaired, truncated, infected_no_action_taken, skipped_per_settings.  However, a longer string starting with 'unknown_status' and describing the details can also appear in uncommon edge cases.  # noqa: E501

        :param scan_result: The scan_result of this AntivirusQuarantine.  # noqa: E501
        :type: str
        """
        if scan_result is None:
            raise ValueError("Invalid value for `scan_result`, must not be `None`")  # noqa: E501

        self._scan_result = scan_result

    @property
    def scan_status(self):
        """Gets the scan_status of this AntivirusQuarantine.  # noqa: E501

        The scanning status of this file.  If 'current', the file was scanned with the most up-to-date virus defintions.  If 'not_current', it has either not been scanned, been modified since the last scan, or the virus definitions are not current.  # noqa: E501

        :return: The scan_status of this AntivirusQuarantine.  # noqa: E501
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this AntivirusQuarantine.

        The scanning status of this file.  If 'current', the file was scanned with the most up-to-date virus defintions.  If 'not_current', it has either not been scanned, been modified since the last scan, or the virus definitions are not current.  # noqa: E501

        :param scan_status: The scan_status of this AntivirusQuarantine.  # noqa: E501
        :type: str
        """
        if scan_status is None:
            raise ValueError("Invalid value for `scan_status`, must not be `None`")  # noqa: E501
        allowed_values = ["current", "not_current"]  # noqa: E501
        if scan_status not in allowed_values:
            raise ValueError(
                "Invalid value for `scan_status` ({0}), must be one of {1}"  # noqa: E501
                .format(scan_status, allowed_values)
            )

        self._scan_status = scan_status

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
        if not isinstance(other, AntivirusQuarantine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
