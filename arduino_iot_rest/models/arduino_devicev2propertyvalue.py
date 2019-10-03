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


class ArduinoDevicev2propertyvalue(object):
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
        'created_at': 'datetime',
        'value': 'ArduinoDevicev2propertyvalueValue'
    }

    attribute_map = {
        'created_at': 'created_at',
        'value': 'value'
    }

    def __init__(self, created_at=None, value=None):  # noqa: E501
        """ArduinoDevicev2propertyvalue - a model defined in OpenAPI"""  # noqa: E501

        self._created_at = None
        self._value = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if value is not None:
            self.value = value

    @property
    def created_at(self):
        """Gets the created_at of this ArduinoDevicev2propertyvalue.  # noqa: E501


        :return: The created_at of this ArduinoDevicev2propertyvalue.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ArduinoDevicev2propertyvalue.


        :param created_at: The created_at of this ArduinoDevicev2propertyvalue.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def value(self):
        """Gets the value of this ArduinoDevicev2propertyvalue.  # noqa: E501


        :return: The value of this ArduinoDevicev2propertyvalue.  # noqa: E501
        :rtype: ArduinoDevicev2propertyvalueValue
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ArduinoDevicev2propertyvalue.


        :param value: The value of this ArduinoDevicev2propertyvalue.  # noqa: E501
        :type: ArduinoDevicev2propertyvalueValue
        """

        self._value = value

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
        if not isinstance(other, ArduinoDevicev2propertyvalue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other