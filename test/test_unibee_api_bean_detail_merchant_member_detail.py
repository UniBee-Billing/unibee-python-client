# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_bean_detail_merchant_member_detail import UnibeeApiBeanDetailMerchantMemberDetail

class TestUnibeeApiBeanDetailMerchantMemberDetail(unittest.TestCase):
    """UnibeeApiBeanDetailMerchantMemberDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiBeanDetailMerchantMemberDetail:
        """Test UnibeeApiBeanDetailMerchantMemberDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiBeanDetailMerchantMemberDetail`
        """
        model = UnibeeApiBeanDetailMerchantMemberDetail()
        if include_optional:
            return UnibeeApiBeanDetailMerchantMemberDetail(
                create_time = 56,
                email = '',
                first_name = '',
                id = 56,
                last_name = '',
                merchant_id = 56,
                mobile = '',
                permissions = [
                    openapi_client.models.unibee/api/bean/merchant_role_permission.unibee.api.bean.MerchantRolePermission(
                        group = '', 
                        permissions = [
                            ''
                            ], )
                    ],
                role = ''
            )
        else:
            return UnibeeApiBeanDetailMerchantMemberDetail(
        )
        """

    def testUnibeeApiBeanDetailMerchantMemberDetail(self):
        """Test UnibeeApiBeanDetailMerchantMemberDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
