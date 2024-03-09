# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_auth_register_verify_res import UnibeeApiMerchantAuthRegisterVerifyRes

class TestUnibeeApiMerchantAuthRegisterVerifyRes(unittest.TestCase):
    """UnibeeApiMerchantAuthRegisterVerifyRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantAuthRegisterVerifyRes:
        """Test UnibeeApiMerchantAuthRegisterVerifyRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantAuthRegisterVerifyRes`
        """
        model = UnibeeApiMerchantAuthRegisterVerifyRes()
        if include_optional:
            return UnibeeApiMerchantAuthRegisterVerifyRes(
                merchant_member = openapi_client.models.unibee/internal/model/entity/oversea_pay/merchant_member.unibee.internal.model.entity.oversea_pay.MerchantMember(
                    create_time = 56, 
                    email = '', 
                    first_name = '', 
                    gmt_create = '', 
                    gmt_modify = '', 
                    id = 56, 
                    is_deleted = 56, 
                    last_name = '', 
                    merchant_id = 56, 
                    mobile = '', 
                    password = '', 
                    user_name = '', )
            )
        else:
            return UnibeeApiMerchantAuthRegisterVerifyRes(
        )
        """

    def testUnibeeApiMerchantAuthRegisterVerifyRes(self):
        """Test UnibeeApiMerchantAuthRegisterVerifyRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
