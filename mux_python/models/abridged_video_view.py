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


class AbridgedVideoView(object):
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
        'id': 'str',
        'viewer_os_family': 'str',
        'viewer_application_name': 'str',
        'video_title': 'str',
        'total_row_count': 'int',
        'player_error_message': 'str',
        'player_error_code': 'str',
        'error_type_id': 'int',
        'country_code': 'str',
        'view_start': 'str',
        'view_end': 'str'
    }

    attribute_map = {
        'id': 'id',
        'viewer_os_family': 'viewer_os_family',
        'viewer_application_name': 'viewer_application_name',
        'video_title': 'video_title',
        'total_row_count': 'total_row_count',
        'player_error_message': 'player_error_message',
        'player_error_code': 'player_error_code',
        'error_type_id': 'error_type_id',
        'country_code': 'country_code',
        'view_start': 'view_start',
        'view_end': 'view_end'
    }

    def __init__(self, id=None, viewer_os_family=None, viewer_application_name=None, video_title=None, total_row_count=None, player_error_message=None, player_error_code=None, error_type_id=None, country_code=None, view_start=None, view_end=None, local_vars_configuration=None):  # noqa: E501
        """AbridgedVideoView - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._viewer_os_family = None
        self._viewer_application_name = None
        self._video_title = None
        self._total_row_count = None
        self._player_error_message = None
        self._player_error_code = None
        self._error_type_id = None
        self._country_code = None
        self._view_start = None
        self._view_end = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if viewer_os_family is not None:
            self.viewer_os_family = viewer_os_family
        if viewer_application_name is not None:
            self.viewer_application_name = viewer_application_name
        if video_title is not None:
            self.video_title = video_title
        if total_row_count is not None:
            self.total_row_count = total_row_count
        if player_error_message is not None:
            self.player_error_message = player_error_message
        if player_error_code is not None:
            self.player_error_code = player_error_code
        if error_type_id is not None:
            self.error_type_id = error_type_id
        if country_code is not None:
            self.country_code = country_code
        if view_start is not None:
            self.view_start = view_start
        if view_end is not None:
            self.view_end = view_end

    @property
    def id(self):
        """Gets the id of this AbridgedVideoView.  # noqa: E501


        :return: The id of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AbridgedVideoView.


        :param id: The id of this AbridgedVideoView.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def viewer_os_family(self):
        """Gets the viewer_os_family of this AbridgedVideoView.  # noqa: E501


        :return: The viewer_os_family of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_os_family

    @viewer_os_family.setter
    def viewer_os_family(self, viewer_os_family):
        """Sets the viewer_os_family of this AbridgedVideoView.


        :param viewer_os_family: The viewer_os_family of this AbridgedVideoView.  # noqa: E501
        :type viewer_os_family: str
        """

        self._viewer_os_family = viewer_os_family

    @property
    def viewer_application_name(self):
        """Gets the viewer_application_name of this AbridgedVideoView.  # noqa: E501


        :return: The viewer_application_name of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._viewer_application_name

    @viewer_application_name.setter
    def viewer_application_name(self, viewer_application_name):
        """Sets the viewer_application_name of this AbridgedVideoView.


        :param viewer_application_name: The viewer_application_name of this AbridgedVideoView.  # noqa: E501
        :type viewer_application_name: str
        """

        self._viewer_application_name = viewer_application_name

    @property
    def video_title(self):
        """Gets the video_title of this AbridgedVideoView.  # noqa: E501


        :return: The video_title of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._video_title

    @video_title.setter
    def video_title(self, video_title):
        """Sets the video_title of this AbridgedVideoView.


        :param video_title: The video_title of this AbridgedVideoView.  # noqa: E501
        :type video_title: str
        """

        self._video_title = video_title

    @property
    def total_row_count(self):
        """Gets the total_row_count of this AbridgedVideoView.  # noqa: E501


        :return: The total_row_count of this AbridgedVideoView.  # noqa: E501
        :rtype: int
        """
        return self._total_row_count

    @total_row_count.setter
    def total_row_count(self, total_row_count):
        """Sets the total_row_count of this AbridgedVideoView.


        :param total_row_count: The total_row_count of this AbridgedVideoView.  # noqa: E501
        :type total_row_count: int
        """

        self._total_row_count = total_row_count

    @property
    def player_error_message(self):
        """Gets the player_error_message of this AbridgedVideoView.  # noqa: E501


        :return: The player_error_message of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_error_message

    @player_error_message.setter
    def player_error_message(self, player_error_message):
        """Sets the player_error_message of this AbridgedVideoView.


        :param player_error_message: The player_error_message of this AbridgedVideoView.  # noqa: E501
        :type player_error_message: str
        """

        self._player_error_message = player_error_message

    @property
    def player_error_code(self):
        """Gets the player_error_code of this AbridgedVideoView.  # noqa: E501


        :return: The player_error_code of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._player_error_code

    @player_error_code.setter
    def player_error_code(self, player_error_code):
        """Sets the player_error_code of this AbridgedVideoView.


        :param player_error_code: The player_error_code of this AbridgedVideoView.  # noqa: E501
        :type player_error_code: str
        """

        self._player_error_code = player_error_code

    @property
    def error_type_id(self):
        """Gets the error_type_id of this AbridgedVideoView.  # noqa: E501


        :return: The error_type_id of this AbridgedVideoView.  # noqa: E501
        :rtype: int
        """
        return self._error_type_id

    @error_type_id.setter
    def error_type_id(self, error_type_id):
        """Sets the error_type_id of this AbridgedVideoView.


        :param error_type_id: The error_type_id of this AbridgedVideoView.  # noqa: E501
        :type error_type_id: int
        """

        self._error_type_id = error_type_id

    @property
    def country_code(self):
        """Gets the country_code of this AbridgedVideoView.  # noqa: E501


        :return: The country_code of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this AbridgedVideoView.


        :param country_code: The country_code of this AbridgedVideoView.  # noqa: E501
        :type country_code: str
        """

        self._country_code = country_code

    @property
    def view_start(self):
        """Gets the view_start of this AbridgedVideoView.  # noqa: E501


        :return: The view_start of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_start

    @view_start.setter
    def view_start(self, view_start):
        """Sets the view_start of this AbridgedVideoView.


        :param view_start: The view_start of this AbridgedVideoView.  # noqa: E501
        :type view_start: str
        """

        self._view_start = view_start

    @property
    def view_end(self):
        """Gets the view_end of this AbridgedVideoView.  # noqa: E501


        :return: The view_end of this AbridgedVideoView.  # noqa: E501
        :rtype: str
        """
        return self._view_end

    @view_end.setter
    def view_end(self, view_end):
        """Sets the view_end of this AbridgedVideoView.


        :param view_end: The view_end of this AbridgedVideoView.  # noqa: E501
        :type view_end: str
        """

        self._view_end = view_end

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
        if not isinstance(other, AbridgedVideoView):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AbridgedVideoView):
            return True

        return self.to_dict() != other.to_dict()
