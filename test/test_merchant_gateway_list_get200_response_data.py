# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.merchant_gateway_list_get200_response_data import MerchantGatewayListGet200ResponseData

class TestMerchantGatewayListGet200ResponseData(unittest.TestCase):
    """MerchantGatewayListGet200ResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MerchantGatewayListGet200ResponseData:
        """Test MerchantGatewayListGet200ResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MerchantGatewayListGet200ResponseData`
        """
        model = MerchantGatewayListGet200ResponseData()
        if include_optional:
            return MerchantGatewayListGet200ResponseData(
                gateways = [
                    openapi_client.models.unibee/internal/logic/gateway/ro/gateway_simplify.unibee.internal.logic.gateway.ro.GatewaySimplify(
                        gateway_id = 56, 
                        gateway_logo = '', 
                        gateway_name = '', )
                    ]
            )
        else:
            return MerchantGatewayListGet200ResponseData(
        )
        """

    def testMerchantGatewayListGet200ResponseData(self):
        """Test MerchantGatewayListGet200ResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
