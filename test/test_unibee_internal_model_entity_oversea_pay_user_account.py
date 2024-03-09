# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_internal_model_entity_oversea_pay_user_account import UnibeeInternalModelEntityOverseaPayUserAccount

class TestUnibeeInternalModelEntityOverseaPayUserAccount(unittest.TestCase):
    """UnibeeInternalModelEntityOverseaPayUserAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeInternalModelEntityOverseaPayUserAccount:
        """Test UnibeeInternalModelEntityOverseaPayUserAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeInternalModelEntityOverseaPayUserAccount`
        """
        model = UnibeeInternalModelEntityOverseaPayUserAccount()
        if include_optional:
            return UnibeeInternalModelEntityOverseaPayUserAccount(
                address = '',
                avatar_url = '',
                billing_type = 56,
                birthday = '',
                company_name = '',
                country_code = '',
                country_name = '',
                create_time = 56,
                custom = '',
                email = '',
                external_user_id = '',
                facebook = '',
                first_name = '',
                gateway_id = '',
                gender = '',
                gmt_create = '',
                gmt_modify = '',
                id = 56,
                is_deleted = 56,
                is_risk = 56,
                is_special = 56,
                last_login_at = 56,
                last_name = '',
                linked_in = '',
                merchant_id = 56,
                mobile = '',
                other_social_info = '',
                password = '',
                payment_method = '',
                phone = '',
                profession = '',
                re_mark = '',
                recurring_amount = 56,
                school = '',
                status = 56,
                subscription_id = '',
                subscription_name = '',
                subscription_status = 56,
                telegram = '',
                tik_tok = '',
                time_zone = '',
                user_name = '',
                v_at_number = '',
                version = 56,
                we_chat = '',
                whats_app = ''
            )
        else:
            return UnibeeInternalModelEntityOverseaPayUserAccount(
        )
        """

    def testUnibeeInternalModelEntityOverseaPayUserAccount(self):
        """Test UnibeeInternalModelEntityOverseaPayUserAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
