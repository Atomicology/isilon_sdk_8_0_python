# coding: utf-8

"""
    Isilon SDK

    Isilon SDK - Language bindings for the OneFS API  # noqa: E501

    OpenAPI spec version: 8.0
    Contact: sdk@isilon.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import isi_sdk_8_0
from isi_sdk_8_0.api.worm_api import WormApi  # noqa: E501
from isi_sdk_8_0.rest import ApiException


class TestWormApi(unittest.TestCase):
    """WormApi unit test stubs"""

    def setUp(self):
        self.api = isi_sdk_8_0.api.worm_api.WormApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_worm_domain(self):
        """Test case for create_worm_domain

        """
        pass

    def test_get_worm_domain(self):
        """Test case for get_worm_domain

        """
        pass

    def test_get_worm_settings(self):
        """Test case for get_worm_settings

        """
        pass

    def test_list_worm_domains(self):
        """Test case for list_worm_domains

        """
        pass

    def test_update_worm_domain(self):
        """Test case for update_worm_domain

        """
        pass

    def test_update_worm_settings(self):
        """Test case for update_worm_settings

        """
        pass


if __name__ == '__main__':
    unittest.main()
