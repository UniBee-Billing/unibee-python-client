# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.user_metric import UserMetric


class TestUserMetric(unittest.TestCase):
    """UserMetric unit test stubs"""

    def setUp(self) -> None:
        self.api = UserMetric()

    def tearDown(self) -> None:
        pass

    def test_metric_user_metric_get(self) -> None:
        """Test case for metric_user_metric_get

        Query User Metric
        """
        pass


if __name__ == '__main__':
    unittest.main()
