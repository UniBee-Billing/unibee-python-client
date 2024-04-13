# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_payment_method_new_post200_response_data import MerchantPaymentMethodNewPost200ResponseData

class TestMerchantPaymentMethodNewPost200ResponseData(unittest.TestCase):
    """MerchantPaymentMethodNewPost200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantPaymentMethodNewPost200ResponseData:
        """Test MerchantPaymentMethodNewPost200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantPaymentMethodNewPost200ResponseData`
        """
        model = MerchantPaymentMethodNewPost200ResponseData()
        if include_optional:
            return MerchantPaymentMethodNewPost200ResponseData(
                method = openapi_client.models.unibee/api/bean/payment_method.unibee.api.bean.PaymentMethod(
                    data = openapi_client.models.data.data(), 
                    id = '', 
                    type = '', ),
                url = ''
            )
        else:
            return MerchantPaymentMethodNewPost200ResponseData(
        )
        """

    def testMerchantPaymentMethodNewPost200ResponseData(self):
        """Test MerchantPaymentMethodNewPost200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
