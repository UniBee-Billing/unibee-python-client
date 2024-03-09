# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_model_entity_oversea_pay_payment_timeline import UnibeeInternalModelEntityOverseaPayPaymentTimeline

class TestUnibeeInternalModelEntityOverseaPayPaymentTimeline(unittest.TestCase):
    """UnibeeInternalModelEntityOverseaPayPaymentTimeline unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalModelEntityOverseaPayPaymentTimeline:
        """Test UnibeeInternalModelEntityOverseaPayPaymentTimeline
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalModelEntityOverseaPayPaymentTimeline`
        """
        model = UnibeeInternalModelEntityOverseaPayPaymentTimeline()
        if include_optional:
            return UnibeeInternalModelEntityOverseaPayPaymentTimeline(
                create_time = 56,
                currency = '',
                gateway_id = 56,
                gmt_create = '',
                gmt_modify = '',
                id = 56,
                invoice_id = '',
                is_deleted = 56,
                merchant_id = 56,
                payment_id = '',
                status = 56,
                subscription_id = '',
                timeline_type = 56,
                total_amount = 56,
                unique_id = '',
                user_id = 56
            )
        else:
            return UnibeeInternalModelEntityOverseaPayPaymentTimeline(
        )
        """

    def testUnibeeInternalModelEntityOverseaPayPaymentTimeline(self):
        """Test UnibeeInternalModelEntityOverseaPayPaymentTimeline"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
