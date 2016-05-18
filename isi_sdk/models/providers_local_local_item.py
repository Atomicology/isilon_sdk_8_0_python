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


class ProvidersLocalLocalItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProvidersLocalLocalItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'authentication': 'bool',
            'create_home_directory': 'bool',
            'home_directory_template': 'str',
            'id': 'str',
            'lockout_duration': 'int',
            'lockout_threshold': 'int',
            'lockout_window': 'int',
            'login_shell': 'str',
            'machine_name': 'str',
            'max_password_age': 'int',
            'min_password_age': 'int',
            'min_password_length': 'int',
            'name': 'str',
            'password_complexity': 'list[str]',
            'password_history_length': 'int',
            'password_prompt_time': 'int',
            'status': 'str',
            'system': 'bool'
        }

        self.attribute_map = {
            'authentication': 'authentication',
            'create_home_directory': 'create_home_directory',
            'home_directory_template': 'home_directory_template',
            'id': 'id',
            'lockout_duration': 'lockout_duration',
            'lockout_threshold': 'lockout_threshold',
            'lockout_window': 'lockout_window',
            'login_shell': 'login_shell',
            'machine_name': 'machine_name',
            'max_password_age': 'max_password_age',
            'min_password_age': 'min_password_age',
            'min_password_length': 'min_password_length',
            'name': 'name',
            'password_complexity': 'password_complexity',
            'password_history_length': 'password_history_length',
            'password_prompt_time': 'password_prompt_time',
            'status': 'status',
            'system': 'system'
        }

        self._authentication = None
        self._create_home_directory = None
        self._home_directory_template = None
        self._id = None
        self._lockout_duration = None
        self._lockout_threshold = None
        self._lockout_window = None
        self._login_shell = None
        self._machine_name = None
        self._max_password_age = None
        self._min_password_age = None
        self._min_password_length = None
        self._name = None
        self._password_complexity = None
        self._password_history_length = None
        self._password_prompt_time = None
        self._status = None
        self._system = None

    @property
    def authentication(self):
        """
        Gets the authentication of this ProvidersLocalLocalItem.
        If true, enables authentication and identity management through the authentication provider.

        :return: The authentication of this ProvidersLocalLocalItem.
        :rtype: bool
        """
        return self._authentication

    @authentication.setter
    def authentication(self, authentication):
        """
        Sets the authentication of this ProvidersLocalLocalItem.
        If true, enables authentication and identity management through the authentication provider.

        :param authentication: The authentication of this ProvidersLocalLocalItem.
        :type: bool
        """
        
        self._authentication = authentication

    @property
    def create_home_directory(self):
        """
        Gets the create_home_directory of this ProvidersLocalLocalItem.
        Automatically creates the home directory on the first login.

        :return: The create_home_directory of this ProvidersLocalLocalItem.
        :rtype: bool
        """
        return self._create_home_directory

    @create_home_directory.setter
    def create_home_directory(self, create_home_directory):
        """
        Sets the create_home_directory of this ProvidersLocalLocalItem.
        Automatically creates the home directory on the first login.

        :param create_home_directory: The create_home_directory of this ProvidersLocalLocalItem.
        :type: bool
        """
        
        self._create_home_directory = create_home_directory

    @property
    def home_directory_template(self):
        """
        Gets the home_directory_template of this ProvidersLocalLocalItem.
        Specifies the path to the home directory template.

        :return: The home_directory_template of this ProvidersLocalLocalItem.
        :rtype: str
        """
        return self._home_directory_template

    @home_directory_template.setter
    def home_directory_template(self, home_directory_template):
        """
        Sets the home_directory_template of this ProvidersLocalLocalItem.
        Specifies the path to the home directory template.

        :param home_directory_template: The home_directory_template of this ProvidersLocalLocalItem.
        :type: str
        """
        
        self._home_directory_template = home_directory_template

    @property
    def id(self):
        """
        Gets the id of this ProvidersLocalLocalItem.
        Specifies the local provider ID.

        :return: The id of this ProvidersLocalLocalItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProvidersLocalLocalItem.
        Specifies the local provider ID.

        :param id: The id of this ProvidersLocalLocalItem.
        :type: str
        """
        
        self._id = id

    @property
    def lockout_duration(self):
        """
        Gets the lockout_duration of this ProvidersLocalLocalItem.
        Specifies the length of time in seconds that an account will be inaccessible after multiple failed login attempts.

        :return: The lockout_duration of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._lockout_duration

    @lockout_duration.setter
    def lockout_duration(self, lockout_duration):
        """
        Sets the lockout_duration of this ProvidersLocalLocalItem.
        Specifies the length of time in seconds that an account will be inaccessible after multiple failed login attempts.

        :param lockout_duration: The lockout_duration of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._lockout_duration = lockout_duration

    @property
    def lockout_threshold(self):
        """
        Gets the lockout_threshold of this ProvidersLocalLocalItem.
        Specifies the number of failed login attempts necessary before an account is locked.

        :return: The lockout_threshold of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._lockout_threshold

    @lockout_threshold.setter
    def lockout_threshold(self, lockout_threshold):
        """
        Sets the lockout_threshold of this ProvidersLocalLocalItem.
        Specifies the number of failed login attempts necessary before an account is locked.

        :param lockout_threshold: The lockout_threshold of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._lockout_threshold = lockout_threshold

    @property
    def lockout_window(self):
        """
        Gets the lockout_window of this ProvidersLocalLocalItem.
        Specifies the duration of time in seconds in which the number of failed attempts set in the 'lockout_threshold' parameter must be made before an account is locked.

        :return: The lockout_window of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._lockout_window

    @lockout_window.setter
    def lockout_window(self, lockout_window):
        """
        Sets the lockout_window of this ProvidersLocalLocalItem.
        Specifies the duration of time in seconds in which the number of failed attempts set in the 'lockout_threshold' parameter must be made before an account is locked.

        :param lockout_window: The lockout_window of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._lockout_window = lockout_window

    @property
    def login_shell(self):
        """
        Gets the login_shell of this ProvidersLocalLocalItem.
        Specifies the login shell path.

        :return: The login_shell of this ProvidersLocalLocalItem.
        :rtype: str
        """
        return self._login_shell

    @login_shell.setter
    def login_shell(self, login_shell):
        """
        Sets the login_shell of this ProvidersLocalLocalItem.
        Specifies the login shell path.

        :param login_shell: The login_shell of this ProvidersLocalLocalItem.
        :type: str
        """
        
        self._login_shell = login_shell

    @property
    def machine_name(self):
        """
        Gets the machine_name of this ProvidersLocalLocalItem.
        Specifies the domain for this provider through which users and groups are qualified.

        :return: The machine_name of this ProvidersLocalLocalItem.
        :rtype: str
        """
        return self._machine_name

    @machine_name.setter
    def machine_name(self, machine_name):
        """
        Sets the machine_name of this ProvidersLocalLocalItem.
        Specifies the domain for this provider through which users and groups are qualified.

        :param machine_name: The machine_name of this ProvidersLocalLocalItem.
        :type: str
        """
        
        self._machine_name = machine_name

    @property
    def max_password_age(self):
        """
        Gets the max_password_age of this ProvidersLocalLocalItem.
        Specifies the maximum password age in seconds.

        :return: The max_password_age of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._max_password_age

    @max_password_age.setter
    def max_password_age(self, max_password_age):
        """
        Sets the max_password_age of this ProvidersLocalLocalItem.
        Specifies the maximum password age in seconds.

        :param max_password_age: The max_password_age of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._max_password_age = max_password_age

    @property
    def min_password_age(self):
        """
        Gets the min_password_age of this ProvidersLocalLocalItem.
        Specifies the minimum password age in seconds.

        :return: The min_password_age of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._min_password_age

    @min_password_age.setter
    def min_password_age(self, min_password_age):
        """
        Sets the min_password_age of this ProvidersLocalLocalItem.
        Specifies the minimum password age in seconds.

        :param min_password_age: The min_password_age of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._min_password_age = min_password_age

    @property
    def min_password_length(self):
        """
        Gets the min_password_length of this ProvidersLocalLocalItem.
        Specifies the minimum password length.

        :return: The min_password_length of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._min_password_length

    @min_password_length.setter
    def min_password_length(self, min_password_length):
        """
        Sets the min_password_length of this ProvidersLocalLocalItem.
        Specifies the minimum password length.

        :param min_password_length: The min_password_length of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._min_password_length = min_password_length

    @property
    def name(self):
        """
        Gets the name of this ProvidersLocalLocalItem.
        Specifies the local provider name.

        :return: The name of this ProvidersLocalLocalItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProvidersLocalLocalItem.
        Specifies the local provider name.

        :param name: The name of this ProvidersLocalLocalItem.
        :type: str
        """
        
        self._name = name

    @property
    def password_complexity(self):
        """
        Gets the password_complexity of this ProvidersLocalLocalItem.
        Specifies the conditions required for a password.

        :return: The password_complexity of this ProvidersLocalLocalItem.
        :rtype: list[str]
        """
        return self._password_complexity

    @password_complexity.setter
    def password_complexity(self, password_complexity):
        """
        Sets the password_complexity of this ProvidersLocalLocalItem.
        Specifies the conditions required for a password.

        :param password_complexity: The password_complexity of this ProvidersLocalLocalItem.
        :type: list[str]
        """
        
        self._password_complexity = password_complexity

    @property
    def password_history_length(self):
        """
        Gets the password_history_length of this ProvidersLocalLocalItem.
        Specifies the number of previous passwords to store.

        :return: The password_history_length of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._password_history_length

    @password_history_length.setter
    def password_history_length(self, password_history_length):
        """
        Sets the password_history_length of this ProvidersLocalLocalItem.
        Specifies the number of previous passwords to store.

        :param password_history_length: The password_history_length of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._password_history_length = password_history_length

    @property
    def password_prompt_time(self):
        """
        Gets the password_prompt_time of this ProvidersLocalLocalItem.
        Specifies the time in seconds remaining before a user will be prompted for a password change.

        :return: The password_prompt_time of this ProvidersLocalLocalItem.
        :rtype: int
        """
        return self._password_prompt_time

    @password_prompt_time.setter
    def password_prompt_time(self, password_prompt_time):
        """
        Sets the password_prompt_time of this ProvidersLocalLocalItem.
        Specifies the time in seconds remaining before a user will be prompted for a password change.

        :param password_prompt_time: The password_prompt_time of this ProvidersLocalLocalItem.
        :type: int
        """
        
        self._password_prompt_time = password_prompt_time

    @property
    def status(self):
        """
        Gets the status of this ProvidersLocalLocalItem.
        Specifies the status of the provider.

        :return: The status of this ProvidersLocalLocalItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ProvidersLocalLocalItem.
        Specifies the status of the provider.

        :param status: The status of this ProvidersLocalLocalItem.
        :type: str
        """
        
        self._status = status

    @property
    def system(self):
        """
        Gets the system of this ProvidersLocalLocalItem.
        If true, indicates that this provider instance was created by OneFS and cannot be removed.

        :return: The system of this ProvidersLocalLocalItem.
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """
        Sets the system of this ProvidersLocalLocalItem.
        If true, indicates that this provider instance was created by OneFS and cannot be removed.

        :param system: The system of this ProvidersLocalLocalItem.
        :type: bool
        """
        
        self._system = system

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
