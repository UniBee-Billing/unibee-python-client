# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_payment_new_req import UnibeeApiMerchantPaymentNewReq

class TestUnibeeApiMerchantPaymentNewReq(unittest.TestCase):
    """UnibeeApiMerchantPaymentNewReq unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantPaymentNewReq:
        """Test UnibeeApiMerchantPaymentNewReq
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantPaymentNewReq`
        """
        model = UnibeeApiMerchantPaymentNewReq()
        if include_optional:
            return UnibeeApiMerchantPaymentNewReq(
                country_code = '',
                currency = '',
                email = '',
                external_payment_id = '',
                external_user_id = '',
                gateway_id = 56,
                line_items = [
                    openapi_client.models.unibee/api/merchant/payment/item.unibee.api.merchant.payment.Item(
                        description = '', 
                        image_url = '', 
                        product_url = '', 
                        quantity = 56, 
                        tax_scale = 56, 
                        unit_amount_excluding_tax = 56, )
                    ],
                redirect_url = '',
                reference = {
                    'key' : ''
                    },
                total_amount = 56
            )
        else:
            return UnibeeApiMerchantPaymentNewReq(
                country_code = '',
                currency = '',
                email = '',
                external_payment_id = '',
                external_user_id = '',
                gateway_id = 56,
                redirect_url = '',
                total_amount = 56,
        )
        """

    def testUnibeeApiMerchantPaymentNewReq(self):
        """Test UnibeeApiMerchantPaymentNewReq"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
