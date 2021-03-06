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


class RolePrivileges(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        RolePrivileges - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'privileges': 'list[AuthIdNtokenPrivilegeItem]',
            'resume': 'str'
        }

        self.attribute_map = {
            'privileges': 'privileges',
            'resume': 'resume'
        }

        self._privileges = None
        self._resume = None

    @property
    def privileges(self):
        """
        Gets the privileges of this RolePrivileges.


        :return: The privileges of this RolePrivileges.
        :rtype: list[AuthIdNtokenPrivilegeItem]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """
        Sets the privileges of this RolePrivileges.


        :param privileges: The privileges of this RolePrivileges.
        :type: list[AuthIdNtokenPrivilegeItem]
        """
        
        self._privileges = privileges

    @property
    def resume(self):
        """
        Gets the resume of this RolePrivileges.
        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).

        :return: The resume of this RolePrivileges.
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """
        Sets the resume of this RolePrivileges.
        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).

        :param resume: The resume of this RolePrivileges.
        :type: str
        """
        
        self._resume = resume

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

