# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_webhook_endpoint_list_res import UnibeeApiMerchantWebhookEndpointListRes

class TestUnibeeApiMerchantWebhookEndpointListRes(unittest.TestCase):
    """UnibeeApiMerchantWebhookEndpointListRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantWebhookEndpointListRes:
        """Test UnibeeApiMerchantWebhookEndpointListRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantWebhookEndpointListRes`
        """
        model = UnibeeApiMerchantWebhookEndpointListRes()
        if include_optional:
            return UnibeeApiMerchantWebhookEndpointListRes(
                endpoint_list = [
                    openapi_client.models.unibee/internal/logic/webhook/merchant_webhook_endpoint_vo.unibee.internal.logic.webhook.MerchantWebhookEndpointVo(
                        create_time = 56, 
                        gmt_modify = 56, 
                        id = 56, 
                        merchant_id = 56, 
                        webhook_events = [
                            ''
                            ], 
                        webhook_url = '', )
                    ]
            )
        else:
            return UnibeeApiMerchantWebhookEndpointListRes(
        )
        """

    def testUnibeeApiMerchantWebhookEndpointListRes(self):
        """Test UnibeeApiMerchantWebhookEndpointListRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
