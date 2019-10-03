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


class ArduinoDevicev2propertyvalueValueStatistics(object):
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
        'adr': 'float',
        'channel': 'float',
        'duplicate': 'float',
        'freq': 'float',
        'mod_bw': 'float',
        'rssi': 'float',
        'seqno': 'float',
        'sf': 'float',
        'snr': 'float',
        'time': 'float'
    }

    attribute_map = {
        'adr': 'adr',
        'channel': 'channel',
        'duplicate': 'duplicate',
        'freq': 'freq',
        'mod_bw': 'modBW',
        'rssi': 'rssi',
        'seqno': 'seqno',
        'sf': 'sf',
        'snr': 'snr',
        'time': 'time'
    }

    def __init__(self, adr=None, channel=None, duplicate=None, freq=None, mod_bw=None, rssi=None, seqno=None, sf=None, snr=None, time=None):  # noqa: E501
        """ArduinoDevicev2propertyvalueValueStatistics - a model defined in OpenAPI"""  # noqa: E501

        self._adr = None
        self._channel = None
        self._duplicate = None
        self._freq = None
        self._mod_bw = None
        self._rssi = None
        self._seqno = None
        self._sf = None
        self._snr = None
        self._time = None
        self.discriminator = None

        if adr is not None:
            self.adr = adr
        if channel is not None:
            self.channel = channel
        if duplicate is not None:
            self.duplicate = duplicate
        if freq is not None:
            self.freq = freq
        if mod_bw is not None:
            self.mod_bw = mod_bw
        if rssi is not None:
            self.rssi = rssi
        if seqno is not None:
            self.seqno = seqno
        if sf is not None:
            self.sf = sf
        if snr is not None:
            self.snr = snr
        if time is not None:
            self.time = time

    @property
    def adr(self):
        """Gets the adr of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The adr of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._adr

    @adr.setter
    def adr(self, adr):
        """Sets the adr of this ArduinoDevicev2propertyvalueValueStatistics.


        :param adr: The adr of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._adr = adr

    @property
    def channel(self):
        """Gets the channel of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The channel of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this ArduinoDevicev2propertyvalueValueStatistics.


        :param channel: The channel of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._channel = channel

    @property
    def duplicate(self):
        """Gets the duplicate of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The duplicate of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._duplicate

    @duplicate.setter
    def duplicate(self, duplicate):
        """Sets the duplicate of this ArduinoDevicev2propertyvalueValueStatistics.


        :param duplicate: The duplicate of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._duplicate = duplicate

    @property
    def freq(self):
        """Gets the freq of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The freq of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._freq

    @freq.setter
    def freq(self, freq):
        """Sets the freq of this ArduinoDevicev2propertyvalueValueStatistics.


        :param freq: The freq of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._freq = freq

    @property
    def mod_bw(self):
        """Gets the mod_bw of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The mod_bw of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._mod_bw

    @mod_bw.setter
    def mod_bw(self, mod_bw):
        """Sets the mod_bw of this ArduinoDevicev2propertyvalueValueStatistics.


        :param mod_bw: The mod_bw of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._mod_bw = mod_bw

    @property
    def rssi(self):
        """Gets the rssi of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The rssi of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._rssi

    @rssi.setter
    def rssi(self, rssi):
        """Sets the rssi of this ArduinoDevicev2propertyvalueValueStatistics.


        :param rssi: The rssi of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._rssi = rssi

    @property
    def seqno(self):
        """Gets the seqno of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The seqno of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._seqno

    @seqno.setter
    def seqno(self, seqno):
        """Sets the seqno of this ArduinoDevicev2propertyvalueValueStatistics.


        :param seqno: The seqno of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._seqno = seqno

    @property
    def sf(self):
        """Gets the sf of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The sf of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._sf

    @sf.setter
    def sf(self, sf):
        """Sets the sf of this ArduinoDevicev2propertyvalueValueStatistics.


        :param sf: The sf of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._sf = sf

    @property
    def snr(self):
        """Gets the snr of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The snr of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._snr

    @snr.setter
    def snr(self, snr):
        """Sets the snr of this ArduinoDevicev2propertyvalueValueStatistics.


        :param snr: The snr of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._snr = snr

    @property
    def time(self):
        """Gets the time of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501


        :return: The time of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this ArduinoDevicev2propertyvalueValueStatistics.


        :param time: The time of this ArduinoDevicev2propertyvalueValueStatistics.  # noqa: E501
        :type: float
        """

        self._time = time

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
        if not isinstance(other, ArduinoDevicev2propertyvalueValueStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other