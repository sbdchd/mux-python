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


class ListFiltersResponseData(object):
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
        'basic': 'list[str]',
        'advanced': 'list[str]'
    }

    attribute_map = {
        'basic': 'basic',
        'advanced': 'advanced'
    }

    def __init__(self, basic=None, advanced=None, local_vars_configuration=None):  # noqa: E501
        """ListFiltersResponseData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._basic = None
        self._advanced = None
        self.discriminator = None

        if basic is not None:
            self.basic = basic
        if advanced is not None:
            self.advanced = advanced

    @property
    def basic(self):
        """Gets the basic of this ListFiltersResponseData.  # noqa: E501


        :return: The basic of this ListFiltersResponseData.  # noqa: E501
        :rtype: list[str]
        """
        return self._basic

    @basic.setter
    def basic(self, basic):
        """Sets the basic of this ListFiltersResponseData.


        :param basic: The basic of this ListFiltersResponseData.  # noqa: E501
        :type basic: list[str]
        """

        self._basic = basic

    @property
    def advanced(self):
        """Gets the advanced of this ListFiltersResponseData.  # noqa: E501


        :return: The advanced of this ListFiltersResponseData.  # noqa: E501
        :rtype: list[str]
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this ListFiltersResponseData.


        :param advanced: The advanced of this ListFiltersResponseData.  # noqa: E501
        :type advanced: list[str]
        """

        self._advanced = advanced

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
        if not isinstance(other, ListFiltersResponseData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListFiltersResponseData):
            return True

        return self.to_dict() != other.to_dict()
