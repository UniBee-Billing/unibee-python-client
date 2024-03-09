# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_invoice_finish_post200_response import MerchantInvoiceFinishPost200Response

class TestMerchantInvoiceFinishPost200Response(unittest.TestCase):
    """MerchantInvoiceFinishPost200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantInvoiceFinishPost200Response:
        """Test MerchantInvoiceFinishPost200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantInvoiceFinishPost200Response`
        """
        model = MerchantInvoiceFinishPost200Response()
        if include_optional:
            return MerchantInvoiceFinishPost200Response(
                code = 56,
                data = openapi_client.models._merchant_invoice_finish_post_200_response_data._merchant_invoice_finish_post_200_response_data(
                    invoice = openapi_client.models.unibee/internal/model/entity/oversea_pay/invoice.unibee.internal.model.entity.oversea_pay.Invoice(
                        biz_type = 56, 
                        create_time = 56, 
                        currency = '', 
                        data = '', 
                        gateway_id = 56, 
                        gateway_invoice_id = '', 
                        gateway_invoice_pdf = '', 
                        gateway_payment_id = '', 
                        gateway_status = '', 
                        gmt_create = '', 
                        gmt_modify = '', 
                        id = 56, 
                        invoice_id = '', 
                        invoice_name = '', 
                        is_deleted = 56, 
                        lines = '', 
                        link = '', 
                        merchant_id = 56, 
                        payment_id = '', 
                        payment_link = '', 
                        period_end = 56, 
                        period_end_time = '', 
                        period_start = 56, 
                        period_start_time = '', 
                        refund_id = '', 
                        send_email = '', 
                        send_note = '', 
                        send_pdf = '', 
                        send_status = 56, 
                        send_terms = '', 
                        status = 56, 
                        subscription_amount = 56, 
                        subscription_amount_excluding_tax = 56, 
                        subscription_id = '', 
                        tax_amount = 56, 
                        tax_scale = 56, 
                        total_amount = 56, 
                        total_amount_excluding_tax = 56, 
                        unique_id = '', 
                        user_id = 56, ), ),
                message = '',
                redirect = '',
                request_id = ''
            )
        else:
            return MerchantInvoiceFinishPost200Response(
        )
        """

    def testMerchantInvoiceFinishPost200Response(self):
        """Test MerchantInvoiceFinishPost200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
