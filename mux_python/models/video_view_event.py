# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from mux_python.configuration import Configuration


class VideoViewEvent(object):
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
        'viewer_time': 'int',
        'playback_time': 'int',
        'name': 'str',
        'event_time': 'int'
    }

    attribute_map = {
        'viewer_time': 'viewer_time',
        'playback_time': 'playback_time',
        'name': 'name',
        'event_time': 'event_time'
    }

    def __init__(self, viewer_time=None, playback_time=None, name=None, event_time=None, local_vars_configuration=None):  # noqa: E501
        """VideoViewEvent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._viewer_time = None
        self._playback_time = None
        self._name = None
        self._event_time = None
        self.discriminator = None

        if viewer_time is not None:
            self.viewer_time = viewer_time
        if playback_time is not None:
            self.playback_time = playback_time
        if name is not None:
            self.name = name
        if event_time is not None:
            self.event_time = event_time

    @property
    def viewer_time(self):
        """Gets the viewer_time of this VideoViewEvent.  # noqa: E501


        :return: The viewer_time of this VideoViewEvent.  # noqa: E501
        :rtype: int
        """
        return self._viewer_time

    @viewer_time.setter
    def viewer_time(self, viewer_time):
        """Sets the viewer_time of this VideoViewEvent.


        :param viewer_time: The viewer_time of this VideoViewEvent.  # noqa: E501
        :type viewer_time: int
        """

        self._viewer_time = viewer_time

    @property
    def playback_time(self):
        """Gets the playback_time of this VideoViewEvent.  # noqa: E501


        :return: The playback_time of this VideoViewEvent.  # noqa: E501
        :rtype: int
        """
        return self._playback_time

    @playback_time.setter
    def playback_time(self, playback_time):
        """Sets the playback_time of this VideoViewEvent.


        :param playback_time: The playback_time of this VideoViewEvent.  # noqa: E501
        :type playback_time: int
        """

        self._playback_time = playback_time

    @property
    def name(self):
        """Gets the name of this VideoViewEvent.  # noqa: E501


        :return: The name of this VideoViewEvent.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VideoViewEvent.


        :param name: The name of this VideoViewEvent.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def event_time(self):
        """Gets the event_time of this VideoViewEvent.  # noqa: E501


        :return: The event_time of this VideoViewEvent.  # noqa: E501
        :rtype: int
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this VideoViewEvent.


        :param event_time: The event_time of this VideoViewEvent.  # noqa: E501
        :type event_time: int
        """

        self._event_time = event_time

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VideoViewEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VideoViewEvent):
            return True

        return self.to_dict() != other.to_dict()
