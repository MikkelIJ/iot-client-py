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


class ArduinoDashboardlist(object):
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
        'dashboards': 'list[ArduinoDashboard]'
    }

    attribute_map = {
        'dashboards': 'dashboards'
    }

    def __init__(self, dashboards=None):  # noqa: E501
        """ArduinoDashboardlist - a model defined in OpenAPI"""  # noqa: E501

        self._dashboards = None
        self.discriminator = None

        self.dashboards = dashboards

    @property
    def dashboards(self):
        """Gets the dashboards of this ArduinoDashboardlist.  # noqa: E501

        The dashboards of the users  # noqa: E501

        :return: The dashboards of this ArduinoDashboardlist.  # noqa: E501
        :rtype: list[ArduinoDashboard]
        """
        return self._dashboards

    @dashboards.setter
    def dashboards(self, dashboards):
        """Sets the dashboards of this ArduinoDashboardlist.

        The dashboards of the users  # noqa: E501

        :param dashboards: The dashboards of this ArduinoDashboardlist.  # noqa: E501
        :type: list[ArduinoDashboard]
        """
        if dashboards is None:
            raise ValueError("Invalid value for `dashboards`, must not be `None`")  # noqa: E501

        self._dashboards = dashboards

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
        if not isinstance(other, ArduinoDashboardlist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
