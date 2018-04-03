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

from isi_sdk_8_0.models.create_compatibilities_class_active_item_response_merge import CreateCompatibilitiesClassActiveItemResponseMerge  # noqa: F401,E501
from isi_sdk_8_0.models.create_compatibilities_class_active_item_response_split import CreateCompatibilitiesClassActiveItemResponseSplit  # noqa: F401,E501


class CreateCompatibilitiesClassActiveItemResponse(object):
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
        'merges': 'list[CreateCompatibilitiesClassActiveItemResponseMerge]',
        'message': 'str',
        'splits': 'list[CreateCompatibilitiesClassActiveItemResponseSplit]'
    }

    attribute_map = {
        'merges': 'merges',
        'message': 'message',
        'splits': 'splits'
    }

    def __init__(self, merges=None, message=None, splits=None):  # noqa: E501
        """CreateCompatibilitiesClassActiveItemResponse - a model defined in Swagger"""  # noqa: E501

        self._merges = None
        self._message = None
        self._splits = None
        self.discriminator = None

        if merges is not None:
            self.merges = merges
        self.message = message
        if splits is not None:
            self.splits = splits

    @property
    def merges(self):
        """Gets the merges of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501

        A list of all merges that will occur given this compatibility operation  # noqa: E501

        :return: The merges of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501
        :rtype: list[CreateCompatibilitiesClassActiveItemResponseMerge]
        """
        return self._merges

    @merges.setter
    def merges(self, merges):
        """Sets the merges of this CreateCompatibilitiesClassActiveItemResponse.

        A list of all merges that will occur given this compatibility operation  # noqa: E501

        :param merges: The merges of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501
        :type: list[CreateCompatibilitiesClassActiveItemResponseMerge]
        """

        self._merges = merges

    @property
    def message(self):
        """Gets the message of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501

        A string describing the effects of the compatibility operation.  # noqa: E501

        :return: The message of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CreateCompatibilitiesClassActiveItemResponse.

        A string describing the effects of the compatibility operation.  # noqa: E501

        :param message: The message of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def splits(self):
        """Gets the splits of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501

        A list of all splits that will occur given this compatibility operation  # noqa: E501

        :return: The splits of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501
        :rtype: list[CreateCompatibilitiesClassActiveItemResponseSplit]
        """
        return self._splits

    @splits.setter
    def splits(self, splits):
        """Sets the splits of this CreateCompatibilitiesClassActiveItemResponse.

        A list of all splits that will occur given this compatibility operation  # noqa: E501

        :param splits: The splits of this CreateCompatibilitiesClassActiveItemResponse.  # noqa: E501
        :type: list[CreateCompatibilitiesClassActiveItemResponseSplit]
        """

        self._splits = splits

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
        if not isinstance(other, CreateCompatibilitiesClassActiveItemResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
