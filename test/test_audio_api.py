# coding: utf-8

"""
    videoapi

    The video APIs help you convert, encode, and transcode videos.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import cloudmersive_video_api_client
from cloudmersive_video_api_client.api.audio_api import AudioApi  # noqa: E501
from cloudmersive_video_api_client.rest import ApiException


class TestAudioApi(unittest.TestCase):
    """AudioApi unit test stubs"""

    def setUp(self):
        self.api = cloudmersive_video_api_client.api.audio_api.AudioApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_audio_convert_to_aac(self):
        """Test case for audio_convert_to_aac

        Convert Audio File to AAC format.  # noqa: E501
        """
        pass

    def test_audio_convert_to_m4a(self):
        """Test case for audio_convert_to_m4a

        Convert Audio File to M4A format.  # noqa: E501
        """
        pass

    def test_audio_convert_to_mp3(self):
        """Test case for audio_convert_to_mp3

        Convert Audio File to MP3 format.  # noqa: E501
        """
        pass

    def test_audio_convert_to_wav(self):
        """Test case for audio_convert_to_wav

        Convert Audio File to WAV format.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
