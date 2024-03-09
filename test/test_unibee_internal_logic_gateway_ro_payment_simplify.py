# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_logic_gateway_ro_payment_simplify import UnibeeInternalLogicGatewayRoPaymentSimplify

class TestUnibeeInternalLogicGatewayRoPaymentSimplify(unittest.TestCase):
    """UnibeeInternalLogicGatewayRoPaymentSimplify unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalLogicGatewayRoPaymentSimplify:
        """Test UnibeeInternalLogicGatewayRoPaymentSimplify
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalLogicGatewayRoPaymentSimplify`
        """
        model = UnibeeInternalLogicGatewayRoPaymentSimplify()
        if include_optional:
            return UnibeeInternalLogicGatewayRoPaymentSimplify(
                authorize_reason = '',
                authorize_status = 56,
                automatic = 56,
                balance_amount = 56,
                billing_reason = '',
                cancel_time = 56,
                country_code = '',
                create_time = 56,
                currency = '',
                external_payment_id = '',
                failure_reason = '',
                gateway_id = 56,
                gateway_payment_id = '',
                invoice_id = '',
                link = '',
                merchant_id = 56,
                paid_time = 56,
                payment_amount = 56,
                payment_id = '',
                refund_amount = 56,
                return_url = '',
                status = 56,
                subscription_id = '',
                total_amount = 56,
                user_id = 56
            )
        else:
            return UnibeeInternalLogicGatewayRoPaymentSimplify(
        )
        """

    def testUnibeeInternalLogicGatewayRoPaymentSimplify(self):
        """Test UnibeeInternalLogicGatewayRoPaymentSimplify"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
