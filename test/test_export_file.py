# coding: utf-8

"""
    Mux API

    Mux is how developers build online video. This API encompasses both Mux Video and Mux Data functionality to help you build your video-related projects better and faster than ever before.  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: devex@mux.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import mux_python
from mux_python.models.export_file import ExportFile  # noqa: E501
from mux_python.rest import ApiException

class TestExportFile(unittest.TestCase):
    """ExportFile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ExportFile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = mux_python.models.export_file.ExportFile()  # noqa: E501
        if include_optional :
            return ExportFile(
                version = 56, 
                type = '', 
                path = ''
            )
        else :
            return ExportFile(
        )

    def testExportFile(self):
        """Test ExportFile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
