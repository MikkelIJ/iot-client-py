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
from iot_api_client.api.lora_devices_v1_api import LoraDevicesV1Api  # noqa: E501
from iot_api_client.rest import ApiException


class TestLoraDevicesV1Api(unittest.TestCase):
    """LoraDevicesV1Api unit test stubs"""

    def setUp(self):
        self.api = iot_api_client.api.lora_devices_v1_api.LoraDevicesV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_lora_devices_v1_create(self):
        """Test case for lora_devices_v1_create

        create lora_devices_v1  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
