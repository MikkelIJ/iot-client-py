# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import iot_api_client
from iot_api_client.api.cleanup_api import CleanupApi  # noqa: E501
from iot_api_client.rest import ApiException


class TestCleanupApi(unittest.TestCase):
    """CleanupApi unit test stubs"""

    def setUp(self):
        self.api = iot_api_client.api.cleanup_api.CleanupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_cleanup_iot(self):
        """Test case for cleanup_iot

        iot cleanup  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
