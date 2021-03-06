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


class NodeStatusNodeBatterystatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NodeStatusNodeBatterystatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'last_test_time1': 'str',
            'last_test_time2': 'str',
            'next_test_time1': 'str',
            'next_test_time2': 'str',
            'present': 'bool',
            'result1': 'str',
            'result2': 'str',
            'status1': 'str',
            'status2': 'str',
            'supported': 'bool'
        }

        self.attribute_map = {
            'last_test_time1': 'last_test_time1',
            'last_test_time2': 'last_test_time2',
            'next_test_time1': 'next_test_time1',
            'next_test_time2': 'next_test_time2',
            'present': 'present',
            'result1': 'result1',
            'result2': 'result2',
            'status1': 'status1',
            'status2': 'status2',
            'supported': 'supported'
        }

        self._last_test_time1 = None
        self._last_test_time2 = None
        self._next_test_time1 = None
        self._next_test_time2 = None
        self._present = None
        self._result1 = None
        self._result2 = None
        self._status1 = None
        self._status2 = None
        self._supported = None

    @property
    def last_test_time1(self):
        """
        Gets the last_test_time1 of this NodeStatusNodeBatterystatus.
        The last battery test time for battery 1.

        :return: The last_test_time1 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._last_test_time1

    @last_test_time1.setter
    def last_test_time1(self, last_test_time1):
        """
        Sets the last_test_time1 of this NodeStatusNodeBatterystatus.
        The last battery test time for battery 1.

        :param last_test_time1: The last_test_time1 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._last_test_time1 = last_test_time1

    @property
    def last_test_time2(self):
        """
        Gets the last_test_time2 of this NodeStatusNodeBatterystatus.
        The last battery test time for battery 2.

        :return: The last_test_time2 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._last_test_time2

    @last_test_time2.setter
    def last_test_time2(self, last_test_time2):
        """
        Sets the last_test_time2 of this NodeStatusNodeBatterystatus.
        The last battery test time for battery 2.

        :param last_test_time2: The last_test_time2 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._last_test_time2 = last_test_time2

    @property
    def next_test_time1(self):
        """
        Gets the next_test_time1 of this NodeStatusNodeBatterystatus.
        The next checkup for battery 1.

        :return: The next_test_time1 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._next_test_time1

    @next_test_time1.setter
    def next_test_time1(self, next_test_time1):
        """
        Sets the next_test_time1 of this NodeStatusNodeBatterystatus.
        The next checkup for battery 1.

        :param next_test_time1: The next_test_time1 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._next_test_time1 = next_test_time1

    @property
    def next_test_time2(self):
        """
        Gets the next_test_time2 of this NodeStatusNodeBatterystatus.
        The next checkup for battery 2.

        :return: The next_test_time2 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._next_test_time2

    @next_test_time2.setter
    def next_test_time2(self, next_test_time2):
        """
        Sets the next_test_time2 of this NodeStatusNodeBatterystatus.
        The next checkup for battery 2.

        :param next_test_time2: The next_test_time2 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._next_test_time2 = next_test_time2

    @property
    def present(self):
        """
        Gets the present of this NodeStatusNodeBatterystatus.
        Node has battery status.

        :return: The present of this NodeStatusNodeBatterystatus.
        :rtype: bool
        """
        return self._present

    @present.setter
    def present(self, present):
        """
        Sets the present of this NodeStatusNodeBatterystatus.
        Node has battery status.

        :param present: The present of this NodeStatusNodeBatterystatus.
        :type: bool
        """
        
        self._present = present

    @property
    def result1(self):
        """
        Gets the result1 of this NodeStatusNodeBatterystatus.
        The result of the last battery test for battery 1.

        :return: The result1 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._result1

    @result1.setter
    def result1(self, result1):
        """
        Sets the result1 of this NodeStatusNodeBatterystatus.
        The result of the last battery test for battery 1.

        :param result1: The result1 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._result1 = result1

    @property
    def result2(self):
        """
        Gets the result2 of this NodeStatusNodeBatterystatus.
        The result of the last battery test for battery 2.

        :return: The result2 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._result2

    @result2.setter
    def result2(self, result2):
        """
        Sets the result2 of this NodeStatusNodeBatterystatus.
        The result of the last battery test for battery 2.

        :param result2: The result2 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._result2 = result2

    @property
    def status1(self):
        """
        Gets the status1 of this NodeStatusNodeBatterystatus.
        The status of battery 1.

        :return: The status1 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._status1

    @status1.setter
    def status1(self, status1):
        """
        Sets the status1 of this NodeStatusNodeBatterystatus.
        The status of battery 1.

        :param status1: The status1 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._status1 = status1

    @property
    def status2(self):
        """
        Gets the status2 of this NodeStatusNodeBatterystatus.
        The status of battery 2.

        :return: The status2 of this NodeStatusNodeBatterystatus.
        :rtype: str
        """
        return self._status2

    @status2.setter
    def status2(self, status2):
        """
        Sets the status2 of this NodeStatusNodeBatterystatus.
        The status of battery 2.

        :param status2: The status2 of this NodeStatusNodeBatterystatus.
        :type: str
        """
        
        self._status2 = status2

    @property
    def supported(self):
        """
        Gets the supported of this NodeStatusNodeBatterystatus.
        Node supports battery status.

        :return: The supported of this NodeStatusNodeBatterystatus.
        :rtype: bool
        """
        return self._supported

    @supported.setter
    def supported(self, supported):
        """
        Sets the supported of this NodeStatusNodeBatterystatus.
        Node supports battery status.

        :param supported: The supported of this NodeStatusNodeBatterystatus.
        :type: bool
        """
        
        self._supported = supported

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

