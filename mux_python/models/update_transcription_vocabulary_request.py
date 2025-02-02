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


class UpdateTranscriptionVocabularyRequest(object):
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
        'name': 'str',
        'phrases': 'list[str]',
        'passthrough': 'str'
    }

    attribute_map = {
        'name': 'name',
        'phrases': 'phrases',
        'passthrough': 'passthrough'
    }

    def __init__(self, name=None, phrases=None, passthrough=None, local_vars_configuration=None):  # noqa: E501
        """UpdateTranscriptionVocabularyRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._phrases = None
        self._passthrough = None
        self.discriminator = None

        if name is not None:
            self.name = name
        self.phrases = phrases
        if passthrough is not None:
            self.passthrough = passthrough

    @property
    def name(self):
        """Gets the name of this UpdateTranscriptionVocabularyRequest.  # noqa: E501

        The user-supplied name of the Transcription Vocabulary.  # noqa: E501

        :return: The name of this UpdateTranscriptionVocabularyRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTranscriptionVocabularyRequest.

        The user-supplied name of the Transcription Vocabulary.  # noqa: E501

        :param name: The name of this UpdateTranscriptionVocabularyRequest.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def phrases(self):
        """Gets the phrases of this UpdateTranscriptionVocabularyRequest.  # noqa: E501

        Phrases, individual words, or proper names to include in the Transcription Vocabulary. When the Transcription Vocabulary is attached to a live stream's `generated_subtitles`, the probability of successful speech recognition for these words or phrases is boosted.  # noqa: E501

        :return: The phrases of this UpdateTranscriptionVocabularyRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._phrases

    @phrases.setter
    def phrases(self, phrases):
        """Sets the phrases of this UpdateTranscriptionVocabularyRequest.

        Phrases, individual words, or proper names to include in the Transcription Vocabulary. When the Transcription Vocabulary is attached to a live stream's `generated_subtitles`, the probability of successful speech recognition for these words or phrases is boosted.  # noqa: E501

        :param phrases: The phrases of this UpdateTranscriptionVocabularyRequest.  # noqa: E501
        :type phrases: list[str]
        """
        if self.local_vars_configuration.client_side_validation and phrases is None:  # noqa: E501
            raise ValueError("Invalid value for `phrases`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                phrases is not None and len(phrases) > 1000):
            raise ValueError("Invalid value for `phrases`, number of items must be less than or equal to `1000`")  # noqa: E501

        self._phrases = phrases

    @property
    def passthrough(self):
        """Gets the passthrough of this UpdateTranscriptionVocabularyRequest.  # noqa: E501

        Arbitrary user-supplied metadata set for the Transcription Vocabulary. Max 255 characters.  # noqa: E501

        :return: The passthrough of this UpdateTranscriptionVocabularyRequest.  # noqa: E501
        :rtype: str
        """
        return self._passthrough

    @passthrough.setter
    def passthrough(self, passthrough):
        """Sets the passthrough of this UpdateTranscriptionVocabularyRequest.

        Arbitrary user-supplied metadata set for the Transcription Vocabulary. Max 255 characters.  # noqa: E501

        :param passthrough: The passthrough of this UpdateTranscriptionVocabularyRequest.  # noqa: E501
        :type passthrough: str
        """

        self._passthrough = passthrough

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
        if not isinstance(other, UpdateTranscriptionVocabularyRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateTranscriptionVocabularyRequest):
            return True

        return self.to_dict() != other.to_dict()
