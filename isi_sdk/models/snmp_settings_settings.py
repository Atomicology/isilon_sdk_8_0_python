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


class SnmpSettingsSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        SnmpSettingsSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'read_only_community': 'str',
            'service': 'bool',
            'snmp_v1_v2c_access': 'bool',
            'snmp_v3_access': 'bool',
            'snmp_v3_read_only_user': 'str',
            'system_contact': 'str',
            'system_location': 'str'
        }

        self.attribute_map = {
            'read_only_community': 'read_only_community',
            'service': 'service',
            'snmp_v1_v2c_access': 'snmp_v1_v2c_access',
            'snmp_v3_access': 'snmp_v3_access',
            'snmp_v3_read_only_user': 'snmp_v3_read_only_user',
            'system_contact': 'system_contact',
            'system_location': 'system_location'
        }

        self._read_only_community = None
        self._service = None
        self._snmp_v1_v2c_access = None
        self._snmp_v3_access = None
        self._snmp_v3_read_only_user = None
        self._system_contact = None
        self._system_location = None

    @property
    def read_only_community(self):
        """
        Gets the read_only_community of this SnmpSettingsSettings.
        The read-only community name.  @DEFAULT reverts this field to its default value.

        :return: The read_only_community of this SnmpSettingsSettings.
        :rtype: str
        """
        return self._read_only_community

    @read_only_community.setter
    def read_only_community(self, read_only_community):
        """
        Sets the read_only_community of this SnmpSettingsSettings.
        The read-only community name.  @DEFAULT reverts this field to its default value.

        :param read_only_community: The read_only_community of this SnmpSettingsSettings.
        :type: str
        """
        
        if not read_only_community:
            raise ValueError("Invalid value for `read_only_community`, must not be `None`")
        if len(read_only_community) < 1: 
            raise ValueError("Invalid value for `read_only_community`, length must be greater than or equal to `1`")

        self._read_only_community = read_only_community

    @property
    def service(self):
        """
        Gets the service of this SnmpSettingsSettings.
        Whether the SNMP service is enabled.

        :return: The service of this SnmpSettingsSettings.
        :rtype: bool
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this SnmpSettingsSettings.
        Whether the SNMP service is enabled.

        :param service: The service of this SnmpSettingsSettings.
        :type: bool
        """
        
        self._service = service

    @property
    def snmp_v1_v2c_access(self):
        """
        Gets the snmp_v1_v2c_access of this SnmpSettingsSettings.
        Whether SNMP v1 and v2c protocols are enabled.  @DEFAULT reverts this field to its default value.

        :return: The snmp_v1_v2c_access of this SnmpSettingsSettings.
        :rtype: bool
        """
        return self._snmp_v1_v2c_access

    @snmp_v1_v2c_access.setter
    def snmp_v1_v2c_access(self, snmp_v1_v2c_access):
        """
        Sets the snmp_v1_v2c_access of this SnmpSettingsSettings.
        Whether SNMP v1 and v2c protocols are enabled.  @DEFAULT reverts this field to its default value.

        :param snmp_v1_v2c_access: The snmp_v1_v2c_access of this SnmpSettingsSettings.
        :type: bool
        """
        
        self._snmp_v1_v2c_access = snmp_v1_v2c_access

    @property
    def snmp_v3_access(self):
        """
        Gets the snmp_v3_access of this SnmpSettingsSettings.
        Whether SNMP v3 is enabled.  @DEFAULT reverts this field to its default value.

        :return: The snmp_v3_access of this SnmpSettingsSettings.
        :rtype: bool
        """
        return self._snmp_v3_access

    @snmp_v3_access.setter
    def snmp_v3_access(self, snmp_v3_access):
        """
        Sets the snmp_v3_access of this SnmpSettingsSettings.
        Whether SNMP v3 is enabled.  @DEFAULT reverts this field to its default value.

        :param snmp_v3_access: The snmp_v3_access of this SnmpSettingsSettings.
        :type: bool
        """
        
        self._snmp_v3_access = snmp_v3_access

    @property
    def snmp_v3_read_only_user(self):
        """
        Gets the snmp_v3_read_only_user of this SnmpSettingsSettings.
        The read-only user for SNMP v3 read requests.  @DEFAULT reverts this field to its default value.

        :return: The snmp_v3_read_only_user of this SnmpSettingsSettings.
        :rtype: str
        """
        return self._snmp_v3_read_only_user

    @snmp_v3_read_only_user.setter
    def snmp_v3_read_only_user(self, snmp_v3_read_only_user):
        """
        Sets the snmp_v3_read_only_user of this SnmpSettingsSettings.
        The read-only user for SNMP v3 read requests.  @DEFAULT reverts this field to its default value.

        :param snmp_v3_read_only_user: The snmp_v3_read_only_user of this SnmpSettingsSettings.
        :type: str
        """
        
        if not snmp_v3_read_only_user:
            raise ValueError("Invalid value for `snmp_v3_read_only_user`, must not be `None`")
        if len(snmp_v3_read_only_user) < 1: 
            raise ValueError("Invalid value for `snmp_v3_read_only_user`, length must be greater than or equal to `1`")

        self._snmp_v3_read_only_user = snmp_v3_read_only_user

    @property
    def system_contact(self):
        """
        Gets the system_contact of this SnmpSettingsSettings.
        Contact information for the system owner.  This must be a valid email address.  @DEFAULT reverts this field to its default value.

        :return: The system_contact of this SnmpSettingsSettings.
        :rtype: str
        """
        return self._system_contact

    @system_contact.setter
    def system_contact(self, system_contact):
        """
        Sets the system_contact of this SnmpSettingsSettings.
        Contact information for the system owner.  This must be a valid email address.  @DEFAULT reverts this field to its default value.

        :param system_contact: The system_contact of this SnmpSettingsSettings.
        :type: str
        """
        
        if not system_contact:
            raise ValueError("Invalid value for `system_contact`, must not be `None`")
        if len(system_contact) < 1: 
            raise ValueError("Invalid value for `system_contact`, length must be greater than or equal to `1`")
        if not re.search('^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$', system_contact): 
            raise ValueError("Invalid value for `system_contact`, must be a follow pattern or equal to `/^[a-z0-9._%+-]+@[a-z0-9.-]+\\.[a-z]{2,4}$/`")

        self._system_contact = system_contact

    @property
    def system_location(self):
        """
        Gets the system_location of this SnmpSettingsSettings.
        A location name for the SNMP system.  @DEFAULT reverts this field to its default value.

        :return: The system_location of this SnmpSettingsSettings.
        :rtype: str
        """
        return self._system_location

    @system_location.setter
    def system_location(self, system_location):
        """
        Sets the system_location of this SnmpSettingsSettings.
        A location name for the SNMP system.  @DEFAULT reverts this field to its default value.

        :param system_location: The system_location of this SnmpSettingsSettings.
        :type: str
        """
        
        if not system_location:
            raise ValueError("Invalid value for `system_location`, must not be `None`")
        if len(system_location) < 1: 
            raise ValueError("Invalid value for `system_location`, length must be greater than or equal to `1`")

        self._system_location = system_location

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
