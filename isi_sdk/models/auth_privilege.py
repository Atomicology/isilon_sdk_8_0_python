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


class AuthPrivilege(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        AuthPrivilege - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'category': 'str',
            'description': 'str',
            'id': 'str',
            'name': 'str',
            'read_write': 'bool'
        }

        self.attribute_map = {
            'category': 'category',
            'description': 'description',
            'id': 'id',
            'name': 'name',
            'read_write': 'read_write'
        }

        self._category = None
        self._description = None
        self._id = None
        self._name = None
        self._read_write = None

    @property
    def category(self):
        """
        Gets the category of this AuthPrivilege.
        Specifies the general categorization of the privilege.

        :return: The category of this AuthPrivilege.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this AuthPrivilege.
        Specifies the general categorization of the privilege.

        :param category: The category of this AuthPrivilege.
        :type: str
        """
        
        self._category = category

    @property
    def description(self):
        """
        Gets the description of this AuthPrivilege.
        Specifies a short description of the privilege.

        :return: The description of this AuthPrivilege.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this AuthPrivilege.
        Specifies a short description of the privilege.

        :param description: The description of this AuthPrivilege.
        :type: str
        """
        
        self._description = description

    @property
    def id(self):
        """
        Gets the id of this AuthPrivilege.
        Specifies the ID of the privilege.

        :return: The id of this AuthPrivilege.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AuthPrivilege.
        Specifies the ID of the privilege.

        :param id: The id of this AuthPrivilege.
        :type: str
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this AuthPrivilege.
        Specifies the name of the privilege.

        :return: The name of this AuthPrivilege.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AuthPrivilege.
        Specifies the name of the privilege.

        :param name: The name of this AuthPrivilege.
        :type: str
        """
        
        self._name = name

    @property
    def read_write(self):
        """
        Gets the read_write of this AuthPrivilege.
        True, if the privilege is read-write.

        :return: The read_write of this AuthPrivilege.
        :rtype: bool
        """
        return self._read_write

    @read_write.setter
    def read_write(self, read_write):
        """
        Sets the read_write of this AuthPrivilege.
        True, if the privilege is read-write.

        :param read_write: The read_write of this AuthPrivilege.
        :type: bool
        """
        
        self._read_write = read_write

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

