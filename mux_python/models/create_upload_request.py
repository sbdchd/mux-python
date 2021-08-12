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


class CreateUploadRequest(object):
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
        'timeout': 'int',
        'cors_origin': 'str',
        'new_asset_settings': 'CreateAssetRequest',
        'test': 'bool'
    }

    attribute_map = {
        'timeout': 'timeout',
        'cors_origin': 'cors_origin',
        'new_asset_settings': 'new_asset_settings',
        'test': 'test'
    }

    def __init__(self, timeout=3600, cors_origin=None, new_asset_settings=None, test=None, local_vars_configuration=None):  # noqa: E501
        """CreateUploadRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._timeout = None
        self._cors_origin = None
        self._new_asset_settings = None
        self._test = None
        self.discriminator = None

        if timeout is not None:
            self.timeout = timeout
        if cors_origin is not None:
            self.cors_origin = cors_origin
        self.new_asset_settings = new_asset_settings
        if test is not None:
            self.test = test

    @property
    def timeout(self):
        """Gets the timeout of this CreateUploadRequest.  # noqa: E501

        Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked `timed_out`  # noqa: E501

        :return: The timeout of this CreateUploadRequest.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CreateUploadRequest.

        Max time in seconds for the signed upload URL to be valid. If a successful upload has not occurred before the timeout limit, the direct upload is marked `timed_out`  # noqa: E501

        :param timeout: The timeout of this CreateUploadRequest.  # noqa: E501
        :type timeout: int
        """
        if (self.local_vars_configuration.client_side_validation and
                timeout is not None and timeout > 604800):  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value less than or equal to `604800`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                timeout is not None and timeout < 60):  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `60`")  # noqa: E501

        self._timeout = timeout

    @property
    def cors_origin(self):
        """Gets the cors_origin of this CreateUploadRequest.  # noqa: E501

        If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers.  # noqa: E501

        :return: The cors_origin of this CreateUploadRequest.  # noqa: E501
        :rtype: str
        """
        return self._cors_origin

    @cors_origin.setter
    def cors_origin(self, cors_origin):
        """Sets the cors_origin of this CreateUploadRequest.

        If the upload URL will be used in a browser, you must specify the origin in order for the signed URL to have the correct CORS headers.  # noqa: E501

        :param cors_origin: The cors_origin of this CreateUploadRequest.  # noqa: E501
        :type cors_origin: str
        """

        self._cors_origin = cors_origin

    @property
    def new_asset_settings(self):
        """Gets the new_asset_settings of this CreateUploadRequest.  # noqa: E501


        :return: The new_asset_settings of this CreateUploadRequest.  # noqa: E501
        :rtype: CreateAssetRequest
        """
        return self._new_asset_settings

    @new_asset_settings.setter
    def new_asset_settings(self, new_asset_settings):
        """Sets the new_asset_settings of this CreateUploadRequest.


        :param new_asset_settings: The new_asset_settings of this CreateUploadRequest.  # noqa: E501
        :type new_asset_settings: CreateAssetRequest
        """
        if self.local_vars_configuration.client_side_validation and new_asset_settings is None:  # noqa: E501
            raise ValueError("Invalid value for `new_asset_settings`, must not be `None`")  # noqa: E501

        self._new_asset_settings = new_asset_settings

    @property
    def test(self):
        """Gets the test of this CreateUploadRequest.  # noqa: E501


        :return: The test of this CreateUploadRequest.  # noqa: E501
        :rtype: bool
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this CreateUploadRequest.


        :param test: The test of this CreateUploadRequest.  # noqa: E501
        :type test: bool
        """

        self._test = test

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
        if not isinstance(other, CreateUploadRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateUploadRequest):
            return True

        return self.to_dict() != other.to_dict()
