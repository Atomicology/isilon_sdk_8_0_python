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


class NdmpDiagnosticsDiagnostics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        NdmpDiagnosticsDiagnostics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'diag_level': 'int',
            'protocol_version': 'int',
            'trace_level': 'str'
        }

        self.attribute_map = {
            'diag_level': 'diag_level',
            'protocol_version': 'protocol_version',
            'trace_level': 'trace_level'
        }

        self._diag_level = None
        self._protocol_version = None
        self._trace_level = None

    @property
    def diag_level(self):
        """
        Gets the diag_level of this NdmpDiagnosticsDiagnostics.
        Diagnostics level for ndmp.

        :return: The diag_level of this NdmpDiagnosticsDiagnostics.
        :rtype: int
        """
        return self._diag_level

    @diag_level.setter
    def diag_level(self, diag_level):
        """
        Sets the diag_level of this NdmpDiagnosticsDiagnostics.
        Diagnostics level for ndmp.

        :param diag_level: The diag_level of this NdmpDiagnosticsDiagnostics.
        :type: int
        """
        
        self._diag_level = diag_level

    @property
    def protocol_version(self):
        """
        Gets the protocol_version of this NdmpDiagnosticsDiagnostics.
        The version of the ndmp protocol.

        :return: The protocol_version of this NdmpDiagnosticsDiagnostics.
        :rtype: int
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """
        Sets the protocol_version of this NdmpDiagnosticsDiagnostics.
        The version of the ndmp protocol.

        :param protocol_version: The protocol_version of this NdmpDiagnosticsDiagnostics.
        :type: int
        """
        
        self._protocol_version = protocol_version

    @property
    def trace_level(self):
        """
        Gets the trace_level of this NdmpDiagnosticsDiagnostics.
        Trace level for ndmp.

        :return: The trace_level of this NdmpDiagnosticsDiagnostics.
        :rtype: str
        """
        return self._trace_level

    @trace_level.setter
    def trace_level(self, trace_level):
        """
        Sets the trace_level of this NdmpDiagnosticsDiagnostics.
        Trace level for ndmp.

        :param trace_level: The trace_level of this NdmpDiagnosticsDiagnostics.
        :type: str
        """
        allowed_values = ["none", "standard", "include-file-history", "log-file-history"]
        if trace_level not in allowed_values:
            raise ValueError(
                "Invalid value for `trace_level`, must be one of {0}"
                .format(allowed_values)
            )

        self._trace_level = trace_level

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
