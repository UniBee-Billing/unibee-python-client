# coding: utf-8

"""
    OpenAPI UniBee

    This is UniBee api server, For this sample, you can use the api key `EUXAgwv3Vcr1PFWt2SgBumMHXn3ImBqM` to test the authorization filters

    The version of the OpenAPI document: 
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.unibee_api_merchant_email_template_list_res import UnibeeApiMerchantEmailTemplateListRes

class TestUnibeeApiMerchantEmailTemplateListRes(unittest.TestCase):
    """UnibeeApiMerchantEmailTemplateListRes unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnibeeApiMerchantEmailTemplateListRes:
        """Test UnibeeApiMerchantEmailTemplateListRes
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnibeeApiMerchantEmailTemplateListRes`
        """
        model = UnibeeApiMerchantEmailTemplateListRes()
        if include_optional:
            return UnibeeApiMerchantEmailTemplateListRes(
                email_template_list = [
                    openapi_client.models.unibee/internal/query/email_template_vo.unibee.internal.query.EmailTemplateVo(
                        create_time = 56, 
                        id = 56, 
                        merchant_id = 56, 
                        status = '', 
                        template_attach_name = '', 
                        template_content = '', 
                        template_description = '', 
                        template_name = '', 
                        template_title = '', 
                        update_time = 56, )
                    ]
            )
        else:
            return UnibeeApiMerchantEmailTemplateListRes(
        )
        """

    def testUnibeeApiMerchantEmailTemplateListRes(self):
        """Test UnibeeApiMerchantEmailTemplateListRes"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
