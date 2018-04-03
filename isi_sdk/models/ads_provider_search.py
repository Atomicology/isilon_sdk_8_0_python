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

from isi_sdk_8_0.models.ads_provider_search_object import AdsProviderSearchObject  # noqa: F401,E501


class AdsProviderSearch(object):
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
        'objects': 'list[AdsProviderSearchObject]',
        'resume': 'str'
    }

    attribute_map = {
        'objects': 'objects',
        'resume': 'resume'
    }

    def __init__(self, objects=None, resume=None):  # noqa: E501
        """AdsProviderSearch - a model defined in Swagger"""  # noqa: E501

        self._objects = None
        self._resume = None
        self.discriminator = None

        if objects is not None:
            self.objects = objects
        if resume is not None:
            self.resume = resume

    @property
    def objects(self):
        """Gets the objects of this AdsProviderSearch.  # noqa: E501


        :return: The objects of this AdsProviderSearch.  # noqa: E501
        :rtype: list[AdsProviderSearchObject]
        """
        return self._objects

    @objects.setter
    def objects(self, objects):
        """Sets the objects of this AdsProviderSearch.


        :param objects: The objects of this AdsProviderSearch.  # noqa: E501
        :type: list[AdsProviderSearchObject]
        """

        self._objects = objects

    @property
    def resume(self):
        """Gets the resume of this AdsProviderSearch.  # noqa: E501

        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).  # noqa: E501

        :return: The resume of this AdsProviderSearch.  # noqa: E501
        :rtype: str
        """
        return self._resume

    @resume.setter
    def resume(self, resume):
        """Sets the resume of this AdsProviderSearch.

        Continue returning results from previous call using this token (token should come from the previous call, resume cannot be used with other options).  # noqa: E501

        :param resume: The resume of this AdsProviderSearch.  # noqa: E501
        :type: str
        """

        self._resume = resume

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
        if not isinstance(other, AdsProviderSearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
