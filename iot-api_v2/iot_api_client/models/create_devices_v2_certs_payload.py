# coding: utf-8

"""
    Iot API

    Collection of all public API endpoints.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class CreateDevicesV2CertsPayload(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'ca': 'str',
        'csr': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'ca': 'ca',
        'csr': 'csr',
        'enabled': 'enabled'
    }

    def __init__(self, ca=None, csr=None, enabled=None):  # noqa: E501
        """CreateDevicesV2CertsPayload - a model defined in OpenAPI"""  # noqa: E501

        self._ca = None
        self._csr = None
        self._enabled = None
        self.discriminator = None

        if ca is not None:
            self.ca = ca
        self.csr = csr
        self.enabled = enabled

    @property
    def ca(self):
        """Gets the ca of this CreateDevicesV2CertsPayload.  # noqa: E501

        The Certification Authority you want to use  # noqa: E501

        :return: The ca of this CreateDevicesV2CertsPayload.  # noqa: E501
        :rtype: str
        """
        return self._ca

    @ca.setter
    def ca(self, ca):
        """Sets the ca of this CreateDevicesV2CertsPayload.

        The Certification Authority you want to use  # noqa: E501

        :param ca: The ca of this CreateDevicesV2CertsPayload.  # noqa: E501
        :type: str
        """

        self._ca = ca

    @property
    def csr(self):
        """Gets the csr of this CreateDevicesV2CertsPayload.  # noqa: E501

        The certificate request in pem format  # noqa: E501

        :return: The csr of this CreateDevicesV2CertsPayload.  # noqa: E501
        :rtype: str
        """
        return self._csr

    @csr.setter
    def csr(self, csr):
        """Sets the csr of this CreateDevicesV2CertsPayload.

        The certificate request in pem format  # noqa: E501

        :param csr: The csr of this CreateDevicesV2CertsPayload.  # noqa: E501
        :type: str
        """
        if csr is None:
            raise ValueError("Invalid value for `csr`, must not be `None`")  # noqa: E501
        if csr is not None and len(csr) > 1024:
            raise ValueError("Invalid value for `csr`, length must be less than or equal to `1024`")  # noqa: E501

        self._csr = csr

    @property
    def enabled(self):
        """Gets the enabled of this CreateDevicesV2CertsPayload.  # noqa: E501

        Whether the certificate is enabled  # noqa: E501

        :return: The enabled of this CreateDevicesV2CertsPayload.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CreateDevicesV2CertsPayload.

        Whether the certificate is enabled  # noqa: E501

        :param enabled: The enabled of this CreateDevicesV2CertsPayload.  # noqa: E501
        :type: bool
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, CreateDevicesV2CertsPayload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
