# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server

    The version of the OpenAPI document: buildtime:202404131246 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_bean_detail_payment_detail import UnibeeApiBeanDetailPaymentDetail

class TestUnibeeApiBeanDetailPaymentDetail(unittest.TestCase):
    """UnibeeApiBeanDetailPaymentDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiBeanDetailPaymentDetail:
        """Test UnibeeApiBeanDetailPaymentDetail
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiBeanDetailPaymentDetail`
        """
        model = UnibeeApiBeanDetailPaymentDetail()
        if include_optional:
            return UnibeeApiBeanDetailPaymentDetail(
                payment = openapi_client.models.unibee/api/bean/payment_simplify.unibee.api.bean.PaymentSimplify(
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
                    gas_payer = '', 
                    gateway_id = 56, 
                    gateway_payment_id = '', 
                    invoice_id = '', 
                    link = '', 
                    merchant_id = 56, 
                    metadata = {
                        'key' : ''
                        }, 
                    paid_time = 56, 
                    payment_amount = 56, 
                    payment_id = '', 
                    refund_amount = 56, 
                    return_url = '', 
                    status = 56, 
                    subscription_id = '', 
                    total_amount = 56, 
                    user_id = 56, ),
                user = openapi_client.models.unibee/api/bean/user_account_simplify.unibee.api.bean.UserAccountSimplify(
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
                    id = 56, 
                    is_risk = 56, 
                    is_special = 56, 
                    last_login_at = 56, 
                    last_name = '', 
                    linked_in = '', 
                    merchant_id = 56, 
                    mobile = '', 
                    other_social_info = '', 
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
                    whats_app = '', )
            )
        else:
            return UnibeeApiBeanDetailPaymentDetail(
        )
        """

    def testUnibeeApiBeanDetailPaymentDetail(self):
        """Test UnibeeApiBeanDetailPaymentDetail"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
