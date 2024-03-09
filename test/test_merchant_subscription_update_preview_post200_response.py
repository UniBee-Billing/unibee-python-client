# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_subscription_update_preview_post200_response import MerchantSubscriptionUpdatePreviewPost200Response

class TestMerchantSubscriptionUpdatePreviewPost200Response(unittest.TestCase):
    """MerchantSubscriptionUpdatePreviewPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantSubscriptionUpdatePreviewPost200Response:
        """Test MerchantSubscriptionUpdatePreviewPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantSubscriptionUpdatePreviewPost200Response`
        """
        model = MerchantSubscriptionUpdatePreviewPost200Response()
        if include_optional:
            return MerchantSubscriptionUpdatePreviewPost200Response(
                code = 56,
                data = openapi_client.models._merchant_subscription_update_preview_post_200_response_data._merchant_subscription_update_preview_post_200_response_data(
                    currency = '', 
                    invoice = openapi_client.models.unibee/internal/logic/gateway/ro/invoice_detail_simplify.unibee.internal.logic.gateway.ro.InvoiceDetailSimplify(
                        currency = '', 
                        invoice_id = '', 
                        invoice_name = '', 
                        lines = [
                            openapi_client.models.unibee/internal/logic/gateway/ro/invoice_item_detail_ro.unibee.internal.logic.gateway.ro.InvoiceItemDetailRo(
                                amount = 56, 
                                amount_excluding_tax = 56, 
                                currency = '', 
                                description = '', 
                                period_end = 56, 
                                period_start = 56, 
                                proration = True, 
                                quantity = 56, 
                                tax = 56, 
                                tax_scale = 56, 
                                unit_amount_excluding_tax = 56, )
                            ], 
                        period_end = 56, 
                        period_start = 56, 
                        proration_date = 56, 
                        proration_scale = 56, 
                        subscription_amount = 56, 
                        subscription_amount_excluding_tax = 56, 
                        tax_amount = 56, 
                        tax_scale = 56, 
                        total_amount = 56, 
                        total_amount_excluding_tax = 56, ), 
                    next_period_invoice = openapi_client.models.unibee/internal/logic/gateway/ro/invoice_detail_simplify.unibee.internal.logic.gateway.ro.InvoiceDetailSimplify(
                        currency = '', 
                        invoice_id = '', 
                        invoice_name = '', 
                        period_end = 56, 
                        period_start = 56, 
                        proration_date = 56, 
                        proration_scale = 56, 
                        subscription_amount = 56, 
                        subscription_amount_excluding_tax = 56, 
                        tax_amount = 56, 
                        tax_scale = 56, 
                        total_amount = 56, 
                        total_amount_excluding_tax = 56, ), 
                    proration_date = 56, 
                    total_amount = 56, ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantSubscriptionUpdatePreviewPost200Response(
        )
        """

    def testMerchantSubscriptionUpdatePreviewPost200Response(self):
        """Test MerchantSubscriptionUpdatePreviewPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
