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
from iot_api_client.api.supported_v1_api import SupportedV1Api  # noqa: E501
from iot_api_client.rest import ApiException


class TestSupportedV1Api(unittest.TestCase):
    """SupportedV1Api unit test stubs"""

    def setUp(self):
        self.api = iot_api_client.api.supported_v1_api.SupportedV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_supported_v1_devices(self):
        """Test case for supported_v1_devices

        devices supported_v1  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
